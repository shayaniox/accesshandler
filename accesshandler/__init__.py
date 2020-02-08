from os.path import dirname

from restfulpy import Application

from accesshandler.controllers import Root


__version__ = '0.1.0'


class AccessHandler(Application):
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/accesshandler_dev
        test_url: postgresql://postgres:postgres@localhost/accesshandler_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres
   '''

    def __init__(self, application_name='accesshandler', root=Root()):
        super().__init__(
            application_name,
            root=root,
            path_=dirname(__file__),
        )


accesshandler = AccessHandler()

