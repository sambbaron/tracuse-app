from model_mommy import mommy

from django.contrib.auth.models import User

from app.datum.models import DatumGroup, DatumType, DatumObject
from app.association.models import AssociationDirection
from app.element_type.models import ElementType
from .. import models as filters


class TestFilterSets(object):

    def __init__(self):

        self.filter_set_user1 = {
            "filter_set_user_rules": [
                filters.FilterRuleUser(
                    user=User.objects.get(pk=1),
                ),
            ],
        }

        self.filter_set_group1 = {
            "filter_set_group_rules": [
                filters.FilterRuleGroup(
                    datum_group=DatumGroup.objects.get(entity_name="Area"),
                ),
            ],
        }

        self.filter_set_group2 = {
            "filter_set_group_rules": [
                filters.FilterRuleGroup(
                    datum_group=DatumGroup.objects.get(entity_name="Activity"),
                ),
                filters.FilterRuleGroup(
                    conditional="OR",
                    datum_group=DatumGroup.objects.get(entity_name="Item"),
                ),
            ],
        }

        self.filter_set_type1 = {
            "filter_set_type_rules": [
                filters.FilterRuleType(
                    datum_type=DatumType.objects.get(entity_name="Context"),
                ),
            ],
        }
        
        self.filter_set_type2 = {
            "filter_set_type_rules": [
                filters.FilterRuleType(
                    datum_type=DatumType.objects.get(entity_name="Category"),
                ),
                filters.FilterRuleType(
                    conditional="AND",
                    datum_type=DatumType.objects.get(entity_name="Event"),
                ),
            ],
        }

        self.filter_set_association1 = {
            "filter_set_association_rules": [
                filters.FilterRuleAssociation(
                    datum_object=DatumObject.objects.get(pk=3),
                    association_direction=AssociationDirection.child(),
                    distance=None
                ),
            ],
        }

        self.filter_set_association2 = {
            "filter_set_association_rules": [
                filters.FilterRuleAssociation(
                    datum_object=DatumObject.objects.get(pk=14),
                    association_direction=AssociationDirection.parent(),
                    distance=2
                ),
            ],
        }

        self.filter_set_element1 = {
            "filter_set_element_rules": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="Name"),
                    operator="icontains",
                    elvalue="pdx code guild",
                ),
            ],
        }

        self.filter_set_element2 = {
            "filter_set_element_rules": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="ActionEffort"),
                    operator="exact",
                    elvalue="4",
                ),
            ],
        }

        self.filter_set_element3 = {
            "filter_set_element_rules": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="ActionEffort"),
                    operator="exact",
                    elvalue="3",
                ),
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="Description"),
                    operator="icontains",
                    elvalue="craigs",
                ),
            ],
        }