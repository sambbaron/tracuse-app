from django.test import TestCase

from fixtures.test_data_simple import TestDataSimple


class TestModelElementTypeDatumType(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def test_str(self):
        """Test ElementTypeDatumType.__str__ property"""
        actual = self.test.element_type_datum_type1.__str__()
        expected = "Test Datum Type - Name"
        self.assertEqual(expected, actual)


class TestModelElementTypeDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def test_str(self):
        """Test ElementTypeDatumObject.__str__ property"""
        actual = self.test.element_type_datum_object1.__str__()
        expected = "Test Object Name - Name"
        self.assertEqual(expected, actual)
