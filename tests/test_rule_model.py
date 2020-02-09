from accesshandler.models import Rule


def test_limit_properties():

    rule1 = Rule(pattern='/foo/bar', limit='10/sec')
    assert rule1.limitvalue == 10
    assert rule1.limittimedelta.seconds == 1

    rule1.limit = '10/min'
    assert rule1.limittimedelta.seconds == 60

    rule1.limit = '10/hr'
    assert rule1.limittimedelta.seconds == 3600

