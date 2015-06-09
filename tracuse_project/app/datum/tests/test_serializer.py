from django.test import TestCase

from .test_data import TestDataDatum

from ..serializers import (DatumGroupSerializer,
                           DatumTypeSerializer,
                           DatumObjectSerializer)


class TestDatumGroupSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_serial_basic(self):
        """Test DatumGroupSerializer.serial_basic
        """
        test_object = self.test.datum_group1
        test_serialized = DatumGroupSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "TestDatumGroup1"
        self.assertEqual(expected, actual)

    def test_serial_datum_types_list(self):
        """Test DatumGroupSerializer.serial_related_list
        """
        test_object = self.test.datum_group1
        test_serialized = DatumGroupSerializer. \
            serial_related_list(test_object)
        actual = test_serialized["entity_name"]
        expected = "TestDatumGroup1"
        self.assertEqual(expected, actual)


class TestDatumTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_serial_basic(self):
        """Test DatumTypeSerializer.serial_basic
        """
        test_object = self.test.datum_type1
        test_serialized = DatumTypeSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "TestDatumType1"
        self.assertEqual(expected, actual)


class TestDatumObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_serial_basic(self):
        """Test DatumObjectSerializer.serial_basic
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer. \
            serial_basic(test_object)
        actual = test_serialized["datum_type_id"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)

    def test_serial_element_name_value(self):
        """Test DatumObjectSerializer.serial_element_name_value
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer.serial_element_name_value(test_object)
        actual = test_serialized["name"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_serial_datum_elements_list(self):
        """Test DatumObjectSerializer.serial_datum_elements_list
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer.serial_datum_elements_list(test_object)

        actual_type = test_serialized["datum_type_id"]
        expected_type = self.test.datum_type1.datum_type_id
        self.assertEqual(expected_type, actual_type)

        expected_element = self.test.element_datum_object1.pk
        actual_elements = test_serialized["elements"]
        self.assertIn(expected_element, actual_elements)

    def test_serial_datum_elements_objects(self):
        """Test DatumObjectSerializer.serial_datum_elements_objects
        """
        test_object = self.test.datum_object1
        test_serialized = DatumObjectSerializer.serial_datum_elements_objects(test_object)

        actual_type = test_serialized["datum_type_id"]
        expected_type = self.test.datum_type1.datum_type_id
        self.assertEqual(expected_type, actual_type)

        expected_element = "Name"
        actual_elements = test_serialized["elements"][0]["element_name"]
        self.assertEqual(expected_element, actual_elements)
