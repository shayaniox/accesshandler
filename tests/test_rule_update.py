from bddrest import status, given, when, response

from accesshandler.models import Rule
from .helpers import LocalApplicableTestCase


class TestRule(LocalApplicableTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()
        cls.rule1 = Rule(pattern='/foo', limit=10)
        session.add(cls.rule1)

        cls.rule2 = Rule(pattern='/bar', limit=20)
        session.add(cls.rule2)

        cls.rule3 = Rule(pattern='/foo/bar/*', limit=30)
        session.add(cls.rule3)
        session.commit()

    def test_update(self):
        with self.given(
            f'Updating an rule',
            f'/apiv1/rules/id: {self.rule1.id}',
            f'UPDATE',
            json=dict(pattern='/foo/\\d', limit='100/sec')
        ):
            assert status == 200

            when(
                'Nothing exists in form',
                json=dict(),
            )
            assert status == '400 Empty Form'

            when(
                'Pattern is not in form',
                json=given | dict(pattern=None),
            )
            assert status == '400 Pattern Is Null'

            when(
                'Limit is not in form',
                json=given | dict(limit=None),
            )
            assert status == '400 Limit Is Null'

            when(
                'Limit format is wrong',
                json=given | dict(limit='10'),
            )
            assert status == '400 Wrong Limit Format'

            when(
                'Limit is not greater than 0',
                json=given | dict(limit='0/sec'),
            )
            assert status == '400 Limit Value Must Be Greater Than 0'

