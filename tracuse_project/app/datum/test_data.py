from model_mommy import mommy


class TestDataDatum(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Datum Groups
        self.datum_group1 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup1",
                                       sort=10)
        self.datum_group2 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup2",
                                       sort=20)
        self.datum_group3 = mommy.make("datum.DatumGroup",
                                       entity_name="TestDatumGroup3",
                                       sort=30)

        # Datum Types
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType1",
                                      datum_group=self.datum_group1,
                                      str_expression="{{name}}",
                                      sort=10100)
        # Calculate sort
        self.datum_type2 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType2",
                                      datum_group=self.datum_group1,
                                      str_expression="{{name}}")
        # Calculate sort in new group
        self.datum_type3 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType3",
                                      datum_group=self.datum_group2,
                                      str_expression="{{name}}")

        # Datum Object
        # Has element_type and element_value
        self.datum_object1 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)
        # Has element_type, but no element_value
        self.datum_object2 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)
        # Does not have element_type, or element_value
        self.datum_object3 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)


        # Element Data Type & Element Types
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
        self.element_type3 = mommy.make("element_type.ElementType",
                                        entity_name="Description",
                                        element_data_type=self.element_data_type1
                                        )

        # Element Options
        self.element_option1 = mommy.make("element_type.ElementOption",
                                          entity_name="Option1",
                                          element_type=self.element_type1
                                          )

        # Element Type - Datum Type
        # Test for entity name
        self.element_datum_type1 = mommy.make("element_type.ElementDatumType",
                                              make_m2m=True,
                                              datum_type=self.datum_type1,
                                              element_type=self.element_type1
                                              )
        self.element_datum_type2 = mommy.make("element_type.ElementDatumType",
                                              make_m2m=True,
                                              datum_type=self.datum_type1,
                                              element_type=self.element_type2,
                                              entity_name="TestType2Description"
                                              )


        # Element Type - Datum Object
        self.element_datum_object1 = mommy.make("element_type.ElementDatumObject",
                                                make_m2m=True,
                                                datum_object=self.datum_object1,
                                                element_type=self.element_type1
                                                )
        self.element_datum_object2 = mommy.make("element_type.ElementDatumObject",
                                                make_m2m=True,
                                                datum_object=self.datum_object1,
                                                element_type=self.element_type2
                                                )

        # Element Value objects
        self.element_value_string1 = \
            mommy.make("element_value.ElementValueString",
                       element_datum_object=self.element_datum_object1,
                       elvalue="Test Object Name")
        self.element_value_string2 = \
            mommy.make("element_value.ElementValueString",
                       element_datum_object=self.element_datum_object2,
                       elvalue="Test Object Description")
