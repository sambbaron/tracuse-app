from model_mommy import mommy

from app.datum.models import DatumGroup, DatumType, DatumObject
from app.association.models import AssociationDirection
from app.element_type.models import ElementType
from .. import models as filters


class TestFilterSets(object):
    def __init__(self):
        self.filter_set1 = {
            "group_rules": [
                filters.FilterRuleGroup(
                    datum_group=DatumGroup.objects.get(entity_name="Area"),
                ),
                filters.FilterRuleGroup(
                    conditional="OR",
                    datum_group=DatumGroup.objects.get(entity_name="Activity"),
                ),
            ],
            "type_rules": [
                filters.FilterRuleType(
                    datum_type=DatumType.objects.get(entity_name="Category"),
                ),
                filters.FilterRuleType(
                    conditional="OR",
                    datum_type=DatumType.objects.get(entity_name="Action"),
                ),
            ],
            "association_rules": [
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
            "element_rules": [
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
