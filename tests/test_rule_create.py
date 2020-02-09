from bddrest import status, given, when

from .helpers import LocalApplicableTestCase


class TestRule(LocalApplicableTestCase):

    def test_create(self):
        with self.given(
            'Creating an rule',
            '/apiv1/rules',
            'CREATE',
            json=dict(pattern='example.com/foo/bar', limit='20/min'),
        ):
            assert status == 200

            when(
                'Pattern is not in form',
                json=given - 'pattern',
            )
            assert status == '400 Pattern Is Required'

            when(
                'Limit is not in form',
                json=given - 'limit',
            )
            assert status == '400 Limit Is Required'

            when(
                'Limit format is wrong',
                json=given | dict(limit='20'),
            )
            assert status == '400 Wrong Limit Format'

            when(
                'Limit is not greater than 0',
                json=given | dict(limit='0/sec'),
            )
            assert status == '400 Limit Value Must Be Greater Than 0'

