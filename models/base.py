"""SQLAlchemy Models for General Mixins and Base extension"""

from sqlalchemy import Column, Index
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

from utils import camel_to_underscore


class DefinitionMixin(object):
    """Common properties for models that define entity concept

    Attributes:
        sort (integer)
        name (string, unique, required, indexed)
        short_description (string): Word or two about object
        long_description (string): Long description of object
        schema_name (string): Underscore/lower-case class name
    """

    sort = Column(Integer, default=0)
    name = Column(String(25), unique=True, nullable=False, index=True)
    short_description = Column(String(25))
    long_description = Column(String(100))
    active = Column(Boolean, default=True, index=True)

    def __str__(self):
        return "<{class_name}(Name={instance_name})>".format(
            class_name=self.__class__.__name__,
            instance_name=self.name
        )

    @hybrid_property
    def schema_name(self):
        return camel_to_underscore(self.name)