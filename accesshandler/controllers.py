from nanohttp import json, HTTPNotFound, HTTPStatus
from restfulpy.controllers import RootController, RestController
from restfulpy.orm import commit, DBSession

import accesshandler
from accesshandler.models import Rule
from accesshandler.validators import rule_validator, update_rule_validator, \
    LIMIT_PATTERN


class RuleController(RestController):

    @rule_validator
    @json
    @commit
    def create(self):
        rule = Rule()
        rule.update_from_request()
        if int(rule.limit.split('/')[0]) <= 0:
            raise HTTPStatus('400 Limit Value Must Be Greater Than 0')

        DBSession.add(rule)
        return rule

    @update_rule_validator
    @json(prevent_empty_form='400 Empty Form')
    @commit
    def update(self, id):
        rule = DBSession.query(Rule).filter(Rule.id == id).one_or_none()
        if rule is None:
            raise HTTPNotFound()

        rule.update_from_request()
        if int(rule.limit.split('/')[0]) <= 0:
            raise HTTPStatus('400 Limit Value Must Be Greater Than 0')

        DBSession.add(rule)
        return rule

    @json
    @commit
    def delete(self, id):
        rule = DBSession.query(Rule).filter(Rule.id == id).one_or_none()
        if rule is None:
            raise HTTPNotFound()

        DBSession.delete(rule)
        return rule

    @json
    @Rule.expose
    def list(self):
        return DBSession.query(Rule)


class Apiv1(RestController):

    rules = RuleController()

    @json
    def version(self):
        return dict(version=accesshandler.__version__)


class Root(RootController):
    apiv1 = Apiv1()

