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
        actual = self.test.value_category_name.datum_object
        expected = self.test.datum_category
        self.assertEqual(expected, actual)

    def test_element_type(self):
        """Test ElementValueMixin.element_type
        """
        actual = self.test.value_category_name.element_type
        expected = self.test.element_type_name
        self.assertEqual(expected, actual)

    def test_get_sort_value(self):
        """Test ElementValueMixin.sort value
        no after_object - add to end
        """
        test_object = self.test.value_category_name
        actual = test_object.get_sort_value()
        expected = 101001100
        self.assertEqual(expected, actual)

    def test_str_string(self):
        """Test ElementValueMixin.__str__
        with string value
        """
        actual = self.test.value_category_name.__str__()
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_str_date(self):
        """Test ElementValueMixin.__str__
        with datetime value
        """
        actual = self.test.value_event_endingdate.__str__()
        expected = "Test datetime is May 12, 2015 4:30 PM"
        self.assertEqual(expected, actual)
