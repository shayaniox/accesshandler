from datetime import timedelta

from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin
from sqlalchemy import Integer, Unicode, Boolean


class Rule(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'rule'

    id = Field(Integer, primary_key=True)
    pattern = Field(Unicode, python_type=str)
    limit = Field(Unicode, python_type=str)
    is_exact_url = Field(Boolean, python_type=bool, default=False)

    @property
    def limitvalue(self):
        value, timeunit = self.limit.split('/')
        return int(value)

    @property
    def limittimedelta(self):
        value, timeunit = self.limit.split('/')
        value = int(value)

        if timeunit == 'sec':
            return timedelta(seconds=1)
        elif timeunit == 'min':
            return timedelta(minutes=1)
        else: # timeunit == 'hr'
            return timedelta(hours=1)

