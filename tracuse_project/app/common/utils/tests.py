from django.test import TestCase

from . import entity, expression


class TestUtilsExpression(TestCase):
    """Test Expression Functions"""

    def test_expr_django_template_success(self):
        """Test expression.expr_django_template"""
        expr_string = "Test Expression - {{TestValue}}"
        data_dict = {"TestValue": "Here is the test value"}
        actual = expression.expr_django_template(expr_string=expr_string,
                                                 data_dict=data_dict
                                                 )
        expected = "Test Expression - Here is the test value"
        self.assertEqual(expected, actual)


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