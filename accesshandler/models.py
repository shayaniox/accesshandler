from restfulpy.orm import Field, DeclarativeBase, OrderingMixin, \
    FilteringMixin, PaginationMixin
from sqlalchemy import Integer, Unicode


class Rule(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'Rule'

    id = Field(Integer, primary_key=True)
    pattern = Field(Unicode, python_type=str)
    limit = Field(Unicode, python_type=str)

