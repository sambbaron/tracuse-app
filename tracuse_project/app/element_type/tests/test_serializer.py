from django.test import TestCase

from .test_data import TestDataElement

from ..serializers import (ElementTypeSerializer,
                           ElementOperatorSerializer,
                           ElementDatumTypeSerializer,
                           ElementDatumObjectSerializer)


class TestElementTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_basic(self):
        """Test ElementTypeSerializer.serial_basic
        """
        test_object = self.test.element_type1
        test_serialized = ElementTypeSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "Name"
        self.assertEqual(expected, actual)


class TestElementOperatorSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_basic(self):
        """Test ElementTypeSerializer.serial_basic
        """
        test_object = self.test.element_operator1
        test_serialized = ElementOperatorSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "exact"
        self.assertEqual(expected, actual)


class TestElementDatumTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_basic(self):
        """Test ElementDatumTypeSerializer.serial_basic
        """
        test_object = self.test.element_datum_type1
        test_serialized = ElementDatumTypeSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "TestDatumType1Name"
        self.assertEqual(expected, actual)


class TestElementDatumObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_ids_value(self):
        """Test ElementDatumObjectSerializer.serial_ids_value
        """
        test_object = self.test.element_datum_object1
        test_serialized = ElementDatumObjectSerializer. \
            serial_ids_value(test_object)
        actual = test_serialized["element_value"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)
