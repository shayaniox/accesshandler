from datetime import timedelta

from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin
from sqlalchemy import Integer, Unicode, Boolean


class Rule(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    '''
    A class used to represent an Animal

    ...

    Attributes
    ----------
    id : restfulpy.orm.Field
    A unique autoincremental identifier

    pattern : restfulpy.orm.Field
    The pattern that contains and regex. Example:
        'example.com/foo'

    limit : restfulpy.orm.Field
    The number of views per specific time interval

    is_exact_url : restfulpy.orm.Field
    Shows whether a pattern is an exact URL or not
    '''

    __tablename__ = 'rule'

    id = Field(Integer, primary_key=True)
    pattern = Field(Unicode, python_type=str)
    limit = Field(Unicode, python_type=str)
    is_exact_url = Field(Boolean, python_type=bool, default=False)

    @property
    def limitvalue(self):
        '''
        Gets valid number of views from limit field.
        '''

        value, timeunit = self.limit.split('/')
        return int(value)

    @property
    def limittimedelta(self):
        '''
        Gets timedelta from time unit of limit.
        '''

        value, timeunit = self.limit.split('/')
        value = int(value)

        if timeunit == 'sec':
            return timedelta(seconds=1)
        elif timeunit == 'min':
            return timedelta(minutes=1)
        else: # timeunit == 'hr'
            return timedelta(hours=1)

