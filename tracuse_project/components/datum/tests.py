from django.test import TestCase, mock

from model_mommy import mommy

from fixtures.mock_test_data import TestDataDatumElement


class TestModelDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatumElement()


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
        expected = "Blank Test Datum Type1"
        self.assertEqual(expected, actual)

    def test_str_without_element_type(self):
        """Test DatumObject.__str__ property
        without element type matching repr_expression in ElementTypeDatumObject,
        """
        actual = self.test.datum_object3.__str__()
        expected = "Blank Test Datum Type1"
        self.assertEqual(expected, actual)

    def test_datum_group(self):
        """Test DatumObject.datum_group property"""
        actual = self.test.datum_object1.datum_group
        expected = self.test.datum_group1
        self.assertEqual(expected, actual)

    def test_default_element_types(self):
        """Test DatumObject.default_element_types property"""
        actual = self.test.datum_object1.default_element_types
        expected = [self.test.element_type1, self.test.element_type2]
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

    def test_get_sort_value(self):
        """Test DatumObject.sort value
        no after_object - add to end
        """
        test_object = self.test.datum_object1
        actual = test_object.get_sort_value()
        expected = 101004
        self.assertEqual(expected, actual)

    def test_get_create_self_association(self):
        """Test DatumObject._self_association property
        if exists
        """
        test_object = self.test.datum_object2
        actual = test_object.get_create_self_association()
        self.assertIsNotNone(actual)
        self.assertEqual(actual.parent_datum, actual.child_datum)
        self.assertEqual(0, actual.depth)

    def test_save_create_self_association(self):
        """Test DatumObject.save method
        to test creation of self association
        """
        test_object = mommy.make("datum.DatumObject",
                               user=self.test.user1,
                               datum_type=self.test.datum_type1
                               )
        test_object.save()
        actual = test_object.get_create_self_association()
        self.assertIsNotNone(actual)
        self.assertEqual(actual.parent_datum, actual.child_datum)
        self.assertEqual(0, actual.depth)

    def test_save_with_elements(self):
        """Test DatumObject.save method
        to test creation of default elements
        """
        test_object = mommy.make("datum.DatumObject",
                               user=self.test.user1,
                               datum_type=self.test.datum_type1
                               )
        test_object.save()

        datum_element_count = test_object.element_types.count()
        self.assertEqual(2, datum_element_count)