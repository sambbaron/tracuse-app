from model_mommy import mommy


class TestDataSimple(object):
    def __init__(self):
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

        # Mock Datum Types
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType",
                                      datum_group=self.datum_group1,
                                      repr_expression = "{{name}}",
                                      sort=10100)
        # Calculate sort
        self.datum_type2 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType",
                                      datum_group=self.datum_group1,
                                      repr_expression = "{{name}}")

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

        # Mock Element Type objects
        self.element_data_type1 = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.element_type1 = mommy.make("element_type.ElementType",
                                        entity_name="Name",
                                        element_data_type=self.element_data_type1)
        self.element_type2 = mommy.make("element_type.ElementType",
                                        entity_name="Description",
                                        element_data_type=self.element_data_type1)

        # Mock many-to-many relationships between Datum and Element Type objects
        self.element_type_datum_type1 = mommy.make("element_type.ElementTypeDatumType",
                                                   make_m2m=True,
                                                   element_type=self.element_type1,
                                                   datum_type=self.datum_type1
                                                   )
        self.element_type_datum_object1 = mommy.make("element_type.ElementTypeDatumObject",
                                                     make_m2m=True,
                                                     element_type=self.element_type1,
                                                     datum_object=self.datum_object1
                                                     )
        self.element_type_datum_object2 = mommy.make("element_type.ElementTypeDatumObject",
                                                     make_m2m=True,
                                                     element_type=self.element_type1,
                                                     datum_object=self.datum_object2
                                                     )

        # Mock Element Value objects
        self.element_value_string1 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object1,
                                                element_value="Test Object Name")

