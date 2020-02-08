import re

from nanohttp import HTTPBadRequest, validate

LIMIT_PATTERN = re.compile(r'^\d+\/(sec|min|hr)$')

rule_validator = validate(
    pattern=dict(
        required='400 Pattern Is Required',
    ),
    limit=dict(
        required='400 Limit Is Required',
        type_=(str, '400 Limit Must Be Alphabetical'),
        pattern=(LIMIT_PATTERN, '400 Wrong Limit Format'),
    ),
)


update_rule_validator = validate(
    pattern=dict(
        not_none='400 Pattern Is Null',
    ),
    limit=dict(
        not_none='400 Limit Is Null',
        type_=(str, '400 Limit Must Be Alphabetical'),
        pattern=(LIMIT_PATTERN, '400 Wrong Limit Format'),
    ),
)

