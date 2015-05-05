from django.test import TestCase, mock

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
        """Test BaseMixin.last_sort_value class method"""
        test_object = self.test.datum_type2

        actual = test_object.last_sort_value()
        expected = 10100
        self.assertEqual(expected, actual)

    def test_calc_sort_with_after_object(self):
        """Test BaseMixin._calc_sort_value method
        with object to sort after
        """
        test_object = self.test.datum_type2
        actual = test_object._calc_sort_value(after_object=self.test.datum_type1,
                                              sort_base_length=3,
                                              increment=1,
                                              sort_prefix_parts=[test_object.datum_group.sort]
                                              )
        expected = 10101
        self.assertEqual(expected, actual)

    def test_calc_sort_without_after_object(self):
        """Test BaseMixin._calc_sort_value method
        without object to sort after
        """
        test_object = self.test.datum_type2
        actual = test_object._calc_sort_value(sort_base_length=3,
                                              increment=1,
                                              sort_prefix_parts=[test_object.datum_group.sort]
                                              )
        expected = 10101
        self.assertEqual(expected, actual)

    def test_calc_sort_multiple_parts(self):
        """Test BaseMixin._calc_sort_value method
        with more than one parent prefix part
        with no after_object: add to end
        """
        test_object = self.test.datum_object1
        sort_parts = [test_object.datum_group.sort,
                      test_object.datum_type.sort
                      ]
        actual = self.test.datum_object1._calc_sort_value(sort_base_length=2,
                                                          increment=1,
                                                          sort_prefix_parts=sort_parts
                                                          )

    def test_calc_sort_no_base_sort(self):
        """Test BaseMixin._calc_sort_value method
        with no zero fill: sort_base_length = -1
        with no after_object: add to end
        """
        test_object = self.test.datum_object1
        sort_parts = [test_object.datum_group.sort,
                      test_object.datum_type.sort
                      ]
        actual = test_object._calc_sort_value(sort_base_length=-1,
                                              increment=1,
                                              sort_prefix_parts=sort_parts
                                              )
        expected = 1010100
        self.assertEqual(expected, actual)

    def test_get_sort_value_with_after_object(self):
        """Test BaseMixin.get_sort_value method
        with object to sort after
        """
        test_object = self.test.datum_type2
        actual = test_object.get_sort_value(after_object=self.test.datum_type1)
        expected = 10101
        self.assertEqual(expected, actual)

    def test_get_sort_value_without_after_object(self):
        """Test BaseMixin.get_sort_value method
        with object to sort after
        """
        test_object = self.test.datum_type2
        actual = test_object.get_sort_value()
        expected = 10101
        self.assertEqual(expected, actual)

    def test_save_sort_value(self):
        """Test BaseMixin.save method"""
        test_object = self.test.datum_type2
        with mock.patch("django.db.models.base.Model.save"):
            test_object.save()
        actual = test_object.sort
        expected = 10101
        self.assertEqual(expected, actual)


class TestModelEntityMixin(TestCase):
    """Test Django ORM mixin classes used by all models"""

    def setUp(self):
        from components.datum.models import DatumGroup

        self.test_object = DatumGroup()
        self.test_object.entity_name = "ThisObject"

    def tearDown(self):
        self.test_object = None


    def test_entity_str(self):
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.__str__()
        expected = "This Object"
        self.assertEqual(expected, actual)

    def test_readable_name_input(self):
        self.test_object.readable_name = "Custom Readable Name"
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_name
        expected = "Custom Readable Name"
        self.assertEqual(expected, actual)

    def test_schema_name_default(self):
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.schema_name
        expected = "this_object"
        self.assertEqual(expected, actual)

    def test_schema_name_input(self):
        self.test_object.schema_name = "custom_schema_name"
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.schema_name
        expected = "custom_schema_name"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_s(self):
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "This Objects"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_es(self):
        self.test_object.entity_name = "ThisStatus"
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "This Statuses"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_input(self):
        self.test_object.readable_plural_name = "custom plural names"
        with mock.patch("utils.mixins.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "custom plural names"
        self.assertEqual(expected, actual)