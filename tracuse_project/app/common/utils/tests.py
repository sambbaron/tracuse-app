from django.test import TestCase

from . import entity
from . import model


class TestUtilsEntity(TestCase):
    """Test entity functions"""

    @property
    def test_strings(self):
        return ["First Name", "FirstName", "firstName", "First", "firstname", "FIRSTNAME"]

    def test_camel_to_spaced_lower(self):
        expected_strings = ["first name", "first name", "first name", "first", "firstname", "f i r s t n a m e"]
        for test in self.test_strings:
            actual = entity.camel_to_spaced_lower(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_underscore(self):
        expected_strings = ["first_name", "first_name", "first_name", "first", "firstname", "f_i_r_s_t_n_a_m_e"]
        for test in self.test_strings:
            actual = entity.camel_to_underscore(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_spaced_capital(self):
        expected_strings = ["First Name", "First Name", "First Name", "First", "Firstname", "FIRSTNAME"]
        for test in self.test_strings:
            actual = entity.camel_to_spaced_capital(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_sort_range_value_start(self):
        """Test sort_range_value returning start value
        """
        actual = entity.sort_range_value(
            sort_prefix="22",
            sort_base_length=4,
            return_start=True
        )
        expected = 220000
        self.assertEqual(expected, actual)

    def test_sort_range_value_end(self):
        """Test sort_range_value returning ending value
        """
        actual = entity.sort_range_value(
            sort_prefix="22",
            sort_base_length=4,
            return_start=False
        )
        expected = 229999
        self.assertEqual(expected, actual)


class TestUtilsModel(TestCase):
    """Test model functions"""

    def test_convert_field_data_boolean(self):
        """Test convert_field_data with boolean value
        """
        test_data = "true"
        test_type = "boolean"
        expected = True
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_integer(self):
        """Test convert_field_data with integer value
        """
        test_data = "9"
        test_type = "integer"
        expected = 9
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_json(self):
        """Test convert_field_data with json value
        """
        test_data = {"Test": "Data"}
        test_type = "json"
        expected = '{"Test": "Data"}'
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)
