from accesshandler.validators import LIMIT_PATTERN, EXACT_URL_PATTERN


def test_limit():
    assert LIMIT_PATTERN.match('2/sec')
    assert LIMIT_PATTERN.match('2/min')
    assert LIMIT_PATTERN.match('2/hr')
    assert not LIMIT_PATTERN.match('-1/hr')
    assert not LIMIT_PATTERN.match('a/hr')
    assert not LIMIT_PATTERN.match('1-hr')
    assert not LIMIT_PATTERN.match('1/a')
    assert not LIMIT_PATTERN.match('1/2')

def test_exact_url():
    assert EXACT_URL_PATTERN.match('example.com/foo')
    assert EXACT_URL_PATTERN.match('example.com')
    assert EXACT_URL_PATTERN.match('/foo/bar')
    assert not EXACT_URL_PATTERN.match('example.com/foo/.*')
    assert not EXACT_URL_PATTERN.match('example.com/foo/[a-z]')
    assert not EXACT_URL_PATTERN.match(r'example.com/foo/\d')
    assert not EXACT_URL_PATTERN.match(r'example.com/foo/.+')

