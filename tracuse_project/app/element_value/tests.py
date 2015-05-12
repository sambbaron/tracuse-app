from django.test import TestCase

from .test_data import TestDataElementValue

from app.element_value.models import ElementValueModel, ElementValueString


class TestModelElementValueModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElementValue()

    def test_init_good_data_type(self):
        """Test ElementValueModel.__init__
        with data type name that corresponds to model name
        """
        actual = ElementValueModel(data_type_name="String")
        expected = ElementValueString
        self.assertEqual(expected, actual)

    def test_init_bad_data_type(self):
        """Test ElementValueModel.__init__
        with data type name that does not correspond to model name
        """
        self.assertRaisesMessage(NameError,
                                 "ElementValueOther model class does not exist",
                                 ElementValueModel,
                                 data_type_name="Other"
                                 )


class TestModelElementValueMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElementValue()


    def test_datum_object(self):
        """Test ElementValueMixin.datum_object
        """
        actual = self.test.element_value_string1.datum_object
        expected = self.test.datum_object1
        self.assertEqual(expected, actual)

    def test_element_type(self):
        """Test ElementValueMixin.element_type
        """
        actual = self.test.element_value_string1.element_type
        expected = self.test.element_type1
        self.assertEqual(expected, actual)

    def test_str(self):
        """Test ElementValueMixin.__str__
        """
        actual = self.test.element_value_string1.__str__()
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_get_sort_value(self):
        """Test ElementValueMixin.sort value
        no after_object - add to end
        """
        test_object = self.test.element_value_string1
        actual = test_object.get_sort_value()
        expected = 101001100
        self.assertEqual(expected, actual)
