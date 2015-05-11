from django.test import TestCase

from components.datum.test_data import TestDataDatum


class TestModelElementTypeDatumType(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_str(self):
        """Test ElementTypeDatumType.__str__ property"""
        actual = self.test.element_type_datum_type1.__str__()
        expected = "Test Datum Type1 - Name"
        self.assertEqual(expected, actual)


class TestModelElementTypeDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_str(self):
        """Test ElementTypeDatumObject.__str__ property"""
        actual = self.test.element_type_datum_object1.__str__()
        expected = "Test Object Name - Name"
        self.assertEqual(expected, actual)
