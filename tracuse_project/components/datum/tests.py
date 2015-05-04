from django.test import TestCase, mock

from model_mommy import mommy

from fixtures.test_data_simple import TestDataSimple


class TestModelDatumType(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def test_calc_sort_with_after_datum_type(self):
        """Test DatumType._calc_sort method
        with DatumType to sort after
        """
        actual = self.test.datum_type2._calc_sort(self.test.datum_type1)
        expected = 10101
        self.assertEqual(expected, actual)

    def test_calc_sort_without_after_datum_type(self):
        """Test DatumType._calc_sort method
        without DatumType to sort after (assumes to end)
        """
        with mock.patch("utils.mixins.BaseMixin.last_sorted", new=self.test.datum_type1):
            actual = self.test.datum_type2._calc_sort()
        expected = 10101
        self.assertEqual(expected, actual)


class TestModelDatumObject(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()


    def test_str_with_element_type(self):
        """Test DatumObject.__str__ property
        with element type matching repr_expression in ElementTypeDatumObject,
        """
        actual = self.test.datum_object1.__str__()
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_str_without_element_value(self):
        """Test DatumObject.__str__ property
        with element type matching repr_expression in ElementTypeDatumObject,
        but no element_value in ElementValueModel
        """
        actual = self.test.datum_object2.__str__()
        expected = "Blank Test Datum Type"
        self.assertEqual(expected, actual)

    def test_str_without_element_type(self):
        """Test DatumObject.__str__ property
        without element type matching repr_expression in ElementTypeDatumObject,
        """
        actual = self.test.datum_object3.__str__()
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