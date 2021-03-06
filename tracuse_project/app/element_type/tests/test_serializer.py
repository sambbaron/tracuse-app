from django.test import TestCase

from .test_data import TestDataElement

from ..serializers import (ElementTypeSerializer,
                           ElementOperatorSerializer,
                           ElementDatumTypeSerializer,
                           ElementDatumObjectSerializer,
                           ElementOptionSerializer,
                           ElementDataTypeSerializer)


class TestElementTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementTypeSerializer.serial_default
        """
        test_object = self.test.element_type1
        test_serialized = ElementTypeSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Name"
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test ElementTypeSerializer.serial_related
        """
        test_object = self.test.element_type1
        test_serialized = ElementTypeSerializer \
            ("serial_related").serialize(test_object)
        actual = test_serialized["element_operators"]
        expected = [self.test.element_operator1.element_operator_id,
                    self.test.element_operator2.element_operator_id
                    ]
        self.assertEqual(set(expected), set(actual))


class TestElementOperatorSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementTypeSerializer.serial_default
        """
        test_object = self.test.element_operator1
        test_serialized = ElementOperatorSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "exact"
        self.assertEqual(expected, actual)


class TestElementDatumTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementDatumTypeSerializer.serial_default
        """
        test_object = self.test.element_datum_type1
        test_serialized = ElementDatumTypeSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "TestDatumType1Name"
        self.assertEqual(expected, actual)


class TestElementDatumObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementDatumObjectSerializer.serial_default
        """
        test_object = self.test.element_datum_object1
        test_serialized = ElementDatumObjectSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["element_value"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test ElementDatumObjectSerializer.serial_related
        """
        test_object = self.test.element_datum_object1
        test_serialized = ElementDatumObjectSerializer \
            ("serial_related").serialize(test_object)
        actual = test_serialized["element_value"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)


class TestElementOptionSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementOptionSerializer.serial_default
        """
        test_object = self.test.element_option1
        test_serialized = ElementOptionSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Option1"
        self.assertEqual(expected, actual)


class TestElementDataTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_serial_default(self):
        """Test ElementDataTypeSerializer.serial_default
        """
        test_object = self.test.element_data_type1
        test_serialized = ElementDataTypeSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "String"
        self.assertEqual(expected, actual)
