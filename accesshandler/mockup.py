from restfulpy.orm import DBSession

from .models import Rule


def insert(): # pragma: no cover
    rule1 = Rule(pattern='/foo/bar', limit='10/min', is_exact_url=True)
    DBSession.add(rule1)

    rule2 = Rule(pattern='/foo/.*', limit='10/min')
    DBSession.add(rule2)
    DBSession.commit()
