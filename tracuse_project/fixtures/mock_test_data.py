from model_mommy import mommy
from mock_django.managers import QuerySetMock

from components.datum.models import DatumGroup, DatumObject


class TestDataDatumElement(object):
    """Simple mock datum and element objects for testing"""

    def __init__(self):
        # Mock User
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Mock Datum Groups
        self.datum_group1 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup1",
                                       sort=10)
        self.datum_group2 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup2",
                                       sort=20)
        self.datum_group3 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup3",
                                       sort=30)

        self.datum_groups_all = [self.datum_group1,
                                 self.datum_group2,
                                 self.datum_group3,
                                 ]
        self.datum_group_qs = QuerySetMock(DatumGroup, *self.datum_groups_all)


        # Mock Datum Types
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType1",
                                      datum_group=self.datum_group1,
                                      repr_expression="{{name}}",
                                      sort=10100)
        # Calculate sort
        self.datum_type2 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType2",
                                      datum_group=self.datum_group1,
                                      repr_expression="{{name}}")
        # Calculate sort in new group
        self.datum_type3 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType3",
                                      datum_group=self.datum_group2,
                                      repr_expression="{{name}}")

        # Mock Datum Objects
        # Has element_type and element_value
        self.datum_object1 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)
        # Has element_type, but no element_value
        self.datum_object2 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)
        # Does not have element_type, or element_value
        self.datum_object3 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)

        # Mock Element Types
        self.element_data_type1 = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.element_type1 = mommy.make("element_type.ElementType",
                                        entity_name="Name",
                                        element_data_type=self.element_data_type1,
                                        sort=100)
        self.element_type2 = mommy.make("element_type.ElementType",
                                        entity_name="Description",
                                        element_data_type=self.element_data_type1,
                                        sort=110)

        # Mock Element Type - Datum Type
        self.element_type_datum_type1 = mommy.make("element_type.ElementTypeDatumType",
                                                   make_m2m=True,
                                                   datum_type=self.datum_type1,
                                                   element_type=self.element_type1
                                                   )
        self.element_type_datum_type2 = mommy.make("element_type.ElementTypeDatumType",
                                                   make_m2m=True,
                                                   datum_type=self.datum_type1,
                                                   element_type=self.element_type2
                                                   )

        # Mock Element Type - Datum Object
        self.element_type_datum_object1 = mommy.make("element_type.ElementTypeDatumObject",
                                                     make_m2m=True,
                                                     datum_object=self.datum_object1,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object2 = mommy.make("element_type.ElementTypeDatumObject",
                                                     make_m2m=True,
                                                     datum_object=self.datum_object2,
                                                     element_type=self.element_type1
                                                     )

        # Mock Element Value objects
        self.element_value_string1 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object1,
                                                element_value="Test Object Name")


class TestDataAssociation(object):
    """Datum Objects for testing associations"""

    def __init__(self):

        # Mock Datum Type
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType1",
                                      repr_expression="{{name}}"
                                      )
        # Mock Datum Objects
        self.datum_object1 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object2 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object3 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object4 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object5 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object6 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)

        # Mock Element Type for Name Identification
        self.element_data_type1 = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.element_type1 = mommy.make("element_type.ElementType",
                                        entity_name="Name",
                                        element_data_type=self.element_data_type1
                                        )

        # Assign Element Types to Datum Objects
        self.element_type_datum_object1 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object1,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object2 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object2,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object3 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object3,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object4 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object4,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object5 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object5,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object6 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object6,
                                                     element_type=self.element_type1
                                                     )

        # Mock Element Value objects
        self.element_value_string1 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object1,
                                                element_value="Test Object1")
        self.element_value_string2 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object2,
                                                element_value="Test Object2")
        self.element_value_string3 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object3,
                                                element_value="Test Object3")
        self.element_value_string4 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object4,
                                                element_value="Test Object4")
        self.element_value_string5 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object5,
                                                element_value="Test Object5")
        self.element_value_string6 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object6,
                                                element_value="Test Object6")


        # Adjacent Associations
        self.adjacent_association1 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object1,
                                                child_datum=self.datum_object2
                                                )
        self.adjacent_association2 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object2,
                                                child_datum=self.datum_object3
                                                )
        self.adjacent_association3 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object1,
                                                child_datum=self.datum_object3
                                                )

