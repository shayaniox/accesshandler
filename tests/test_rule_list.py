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

    def test_list(self):
        with self.given(
            'List of rule',
            '/apiv1/rules',
            'LIST',
        ):
            assert status == 200
            assert len(response.json) == 3

            when('Trying to sorting response', query=dict(sort='id'))
            assert response.json[0]['id'] < response.json[1]['id']

            when('Sorting the response descending', query=dict(sort='-id'))
            assert response.json[0]['id'] > response.json[1]['id']

            when('Trying pagination response', query=dict(take=1))
            assert response.json[0]['id'] == 1
            assert len(response.json) == 1

            when('Trying pagination with skip', query=dict(take=1, skip=1))
            assert response.json[0]['id'] == 2
            assert len(response.json) == 1

            when(
                'Trying filtering response',
                query=dict(pattern=self.rule1.pattern)
            )
            assert response.json[0]['id'] == 1
            assert len(response.json) == 1

