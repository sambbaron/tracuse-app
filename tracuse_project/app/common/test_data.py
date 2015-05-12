from model_mommy import mommy


class TestDataCommon(object):

    def __init__(self):

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
        self.datum_object1 = mommy.make("datum.DatumObject",
                                        datum_type=self.datum_type1)
