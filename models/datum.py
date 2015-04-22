"""SQLAlchemy Models for Datum-related entities"""

from datetime import datetime

from sqlalchemy import Column, Index
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

from databases.postgres import Base
from models.base import DefinitionMixin


class DatumGroup(DefinitionMixin, Base):
    """Collection of Datum Types

    Has common functional uses

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
    """

    __tablename__ = "datum_group"
    
    datum_group_id = Column(Integer, primary_key=True)

    datum_types = relationship("DatumType", backref="datum_group")
    group_rules = relationship("FilterRuleGroup", backref="datum_group")


class DatumType(DefinitionMixin, Base):
    """Type of Datum Objects

    Has common functional use and properties (elements)

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
        datum_group_id: (integer, fk, required): DatumGroup
    """

    __tablename__ = "datum_type"

    datum_type_id = Column(Integer, primary_key=True)

    datum_group_id = Column(Integer,
                            ForeignKey('datum_group.datum_group_id'),
                            nullable=False
                            )

    datum_objects = relationship("DatumObject", backref="datum_type")
    element_types = relationship("DatumTypeElement", backref="datum_type")
    type_rules = relationship("FilterRuleType", backref="datum_type")


class DatumObject(DefinitionMixin, Base):
    """Primary personal information data object

    Node/Vertex in graph
    Has Datum Type which defines properties (elements)

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
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


class ElementType(DefinitionMixin, Base):
    """Property types available to Datums

    Has metadata

    Attributes:
        data_type (string): Common string label of data types
        extended_properties (string): Other metadata properties (default, unique, etc.)
    """
    #TODO Entity-Attribute-Value anti-pattern: Metadata in table

    __tablename__ = "element_type"

    element_type_id = Column(Integer, primary_key=True)

    data_type = Column(String(20))
    extended_properties = Column(String(100))

    element_options = relationship("ElementOption", backref="element_type")
    datum_types = relationship("DatumTypeElement", backref="element_type")
    element_values = relationship("ElementValue", backref="element_type")
    element_rules = relationship("FilterRuleElement", backref="element_type")


class ElementOption(DefinitionMixin, Base):
    """Value options for elements

    Example:
        Action Status - New, Someday, Upcoming, etc.

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
        element_type_id (integer, fk): ElementType
        element_option_value (string, required, indexed)
            ***must match element value format
    """
    #TODO Entity-Attribute-Value anti-pattern: Enforce option values

    __tablename__ = "element_option"

    element_option_id = Column(Integer, primary_key=True)

    element_type_id = Column(Integer,
                             ForeignKey("element_type.element_type_id"),
                             nullable=False
                             )
    element_option_value = Column(String, nullable=False, index=True)

    element_values = relationship("ElementValue", backref="element_option")


class DatumTypeElement(Base):
    """Default Element Types assigned to Datum Types

    Used at Datum creation - Added to element_value table

        Attributes:
            datum_type_id (integer, fk, pk): DatumType
            element_type_id (integer, fk, pk): ElementType
    """
    __tablename__ = "datum_type_element"

    datum_type_id = Column(Integer,
                       ForeignKey("datum_type.datum_type_id"),
                       primary_key=True
                       )
    element_type_id = Column(Integer,
                             ForeignKey("element_type.element_type_id"),
                             primary_key=True
                             )


class ElementValue(Base):
    """Element values for Datums

    Attributes:
        datum_object_id (integer, fk, required): DatumObject
        element_type_id (integer, fk, required): ElementType
        element_option_id (integer, fk, nullable): ElementOption
        element_value (string, nullable, indexed): Can be anything
    """

    #TODO Entity-Attribute-Value anti-pattern: Avoid one giant table, manage constraints

    __tablename__ = "element_value"

    element_value_id = Column(Integer, primary_key=True)
    datum_object_id = Column(Integer,
                             ForeignKey("datum_object.datum_object_id"),
                             nullable=False
                             )
    element_type_id = Column(Integer,
                             ForeignKey("element_type.element_type_id"),
                             nullable=False
                             )
    element_option_id = Column(Integer,
                               ForeignKey("element_option.element_option_id"),
                               nullable=True
                               )
    element_value = Column(String, nullable=True, index=True)

    ix_datobj_elmtyp = Index("ix_datum_object_element_type", datum_object_id, element_type_id)


class AssociationType(DefinitionMixin, Base):
    """Types of relationships/edges between Datums

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
    """

    __tablename__ = "association_type"

    association_type_id = Column(Integer, primary_key=True)

    association_objects = relationship("AssociationObject", backref="association_type")
    association_rules = relationship("FilterRuleAssociation", backref="association_type")


class AssociationDirection(DefinitionMixin, Base):
    """Direction of Association from a particular Datum (node)

    Used for filters

    Examples:
        Parent, Child, Both

    Attributes:
        See DefinitionMixin (includes SortActiveMixin)
    """
    __tablename__ = "association_direction"

    association_direction_id = Column(Integer, primary_key=True)


class AssociationObject(Base):
    """Relationship between Datums

    Edge/Link in graph
    Using Closure table pattern
    Stores every path through tree

    Attributes:
        parent_datum_id (integer, pk, fk): DatumObject
        child_datum_id (integer, pk, fk): DatumObject
        depth (integer):  
        association_type_id (integer, fk, required): AssociationType
    """

    __tablename__ = "association_object"

    parent_datum_id = Column(Integer, ForeignKey("datum_object.datum_object_id"), primary_key=True)
    child_datum_id = Column(Integer, ForeignKey("datum_object.datum_object_id"), primary_key=True)
    depth = Column(Integer, default=0)
    association_type_id = Column(Integer,
                                 ForeignKey("association_type.association_type_id"),
                                 nullable=False
                                 )