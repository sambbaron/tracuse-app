from model_mommy import mommy

from django.contrib.auth.models import User

from app.datum.models import DatumGroup, DatumType, DatumObject
from app.association.models import AssociationDirection
from app.element_type.models import ElementType, ElementDataType
from .. import models as filters


class TestFilterSetsModel(object):
    def __init__(self):
        self.filter_set_user1 = {
            "FilterRuleUser": [
                filters.FilterRuleUser(
                    user=User.objects.get(pk=1),
                ),
            ],
        }

        self.filter_set_group1 = {
            "FilterRuleGroup": [
                filters.FilterRuleGroup(
                    datum_group=DatumGroup.objects.get(entity_name="Area"),
                ),
            ],
        }

        self.filter_set_group2 = {
            "FilterRuleGroup": [
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
            "FilterRuleType": [
                filters.FilterRuleType(
                    datum_type=DatumType.objects.get(entity_name="Context"),
                ),
            ],
        }

        self.filter_set_type2 = {
            "FilterRuleType": [
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
            "FilterRuleAssociation": [
                filters.FilterRuleAssociation(
                    datum_object=DatumObject.objects.get(pk=3),
                    association_direction=AssociationDirection.child(),
                    distance=None
                ),
            ],
        }

        self.filter_set_association2 = {
            "FilterRuleAssociation": [
                filters.FilterRuleAssociation(
                    datum_object=DatumObject.objects.get(pk=14),
                    association_direction=AssociationDirection.parent(),
                    distance=2
                ),
            ],
        }

        self.filter_set_element1 = {
            "FilterRuleElement": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="Name"),
                    operator="icontains",
                    element_value="pdx code guild",
                ),
            ],
        }

        self.filter_set_element2 = {
            "FilterRuleElement": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="ActionEffort"),
                    operator="exact",
                    element_value="4",
                ),
            ],
        }

        self.filter_set_element3 = {
            "FilterRuleElement": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="ActionEffort"),
                    operator="exact",
                    element_value="3",
                ),
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="Description"),
                    operator="icontains",
                    element_value="craigs",
                ),
            ],
        }

        self.filter_set_data_type1 = {
            "FilterRuleDataType": [
                filters.FilterRuleDataType(
                    element_data_type=ElementDataType.objects.get(entity_name="String"),
                    operator="icontains",
                    element_value="apartment",
                ),
            ],
        }

        self.filter_set1 = mommy.make("filter.FilterSet")
        self.filter_rule_group1 = mommy.make("filter.FilterRuleGroup",
                                             datum_group=DatumGroup.objects.get(entity_name="Area")
                                             )
        self.filter_set_group_rule1 = mommy.make("filter.FilterSetGroupRule",
                                                 filter_set=self.filter_set1,
                                                 filter_rule_group=self.filter_rule_group1
                                                 )

        self.filter_set_dict1 = {

            "FilterRuleType": [
                dict(
                    datum_type_id=DatumType.objects.get(entity_name="Action").pk,
                ),
                dict(
                    conditional="OR",
                    datum_type_id=DatumType.objects.get(entity_name="Event").pk,
                ),
            ],

            "FilterRuleAssociation": [
                dict(
                    datum_object_id=10,
                    association_direction_id=AssociationDirection.both().pk,
                    distance=None
                ),
            ],

            "FilterRuleElement": [
                dict(
                    element_type_id=ElementType.objects.get(entity_name="ActionEffort").pk,
                    operator="gte",
                    element_value="1",
                ),
                dict(
                    conditional="AND",
                    element_type_id=ElementType.objects.get(entity_name="ActionStatus").pk,
                    operator="iexact",
                    element_value="Upcoming",
                ),
                dict(
                    conditional="OR",
                    element_type_id=ElementType.objects.get(entity_name="ActionStatus").pk,
                    operator="iexact",
                    element_value="Current",
                ),
            ],
        }
