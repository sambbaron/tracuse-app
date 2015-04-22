"""SQLAlchemy Models for Datum-related entities"""

from datetime import datetime

from sqlalchemy import Column, Index
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

from databases.postgres import Base

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


class DatumGroup(Base, DefinitionMixin):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See DefinitionMixin
    """

    __tablename__ = "datum_group"
    
    datum_group_id = Column(Integer, primary_key=True)

    datum_types = relationship("DatumType", backref="datum_group")
    group_rules = relationship("FilterRuleGroup", backref="datum_group")


class DatumType(Base, DefinitionMixin):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See DefinitionMixin
        datum_group_id: (integer, fk, required): DatumGroup
    """

    __tablename__ = "datum_type"

    datum_type_id = Column(Integer, primary_key=True)

    datum_group_id = Column(Integer,
                            ForeignKey('datum_group.datum_group_id'),
                            nullable=False
                            )

    datum_objects = relationship("DatumObject", backref="datum_type")
    element_types = relationship("ElementType", backref="datum_type")
    type_rules = relationship("FilterRuleType", backref="datum_type")


class DatumObject(Base, DefinitionMixin):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See DefinitionMixin
        user_id (integer, fk, required): User
        datum_type_id (integer, fk, required): DatumType
        creation_date (datetime)
    """

    __tablename__ = "datum_object"

    datum_object_id = Column(Integer, primary_key=True)

    user_id = Column(Integer,
                     ForeignKey("user.user_id"),
                     nullable=False,
                     index=True
                     )
    datum_type_id = Column(Integer,
                           ForeignKey("datum_type.datum_type_id"),
                           nullable=False
                           )
    creation_date = Column(DateTime, default=datetime.now())

    element_values = relationship("ElementValue", backref="datum_object")
    parent_associations = relationship("AssociationObject",
                                     primaryjoin="DatumObject.id == association_object.c.parent_datum_id",
                                     backref="child_associations")

    #TODO Property for associated Datums
    #TODO Property with element data


class ElementType(Base, DefinitionMixin):
    """Property types by Datum Type

    Has metadata

    Attributes:
        datum_type_id (integer, fk, nullable): DatumType
        data_type (string): Common string label of data types
        extended_properties (string): Other metadata properties (default, unique, etc.)
    """
    #TODO Entity-Attribute-Value anti-pattern: Metadata in table

    __tablename__ = "element_type"

    element_type_id = Column(Integer, primary_key=True)

    # Null datum type assumes applies to all Datum Types
    datum_type_id = Column(Integer,
                           ForeignKey("datum_type.datum_type_id"),
                           nullable=True
                           )
    data_type = Column(String(20))
    extended_properties = Column(String(100))

    element_options = relationship("ElementOption", backref="element_type")
    element_rules = relationship("FilterRuleElement", backref="element_type")


class ElementOption(Base, DefinitionMixin):
    """Value options for elements

    Example:
        Action Status - New, Someday, Upcoming, etc.

    Attributes:
        See DefinitionMixin
        element_type_id (integer, fk): ElementType
    """
    #TODO Entity-Attribute-Value anti-pattern: Enforce option values

    __tablename__ = "element_option"

    element_option_id = Column(Integer, primary_key=True)

    element_type_id = Column(Integer, ForeignKey("element_type.element_type_id"))

    element_values = relationship("ElementValue", backref="element_option")


class ElementValue(Base):
    """Element property values for Datums

    Attributes:
        datum_object_id (integer, fk): DatumObject
        element_type_id (integer, fk): ElementType
        element_option_id (integer, fk, nullable): ElementOption
        element_value (string): Can be anything
    """

    #TODO Entity-Attribute-Value anti-pattern: Avoid one giant table, manage constraints

    __tablename__ = "element_value"

    element_value_id = Column(Integer, primary_key=True)
    datum_object_id = Column(Integer, ForeignKey("datum_object.datum_object_id"))
    element_type_id = Column(Integer, ForeignKey("element_type.element_type_id"))
    element_option_id = Column(Integer, ForeignKey("element_option.element_option_id"), nullable=True)
    element_value = Column(String)


class AssociationType(Base, DefinitionMixin):
    """Types of relationships/edges between Datums

    Attributes:
        See DefinitionMixin
    """

    __tablename__ = "association_type"

    association_type_id = Column(Integer, primary_key=True)

    association_objects = relationship("AssociationObject", backref="association_type")
    association_rules = relationship("FilterRuleAssociation", backref="association_type")


class AssociationObject(Base):
    """Relationship between Datums

    Edge/Link in graph
    Using Closure table pattern
    Stores every path through tree

    Attributes:
        parent_datum_id (integer, pk, fk): DatumObject
        child_datum_id (integer, pk, fk): DatumObject
        depth (integer):  
        association_type_id (integer, fk): AssociationType
    """

    __tablename__ = "association_object"

    parent_datum_id = Column(Integer, ForeignKey("datum_object.datum_object_id"), primary_key=True)
    child_datum_id = Column(Integer, ForeignKey("datum_object.datum_object_id"), primary_key=True)
    depth = Column(Integer)
    association_type_id = Column(Integer, ForeignKey("association_type.association_type_id"))