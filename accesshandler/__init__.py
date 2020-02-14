from os.path import dirname

from restfulpy import Application

from . import mockup
from .controllers import Root


__version__ = '0.1.0'


class AccessHandler(Application):
        #url: postgresql://postgres:postgres@localhost/accesshandler_dev
    __configuration__ = '''
      db:
        url: postgresql://postgres:@pg:5432/accesshandler
        test_url: postgresql://postgres:postgres@localhost/accesshandler_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres

      redis_:
        host: localhost
        port: 6379
        password: ~
        db: 1
   '''

    def __init__(self, application_name='accesshandler', root=Root()):
        super().__init__(
            application_name,
            root=root,
            path_=dirname(__file__),
        )

    def insert_mockup(self, *args): # pragma: no cover
        mockup.insert()


accesshandler = AccessHandler()

