from unittest import TestCase, mock

from components.common import utils


class TestStringUtils(TestCase):
    """Test string manipulation functions
    """

    @property
    def test_strings(self):
        return ["First Name", "FirstName", "firstName", "First", "firstname", "FIRSTNAME"]

    def test_camel_to_spaced_lower(self):
        expected_strings = ["first name", "first name", "first name", "first", "firstname", "f i r s t n a m e"]
        for test in self.test_strings:
            actual = utils.camel_to_spaced_lower(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_underscore(self):
        expected_strings = ["first_name", "first_name", "first_name", "first", "firstname", "f_i_r_s_t_n_a_m_e"]
        for test in self.test_strings:
            actual = utils.camel_to_underscore(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_spaced_capital(self):
        expected_strings = ["First Name", "First Name", "First Name", "First", "Firstname", "FIRSTNAME"]
        for test in self.test_strings:
            actual = utils.camel_to_spaced_capital(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)


class TestEntityMixin(TestCase):
    """Test Django ORM mixin classes used by all models"""

    def test_readable_name(self):
        from .mixins import EntityMixin

        test_mixin = EntityMixin()
        test_mixin.entity_name = "ThisObject"

        with mock.patch("django.db.models.base.Model.save"):
            test_mixin.save()

        actual = test_mixin.readable_name
        expected = "This Object"
        self.assertEqual(actual, expected)
