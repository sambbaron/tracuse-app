from django.test import TestCase

from .test_data import TestDataUiObject

from ..serializers import UiArrangementTypeSerializer, UiFormattingTypeSerializer


class TestUiArrangementTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataUiObject()

    def test_serial_default(self):
        """Test UiArrangementTypeSerializer.serial_default
        """
        test_object = self.test.ui_arrangement_type1
        test_serialized = UiArrangementTypeSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "ArrangementType1"
        self.assertEqual(expected, actual)


class TestUiFormattingTypeSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataUiObject()

    def test_serial_default(self):
        """Test UiFormattingTypeSerializer.serial_default
        """
        test_object = self.test.ui_formatting_type1
        test_serialized = UiFormattingTypeSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "FormattingType1"
        self.assertEqual(expected, actual)
