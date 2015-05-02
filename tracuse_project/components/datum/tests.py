from django.test import TestCase

from model_mommy import mommy

from .models import DatumGroup, DatumType, DatumObject


class TestModelDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Mock Datum objects
        cls.datum_group1 = mommy.make("datum.DatumGroup",
                                      entity_name="TestGroup")
        cls.datum_type1 = mommy.make("datum.DatumType",
                                     entity_name="TestType",
                                     datum_group=cls.datum_group1)
        cls.datum_object1 = mommy.make("datum.DatumObject",
                                       datum_type=cls.datum_type1)

        # Mock Element Type objects
        cls.element_data_type1 = mommy.make("element_type.ElementDataType",
                                           entity_name="String"
                                           )
        cls.element_type1 = mommy.make("element_type.ElementType",
                                       entity_name="TestElementType1",
                                       element_data_type=cls.element_data_type1)
        cls.element_type2 = mommy.make("element_type.ElementType",
                                       entity_name="TestElementType2",
                                       element_data_type=cls.element_data_type1)

        # Mock many-to-many relationships between Datum and Element Type objects
        cls.element_type_datum_type1 = mommy.make("element_type.ElementTypeDatumType",
                                                make_m2m=True,
                                                element_type = cls.element_type1,
                                                datum_type = cls.datum_type1
                                                )
        cls.element_type_datum_object1 = mommy.make("element_type.ElementTypeDatumObject",
                                                make_m2m=True,
                                                element_type = cls.element_type1,
                                                datum_object = cls.datum_object1
                                                )

        # Mock Element Value objects
        cls.element_value_string1 = mommy.make("element_value.ElementValueString",
                                               element_type_datum_object=cls.element_type_datum_object1,
                                               element_value="Test Object Name")


    def tearDown(self):
        pass

    def test_datum_group(self):
        """Test DatumObject.datum_group property"""
        actual = self.datum_object1.datum_group
        expected = self.datum_group1
        self.assertEqual(expected, actual)
