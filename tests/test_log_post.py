from bddrest import status, given, when

from accesshandler.models import Rule
from accesshandler.cache import redisconnection, keystr
from .helpers import LocalApplicableTestCase


class TestLog(LocalApplicableTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()
        cls.rule1 = Rule(pattern='/foo/bar', limit='2/min', is_exact_url=True)
        session.add(cls.rule1)

        cls.rule2 = Rule(pattern='/foo/.*', limit='2/min')
        session.add(cls.rule2)
        session.commit()

    def test_post(self):
        redisconn = redisconnection()
        redisconn.flushdb()
        json = dict(url=self.rule1.pattern, IP='1.1.1.1')

        with self.given(
            'Post a log to check if passed the limit or not',
            '/apiv1/logs',
            'POST',
            json=json,
        ):
            assert status == 200
            assert redisconn.get(keystr(json['IP'], json['url'])) == b'1'

            when('The specific IP viewed the url one more time')
            assert status == 200
            assert redisconn.get(keystr(json['IP'], json['url'])) == b'2'

            when('The specific IP viewed the url more than valid limitation')
            assert status == 429
            assert redisconn.get(keystr(json['IP'], json['url'])) == b'3'

            when(
                'IP field is not in form',
                json=given - 'IP',
            )
            assert status == 400

            when(
                'URL field is not in form',
                json=given - 'url',
            )
            assert status == 400

