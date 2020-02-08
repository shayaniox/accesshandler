from bddrest import status, given, when

from accesshandler.models import Rule
from .helpers import LocalApplicableTestCase


class TestRule(LocalApplicableTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()
        cls.rule1 = Rule(pattern='/foo', limit=10)
        session.add(cls.rule1)
        session.commit()

    def test_delete(self):
        with self.given(
            f'Deleting an Rule',
            f'/apiv1/rules/id: {self.rule1.id}',
            f'DELETE',
        ):
            assert status == 200

            when(
                'Pattern is not found',
                url_parameters=given | dict(id=0)
            )
            assert status == 404

