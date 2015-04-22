"""SQLAlchemy Models for Datum Filter-related entities"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey, Integer, String, SmallInteger, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr

from databases.postgres import Base
from models.base import SortActiveMixin


class FilterSet(SortActiveMixin, Base):
    """Datum filter with multiple rules

    Attributes:
        See SortActiveMixin
        user_id (integer, fk, nullable): User
        name (string, required):
        description (string): 
    """
    __tablename__ = "filter_set"

    filter_set_id = Column(Integer, primary_key=True)
    # Null user means filter set available to all users??
    user_id = Column(Integer,
                     ForeignKey("user.user_id"),
                     nullable=True
                     )
    name = Column(String(25), unique=True, nullable=False, index=True)
    description = Column(String(100))

    group_rules = relationship("FilterSetGroupRule", backref="filter_set")
    type_rules = relationship("FilterSetTypeRule", backref="filter_set")
    association_rules = relationship("FilterSetAssociationRule", backref="filter_set")
    element_rules = relationship("FilterSetElementRule", backref="filter_set")


class FilterSetRuleMixin(SortActiveMixin):
    """Common properties for assigning Filter Rules to Filter Sets

    Includes rule ordering

    Attributes:
        See SortActiveMixin
        filter_set_id (integer, fk, required): FilterSet
    """

    @declared_attr
    def filter_set_id(self):
        return Column(Integer,
                      ForeignKey("filter_set.filter_set_id"),
                      nullable=False
                      )


class FilterSetGroupRule(FilterSetRuleMixin, Base):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes SortActiveMixin)
        group_rule_id (integer, fk, required): FilterRuleGroup
    """
    __tablename__ = "filter_set_group_rule"
    
    filter_set_group_rule_id = Column(Integer, primary_key=True)
    group_rule_id = Column(Integer,
                           ForeignKey("filter_rule_group.group_rule_id"),
                           nullable=False
                           )


class FilterSetTypeRule(FilterSetRuleMixin, Base):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes SortActiveMixin)
        type_rule_id (integer, fk, required): FilterRuleType
    """
    __tablename__ = "filter_set_type_rule"

    filter_set_type_rule_id = Column(Integer, primary_key=True)
    type_rule_id = Column(Integer,
                          ForeignKey("filter_rule_type.type_rule_id"),
                          nullable=False
                          )


class FilterSetAssociationRule(FilterSetRuleMixin, Base):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes SortActiveMixin)
        association_rule_id (integer, fk, required): FilterRuleAssociation
    """
    __tablename__ = "filter_set_association_rule"

    filter_set_association_rule_id = Column(Integer, primary_key=True)
    association_rule_id = Column(Integer,
                                 ForeignKey("filter_rule_association.association_rule_id"),
                                 nullable=False
                                 )


class FilterSetElementRule(FilterSetRuleMixin, Base):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin (includes SortActiveMixin)
        element_rule_id (integer, fk, required): FilterRuleElement
    """
    __tablename__ = "filter_set_element_rule"

    filter_set_element_rule_id = Column(Integer, primary_key=True)
    element_rule_id = Column(Integer,
                             ForeignKey("filter_rule_element.element_rule_id"),
                             nullable=False
                             )


class FilterRuleMixin(SortActiveMixin):
    """Common properties for Filter Rules

    Attributes:
        See SortActiveMixin
        operator (string, required):  -> = <> => <=
        conditional (string, nullable): And, Or
    """

    operator = Column(String(5), default="=")
    conditional = Column(String(3), nullable=True)


class FilterRuleGroup(FilterRuleMixin, Base):
    """Filter Rules by Datum Group

    Attributes:
        See FilterRuleMixin (includes SortActiveMixin)
        datum_group_id (integer, fk, required): DatumGroup
    """
    __tablename__ = "filter_rule_group"

    group_rule_id = Column(Integer, primary_key=True)
    datum_group_id = Column(Integer,
                            ForeignKey("datum_group.datum_group_id"),
                            nullable=False
                            )


class FilterRuleType(FilterRuleMixin, Base):
    """Filter Rules by Datum Type

    Attributes:
        See FilterRuleMixin (includes SortActiveMixin)
        datum_type_id (integer, fk, required): DatumGroup
    """
    __tablename__ = "filter_rule_type"

    type_rule_id = Column(Integer, primary_key=True)
    datum_type_id = Column(Integer,
                           ForeignKey("datum_type.datum_type_id"),
                           nullable=False
                           )


class FilterRuleAssociation(FilterRuleMixin, Base):
    """Filter Rules by Datum Association

    Attributes:
        See FilterRuleMixin (includes SortActiveMixin)
        datum_object_id (integer, fk, required): DatumObject
        association_direction_id (integer, fk, required): AssociationDirection
        association_type_id (integer, fk, required): AssociationType
        depth (integer, required):
    """
    __tablename__ = "filter_rule_association"
    
    association_rule_id = Column(Integer, primary_key=True)
    datum_object_id = Column(Integer,
                             ForeignKey("datum_object.datum_object_id"),
                             nullable=False
                             )
    association_direction_id = Column(Integer,
                                 ForeignKey("association_direction.association_direction_id"),
                                 nullable=False
                                 )
    association_type_id = Column(Integer,
                                 ForeignKey("association_type.association_type_id"),
                                 nullable=False
                                 )
    depth = Column(Integer, default=1, nullable=False)


class FilterRuleElement(FilterRuleMixin, Base):
    """Filter Rules by Element Value

    Attributes:
        See FilterRuleMixin (includes SortActiveMixin)
        element_type_id (integer, fk, required): ElementType
        element_value (string):  ***Must match value string
    """
    __tablename__ = "filter_rule_element"

    element_rule_id = Column(Integer, primary_key=True)
    element_type_id = Column(Integer,
                             ForeignKey("element_type.element_type_id"),
                             nullable=False
                             )
    element_value = Column(String)