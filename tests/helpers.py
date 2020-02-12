from os import path

from restfulpy.testing import ApplicableTestCase

from accesshandler import AccessHandler


HERE = path.abspath(path.dirname(__file__))
DATA_DIRECTORY = path.abspath(path.join(HERE, '../data'))


class LocalApplicableTestCase(ApplicableTestCase):
    __application__ = AccessHandler()
    __api_documentation_directory__ = path.join(DATA_DIRECTORY, 'markdown')


