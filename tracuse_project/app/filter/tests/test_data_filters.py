from model_mommy import mommy

from django.contrib.auth.models import User

from app.datum.models import DatumGroup, DatumType, DatumObject
from app.association.models import AssociationDirection
from app.element_type.models import ElementType
from .. import models as filters


class TestFilterSets(object):
    def __init__(self):
        self.filter_set1 = {
            "filter_set_user_rules": [
                filters.FilterRuleUser(
                    user=User.objects.get(pk=1),
                ),
            ],
            "filter_set_group_rules": [
                filters.FilterRuleGroup(
                    datum_group=DatumGroup.objects.get(entity_name="Area"),
                ),
                filters.FilterRuleGroup(
                    conditional="OR",
                    datum_group=DatumGroup.objects.get(entity_name="Activity"),
                ),
            ],
            "filter_set_type_rules": [
                filters.FilterRuleType(
                    datum_type=DatumType.objects.get(entity_name="Category"),
                ),
                filters.FilterRuleType(
                    conditional="OR",
                    datum_type=DatumType.objects.get(entity_name="Action"),
                ),
            ],
            "filter_set_association_rules": [
                filters.FilterRuleAssociation(
                    datum_object=DatumObject.objects.get(pk=3),
                    association_direction=AssociationDirection.both()
                ),
                filters.FilterRuleAssociation(
                    conditional="OR",
                    datum_object=DatumObject.objects.get(pk=10),
                    association_direction=AssociationDirection.both(),
                ),
            ],
            "filter_set_element_rules": [
                filters.FilterRuleElement(
                    element_type=ElementType.objects.get(entity_name="Name"),
                    operator="icontains",
                    elvalue="pyth",
                ),
                filters.FilterRuleElement(
                    conditional="OR",
                    element_type=ElementType.objects.get(entity_name="Description"),
                    operator="icontains",
                    elvalue="apart",
                ),
            ],

        }
