from model_mommy import mommy


class TestDataSimple(object):
    def __init__(self):
        # Mock Datum objects
        self.datum_group1 = mommy.make("datum.DatumGroup",
                                       entity_name="TestGroup")
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestType",
                                      datum_group=self.datum_group1)
        self.datum_object1 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)

        # Mock Element Type objects
        self.element_data_type1 = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.element_type1 = mommy.make("element_type.ElementType",
                                        entity_name="TestElementType1",
                                        element_data_type=self.element_data_type1)
        self.element_type2 = mommy.make("element_type.ElementType",
                                        entity_name="TestElementType2",
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

        # Mock Element Value objects
        self.element_value_string1 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object1,
                                                element_value="Test Object Name")

