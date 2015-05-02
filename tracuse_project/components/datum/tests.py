from django.test import TestCase

from model_mommy import mommy

from fixtures.test_data_simple import TestDataSimple


class TestModelDatumObject(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()


    def test_str_with_element(self):
        """Test DatumObject.__str__ property
        with "name" element type matching repr_expression
        """
        actual = self.test.datum_object1.__str__()
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_str_without_element(self):
        """Test DatumObject.__str__ property
        without element type matching repr_expression
        """
        actual = self.test.datum_object2.__str__()
        expected = "Blank Test Datum Type"
        self.assertEqual(expected, actual)

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

    def test_element_value_with_element_type(self):
        """Test DatumObject.element_value method
        with element_type assigned to datum_object
        """
        actual = self.test.datum_object1.element_value(
            element_type_object=self.test.element_type1
        )
        expected = self.test.element_value_string1
        self.assertEqual(expected, actual)

    def test_element_value_without_element_type(self):
        """Test DatumObject.element_value method
        with element_type not assigned to datum_object
        """
        element_type = mommy.make("element_type.ElementType")
        actual = self.test.datum_object1.element_value(
            element_type_object=element_type
        )
        expected = None
        self.assertEqual(expected, actual)

    def test_get_element_value_with_element_type(self):
        """Test DatumObject.get_element_value method
        with element_type assigned to datum_object
        """
        actual = self.test.datum_object1.get_element_value(
            element_type_object=self.test.element_type1
        )
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_get_element_value_without_element_type(self):
        """Test DatumObject.get_element_value method
        with element_type not assigned to datum_object
        """
        element_type = mommy.make("element_type.ElementType")
        actual = self.test.datum_object1.get_element_value(
            element_type_object=element_type
        )
        expected = None
        self.assertEqual(expected, actual)