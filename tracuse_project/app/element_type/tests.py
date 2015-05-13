from django.test import TestCase

from app.datum.test_data import TestDataDatum


class TestModelElementDatumType(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_str(self):
        """Test ElementDatumType.__str__ property"""
        actual = self.test.element_datum_type1.__str__()
        expected = "Test Datum Type1 - Name"
        self.assertEqual(expected, actual)


class TestModelElementDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_str(self):
        """Test ElementDatumObject.__str__ property"""
        actual = self.test.element_datum_object1.__str__()
        expected = "Test Object Name - Name"
        self.assertEqual(expected, actual)
