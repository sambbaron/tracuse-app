from django.test import TestCase, mock

from .test_data import TestDataCommon


class TestManagerBaseMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def test_base_mixin_manager_active(self):
        """Test BaseMixinManagerActive.get_queryset
        """
        from app.datum.models import DatumType

        actual = DatumType.actives.all().count()
        expected = 2
        self.assertEqual(expected, actual)

    def test_base_mixin_manager_inactive(self):
        """Test BaseMixinManagerInactive.get_queryset
        """
        from app.datum.models import DatumType

        actual = DatumType.inactives.all().count()
        expected = 1
        self.assertEqual(expected, actual)


class TestModelBaseMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()


    def test_last_sort_value_no_sort_range(self):
        """Test BaseMixin._last_sort_value
        without sort range - returns maximum sort value
            of all objects
        """
        test_object = self.test.datum_type2
        actual = test_object._last_sort_value()
        expected = 20100
        self.assertEqual(expected, actual)

    def test_last_sort_value_with_sort_range(self):
        """Test BaseMixin._last_sort_value
        with sort range - returns maximum sort value
            of objects in sequence
        """
        test_object = self.test.datum_type2
        actual = test_object._last_sort_value(10000, 10999)
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
        expected = 101010010
        self.assertEqual(expected, actual)

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

    def test_calc_sort_prefix_reset(self):
        """Test BaseMixin._calc_sort_value method
        with new prefix sort
        base value resets
        """
        test_object = self.test.datum_type3
        sort_parts = [test_object.datum_group.sort,
                      ]
        actual = test_object._calc_sort_value(sort_base_length=4,
                                              increment=1,
                                              sort_prefix_parts=sort_parts
                                              )
        expected = 201000
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

    def test_reset_sort(self):
        """Test BaseMixin.reset_sort method"""
        from app.datum.models import DatumGroup

        DatumGroup.reset_sort()
        first_test_object = DatumGroup.objects.first()
        last_test_object = DatumGroup.objects.last()
        self.assertEqual(10, first_test_object.sort)
        self.assertEqual(30, last_test_object.sort)


class TestModelEntityMixin(TestCase):
    """Test Django ORM mixin classes used by all models"""

    def setUp(self):
        from app.datum.models import DatumGroup

        self.test_object = DatumGroup()
        self.test_object.entity_name = "ThisObject"

    def tearDown(self):
        self.test_object = None


    def test_entity_str(self):
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.__str__()
        expected = "This Object"
        self.assertEqual(expected, actual)

    def test_readable_name_input(self):
        self.test_object.readable_name = "Custom Readable Name"
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_name
        expected = "Custom Readable Name"
        self.assertEqual(expected, actual)

    def test_schema_name_default(self):
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.schema_name
        expected = "this_object"
        self.assertEqual(expected, actual)

    def test_schema_name_input(self):
        self.test_object.schema_name = "custom_schema_name"
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.schema_name
        expected = "custom_schema_name"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_s(self):
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "This Objects"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default_es(self):
        self.test_object.entity_name = "ThisStatus"
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "This Statuses"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_input(self):
        self.test_object.readable_plural_name = "custom plural names"
        with mock.patch("common.models.BaseMixin.save"):
            self.test_object.save()

        actual = self.test_object.readable_plural_name
        expected = "custom plural names"
        self.assertEqual(expected, actual)