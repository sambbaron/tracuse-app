"""SQLAlchemy Models for General Mixins and Base extension"""

from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.ext.hybrid import hybrid_property

from utils import camel_to_underscore


class SortActiveMixin(object):
    """Adds Sort and Active columns

    Attributes:
        sort (integer)
        active (boolean, indexed)
    """
    sort = Column(Integer, default=0)
    active = Column(Boolean, default=True, index=True)


class DefinitionMixin(SortActiveMixin):
    """Common properties for models that define entity concept

    Attributes:
        See SortActiveMixin
        name (string, not unique, required, indexed)
        short_description (string): Word or two about object
        long_description (string): Long description of object
        schema_name (string): Underscore/lower-case class name
    """
    #TODO problem with unique names and element types
    name = Column(String(25), unique=False, nullable=False, index=True)
    short_definition = Column(String(25))
    long_definition = Column(String(100))

    def __str__(self):
        return "<{class_name}(Name={instance_name})>".format(
            class_name=self.__class__.__name__,
            instance_name=self.name
        )

    @hybrid_property
    def schema_name(self):
        return camel_to_underscore(self.name)