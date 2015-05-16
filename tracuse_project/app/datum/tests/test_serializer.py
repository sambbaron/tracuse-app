from django.test import TestCase

from .test_data import TestDataDatum

from ..serializers import DatumObjectSerializer


class TestDatumObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()


    def test_element_name_value(self):
        """Test DatumObjectSerializer.serial_element_name_value
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer.serial_element_name_value(test_object)
        actual = test_serialized["name"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)


    def test_datum_all(self):
        """Test DatumObjectSerializer.serial_datum_all
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer.serial_datum_all(test_object)
        actual = test_serialized["datum_type"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)

