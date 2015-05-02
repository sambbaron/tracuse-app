from django.test import TestCase

from fixtures.test_data_simple import TestDataSimple


class TestModelDatumObject(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def tearDown(self):
        pass


    def test_datum_group(self):
        """Test DatumObject.datum_group property"""
        actual = self.test.datum_object1.datum_group
        expected = self.test.datum_group1
        self.assertEqual(expected, actual)

    def test_default_element_types(self):
        """Test DatumObject.default_element_types property"""
        actual = self.test.datum_object1.default_element_types
        expected = [self.test.element_type1]
        self.assertEqual(expected, actual)

    def test_element_value(self):
        """Test DatumObject.element_value method"""
        actual = self.test.datum_object1.element_value(
            element_type_object=self.test.element_type1
        )
        expected = self.test.element_value_string1
        self.assertEqual(expected, actual)

    def test_get_element_value(self):
        """Test DatumObject.get_element_value method"""
        actual = self.test.datum_object1.get_element_value(
            element_type_object=self.test.element_type1
        )
        expected = "Test Object Name"
        self.assertEqual(expected, actual)