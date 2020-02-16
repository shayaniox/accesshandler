import re

from nanohttp import json, HTTPNotFound, HTTPStatus, action, context
from restfulpy.controllers import RootController, RestController
from restfulpy.orm import commit, DBSession
from sqlalchemy import exists

import accesshandler
from .cache import redisconnection, setkey, keystr
from .models import Rule
from .validators import rule_validator, update_rule_validator, \
    LIMIT_PATTERN, log_validator, EXACT_URL_PATTERN


class LogController(RestController):

    def get_matching_patterns(self, url):
        '''
        Finds the patterns match the given url.
        First searches through the exact urls, then regex patterns.

        ...

        Parameters
        ----------
        url: str
        The url to search for matching patterns.
        '''

        exact_matching_pattern = DBSession.query(Rule) \
            .filter(Rule.is_exact_url == True) \
            .filter(Rule.pattern == url) \
            .first()
        if exact_matching_pattern is not None:
            yield exact_matching_pattern

        for rule in DBSession.query(Rule).filter(Rule.is_exact_url == False):
            if re.match(rule.pattern, url):
                yield rule

    @action
    @log_validator
    def post(self):
        ip = context.form['IP']
        url = context.form['url']
        redisconn = redisconnection()

        for rule in self.get_matching_patterns(url):
            viewcount = redisconn.get(keystr(ip, rule.pattern))
            if viewcount is None:
                setkey(redisconn, ip, rule.pattern, rule.limittimedelta)

            elif redisconn.incr(keystr(ip, rule.pattern)) > rule.limitvalue:
                raise HTTPStatus('429 Too Many Requests')


class RuleController(RestController):

    @rule_validator
    @json
    @commit
    def create(self):
        rule = Rule()
        rule.update_from_request()
        if int(rule.limit.split('/')[0]) <= 0:
            raise HTTPStatus('400 Limit Value Must Be Greater Than 0')

        if DBSession.query(
            exists().where(Rule.pattern == rule.pattern)
        ).scalar():
            raise HTTPStatus('400 Pattern Already Exists')

        if EXACT_URL_PATTERN.match(rule.pattern):
            rule.is_exact_url = True

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

        if DBSession.query(
            exists().where(Rule.pattern == rule.pattern)
        ).scalar():
            raise HTTPStatus('400 Pattern Already Exists')

        if EXACT_URL_PATTERN.match(rule.pattern):
            rule.is_exact_url = True

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
    logs = LogController()

    @json
    def version(self):
        return dict(version=accesshandler.__version__)


class Root(RootController):
    apiv1 = Apiv1()

