"""SQLAlchemy Models for Datum Filter-related entities"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey, Integer, String, SmallInteger, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr

from databases.postgres import Base


class FilterSet(Base):
    """Datum filter with multiple rules

    Attributes:
        user_id (integer, fk, nullable): User
        name (string, required):
        description (string): 
        sort (integer):
        active (boolean, indexed):
    """
    __tablename__ = "filter_set"

    filter_set_id = Column(Integer, primary_key=True)
    # Null user means filter set available to all users??
    user_id = Column(Integer,
                     ForeignKey("user.user_id"),
                     nullable=True
                     )
    sort = Column(Integer, default=0)
    name = Column(String(25), unique=True, nullable=False, index=True)
    description = Column(String(100))
    active = Column(Boolean, default=True, index=True)

    group_rules = relationship("FilterSetGroupRule", backref="filter_rule_group")
    type_rules = relationship("FilterSetGroupRule", backref="filter_rule_type")
    association_rules = relationship("FilterSetGroupRule", backref="filter_rule_association")
    element_rules = relationship("FilterSetGroupRule", backref="filter_rule_element")


class FilterSetRuleMixin(object):
    """Common properties for assigning Filter Rules to Filter Sets

    Includes rule ordering

    Attributes:
        filter_set_id (integer, fk, required): FilterSet
        sort (integer):
        active (boolean, indexed):
    """

    @declared_attr
    def filter_set_id(self):
        return Column(Integer,
                      ForeignKey("filter_set.filter_set_id"),
                      nullable=False
                      )

    sort = Column(Integer, default=0)
    active = Column(Boolean, default=True, index=True)


class FilterSetGroupRule(Base, FilterSetRuleMixin):
    """Assign Group Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin
        group_rule_id (integer, fk, required): FilterRuleGroup
    """
    __tablename__ = "filter_set_group_rule"
    
    filter_set_group_rule_id = Column(Integer, primary_key=True)
    group_rule_id = Column(Integer,
                           ForeignKey("filter_rule_group.group_rule_id"),
                           nullable=False
                           )


class FilterSetTypeRule(Base, FilterSetRuleMixin):
    """Assign Type Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin
        type_rule_id (integer, fk, required): FilterRuleType
    """
    __tablename__ = "filter_set_type_rule"

    filter_set_type_rule_id = Column(Integer, primary_key=True)
    type_rule_id = Column(Integer,
                          ForeignKey("filter_rule_type.type_rule_id"),
                          nullable=False
                          )


class FilterSetAssociationRule(Base, FilterSetRuleMixin):
    """Assign Association Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin
        association_rule_id (integer, fk, required): FilterRuleAssociation
    """
    __tablename__ = "filter_set_association_rule"

    filter_set_association_rule_id = Column(Integer, primary_key=True)
    association_rule_id = Column(Integer,
                                 ForeignKey("filter_rule_association.association_rule_id"),
                                 nullable=False
                                 )


class FilterSetElementRule(Base, FilterSetRuleMixin):
    """Assign Element Filter Rules to Filter Sets

    Attributes:
        See FilterSetRuleMixin
        element_rule_id (integer, fk, required): FilterRuleElement
    """
    __tablename__ = "filter_set_element_rule"

    filter_set_element_rule_id = Column(Integer, primary_key=True)
    element_rule_id = Column(Integer,
                             ForeignKey("filter_rule_element.element_rule_id"),
                             nullable=False
                             )


class FilterRuleMixin(object):
    """Common properties for Filter Rules

    Attributes:
        sort (integer): 
        operator (string, required):  -> = <> => <=
        conditional (string, nullable): And, Or
        active (boolean, indexed):
    """

    sort = Column(Integer, default=0)
    operator = Column(String(5), default="=")
    conditional = Column(String(3), nullable=True)
    active = Column(Boolean, default=True, index=True)


class FilterRuleGroup(Base, FilterRuleMixin):
    """Filter Rules by Datum Group

    Attributes:
        See FilterRuleMixin
        datum_group_id (integer, fk): DatumGroup
    """
    __tablename__ = "filter_rule_group"

    group_rule_id = Column(Integer, primary_key=True)
    datum_group_id = Column(Integer, ForeignKey("datum_group.datum_group_id"))

    filter_sets = relationship("FilterSetGroupRule", "filter_rule_group")


class FilterRuleType(Base, FilterRuleMixin):
    """Filter Rules by Datum Type

    Attributes:
        See FilterRuleMixin
        datum_type_id (integer, fk): DatumGroup
    """
    __tablename__ = "filter_rule_type"

    type_rule_id = Column(Integer, primary_key=True)
    datum_type_id = Column(Integer, ForeignKey("datum_type.datum_type_id"))

    filter_sets = relationship("FilterSetTypeRule", "filter_rule_type")


class FilterRuleAssociation(Base, FilterRuleMixin):
    """Filter Rules by Datum Association

    Attributes:
        See FilterRuleMixin
        datum_object_id (integer, fk): DatumObject
        direction (integer): -1: Parent, 1: Child, 0: Bidirectional
        association_type_id (integer, fk): AssociationType
        depth (integer): 
    """
    __tablename__ = "filter_rule_association"
    
    association_rule_id = Column(Integer, primary_key=True)
    datum_object_id = Column(Integer, ForeignKey("datum_object.datum_object_id"))
    direction = Column(SmallInteger)
    association_type_id = Column(Integer, ForeignKey("association_type.association_type_id"))
    depth = Column(Integer)  #TODO Set default depth

    filter_sets = relationship("FilterSetAssociationRule", "filter_rule_association")


class FilterRuleElement(Base, FilterRuleMixin):
    """Filter Rules by Element Value

    Attributes:
        See FilterRuleMixin
        element_type_id (integer, fk): ElementType
        element_value (string):  ***Must match value string
    """
    __tablename__ = "filter_rule_element"

    element_rule_id = Column(Integer, primary_key=True)
    element_type_id = Column(Integer, ForeignKey("element_type.element_type_id"))
    element_value = Column(String)

    filter_sets = relationship("FilterSetElementRule", "filter_rule_element")