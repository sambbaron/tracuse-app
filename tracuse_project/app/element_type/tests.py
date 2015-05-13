from django.test import TestCase, mock

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
        
    def test_entity_name_default(self):
        test_object = self.test.element_datum_type1
        with mock.patch("common.models.BaseMixin.save"):
            test_object.save()

        actual = test_object.entity_name
        expected = "TestDatumType1Name"
        self.assertEqual(expected, actual)

    def test_entity_name_input(self):
        test_object = self.test.element_datum_type1
        test_object.entity_name = "custom_entity_name"
        with mock.patch("common.models.BaseMixin.save"):
            test_object.save()

        actual = test_object.entity_name
        expected = "custom_entity_name"
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
