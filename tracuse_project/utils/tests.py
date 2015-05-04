from django.test import SimpleTestCase, TestCase, mock

from utils import names

from fixtures.test_data_simple import TestDataSimple


class TestUtilsNames(TestCase):
    """Test name string manipulation functions
    """

    @property
    def test_strings(self):
        return ["First Name", "FirstName", "firstName", "First", "firstname", "FIRSTNAME"]

    def test_camel_to_spaced_lower(self):
        expected_strings = ["first name", "first name", "first name", "first", "firstname", "f i r s t n a m e"]
        for test in self.test_strings:
            actual = names.camel_to_spaced_lower(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_underscore(self):
        expected_strings = ["first_name", "first_name", "first_name", "first", "firstname", "f_i_r_s_t_n_a_m_e"]
        for test in self.test_strings:
            actual = names.camel_to_underscore(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)

    def test_camel_to_spaced_capital(self):
        expected_strings = ["First Name", "First Name", "First Name", "First", "Firstname", "FIRSTNAME"]
        for test in self.test_strings:
            actual = names.camel_to_spaced_capital(test)
            expected = expected_strings[self.test_strings.index(test)]
            return self.assertEqual(expected, actual)


class TestModelBaseMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()


    def test_last_sorted(self):
        """Test BaseMixin.last_sorted class method
        """
        from components.datum.models import DatumGroup
        actual = DatumGroup.last_sorted()
        expected = self.test.datum_group3
        self.assertEqual(expected, actual)


class TestModelEntityMixin(TestCase):
    """Test Django ORM mixin classes used by all models"""

    def setUp(self):
        from utils.mixins import EntityMixin

        self.test_mixin = EntityMixin()
        self.test_mixin.entity_name = "ThisObject"

    def tearDown(self):
        self.test_mixin = None


    def test_entity_str(self):
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.__str__()
        expected = "This Object"
        self.assertEqual(expected, actual)

    def test_readable_name_input(self):
        self.test_mixin.readable_name = "Custom Readable Name"
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.readable_name
        expected = "Custom Readable Name"
        self.assertEqual(expected, actual)

    def test_schema_name_default(self):
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.schema_name
        expected = "this_object"
        self.assertEqual(expected, actual)

    def test_schema_name_input(self):
        self.test_mixin.schema_name = "custom_schema_name"
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.schema_name
        expected = "custom_schema_name"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_s(self):
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.readable_plural_name
        expected = "This Objects"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_es(self):
        self.test_mixin.entity_name = "ThisStatus"
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.readable_plural_name
        expected = "This Statuses"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_input(self):
        self.test_mixin.readable_plural_name = "custom plural names"
        with mock.patch("django.db.models.base.Model.save"):
            self.test_mixin.save()

        actual = self.test_mixin.readable_plural_name
        expected = "custom plural names"
        self.assertEqual(expected, actual)