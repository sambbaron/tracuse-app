from django.test import TestCase

from model_mommy import mommy

from .test_data import TestDataDatum
from association.tests.test_data import TestDataAssociation


class TestModelDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_title_with_element_type(self):
        """Test DatumObject.title property
        with element type matching title_expression in ElementDatumObject,
        """
        actual = self.test.datum_object1.title
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_title_without_element_value(self):
        """Test DatumObject.title property
        with element type matching title_expression in ElementDatumObject,
        but no element_value in ElementValueModel
        """
        actual = self.test.datum_object2.title
        expected = "Blank Test Datum Type1"
        self.assertEqual(expected, actual)

    def test_title_without_element_type(self):
        """Test DatumObject.title property
        without element type matching title_expression in ElementDatumObject,
        """
        actual = self.test.datum_object3.title
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
        expected = [self.test.element_type1,
                    self.test.element_type2,
                    self.test.element_type3
                    ]
        self.assertEqual(expected, actual)

    def test_elements(self):
        """Test DatumObject.elements property"""
        actual = self.test.datum_object1.elements
        expected = [self.test.element_datum_object1,
                    self.test.element_datum_object2,
                    self.test.element_datum_object3
                    ]
        self.assertEqual(set(expected), set(actual))

    def test_element_value_with_good_element_type(self):
        """Test DatumObject.element_value method
        with element type in datum
        """
        actual = self.test.datum_object1.element_value(self.test.element_type1)
        expected = self.test.element_value_string1
        self.assertEqual(expected, actual)

    def test_element_value_with_bad_element_type(self):
        """Test DatumObject.element_value method
        with element type not in datum
        """
        from app.element_type.models import ElementType

        actual = self.test.datum_object1.element_value(ElementType())
        expected = None
        self.assertEqual(expected, actual)

    def test_element_value_with_kwargs(self):
        """Test DatumObject.element_value method
        with element type not in datum
        """
        actual = self.test.datum_object1.element_value(
            entity_name="Name"
        )
        expected = self.test.element_value_string1
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
        """Test DatumObject._self_association method
        """
        test_object = self.test.datum_object2
        actual = test_object.get_create_self_association()
        self.assertIsNotNone(actual)
        self.assertEqual(actual.parent_datum, actual.child_datum)
        self.assertEqual(0, actual.distance)

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
        self.assertEqual(0, actual.distance)

    def test_save_with_element_types(self):
        """Test DatumObject.save method
        to test creation of default element types
        """
        test_object = mommy.make("datum.DatumObject",
                                 user=self.test.user1,
                                 datum_type=self.test.datum_type1
                                 )
        test_object.save()

        datum_element_count = test_object.element_types.count()
        expected_count = 3
        self.assertEqual(expected_count, datum_element_count)

    def test_save_with_element_values(self):
        """Test DatumObject.save method
        to test creation of default element values
        string value - default empty
        """
        test_object = mommy.make("datum.DatumObject",
                                 user=self.test.user1,
                                 datum_type=self.test.datum_type1
                                 )
        test_object.save()
        first_element = test_object.elements.first()
        element_value = first_element.get_elvalue
        expected_value = ""
        self.assertEqual(expected_value, element_value)


class TestModelDatumObjectAssociationProperties(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def test_adjacent_parent_datums_m2m(self):
        """Test DatumObject.adjacent_parent_datums
        m2m to AssociationAdjacent exclusive of datum
        """
        test_object = self.test.datum_object4
        actual = test_object.adjacent_parent_datums.all()
        self.assertEqual(1, actual.count())

    def test_adjacent_child_datums_m2m(self):
        """Test DatumObject.adjacent_child_datums
        m2m to AssociationAllAdjacent exclusive of datum
        """
        test_object = self.test.datum_object1
        actual = test_object.adjacent_child_datums.all()
        self.assertEqual(3, actual.count())

    def test_all_parent_datums_m2m(self):
        """Test DatumObject.all_parent_datums
        m2m to AssociationAll inclusive of datum
        """
        test_object = self.test.datum_object4
        actual = test_object.all_parent_datums.all()
        self.assertEqual(4, actual.count())

    def test_all_child_datums_m2m(self):
        """Test DatumObject.all_child_datums
        m2m to AssociationAll inclusive of datum
        """
        test_object = self.test.datum_object1
        actual = test_object.all_child_datums.all()
        self.assertEqual(7, actual.count())

    def test_association_queryset_parent(self):
        """Test DatumObject.association_queryset
        with parent direction and no other args
        """
        from app.association.managers import AssociationQuerySet

        test_object = self.test.datum_object4
        parent_direction = self.test.association_direction1
        test_queryset = test_object.association_queryset(
            direction=parent_direction,
        )

        self.assertEqual(1, len(test_queryset))

        actual_type = type(test_queryset)
        expected_type = AssociationQuerySet
        self.assertEqual(expected_type, actual_type)

        actual_datum = test_queryset[0].parent_datum
        expected_datum = self.test.datum_object3
        self.assertEqual(expected_datum, actual_datum)

    def test_association_queryset_child(self):
        """Test DatumObject.association_queryset
        with child direction and no other args
        """
        from app.association.managers import AssociationQuerySet

        test_object = self.test.datum_object3
        child_direction = self.test.association_direction3
        test_queryset = test_object.association_queryset(
            direction=child_direction,
        )

        self.assertEqual(1, len(test_queryset))

        actual_type = type(test_queryset)
        expected_type = AssociationQuerySet
        self.assertEqual(expected_type, actual_type)

        actual_datum = test_queryset[0].child_datum
        expected_datum = self.test.datum_object4
        self.assertEqual(expected_datum, actual_datum)

    def test_association_queryset_both(self):
        """Test DatumObject.association_queryset
        with both directions and no other args
        """
        from app.association.managers import AssociationQuerySet

        test_object = self.test.datum_object3
        both_direction = self.test.association_direction2
        test_queryset = test_object.association_queryset(
            direction=both_direction,
        )

        self.assertEqual(2, len(test_queryset))

        actual_type = type(test_queryset)
        expected_type = AssociationQuerySet
        self.assertEqual(expected_type, actual_type)

        actual_datum = test_queryset[0].parent_datum
        expected_datum = self.test.datum_object2
        self.assertEqual(expected_datum, actual_datum)

    def test_association_queryset_distance_value(self):
        """Test DatumObject.association_queryset
        using parent direction
        with distance limit
        """
        test_object = self.test.datum_object4
        parent_direction = self.test.association_direction1
        test_queryset = test_object.association_queryset(
            direction=parent_direction,
            distance_limit=2
        )

        self.assertEqual(2, len(test_queryset))

        actual_datum1 = test_queryset[0].parent_datum
        expected_datum1 = self.test.datum_object3
        self.assertEqual(expected_datum1, actual_datum1)

        actual_datum2 = test_queryset[1].parent_datum
        expected_datum2 = self.test.datum_object2
        self.assertEqual(expected_datum2, actual_datum2)

    def test_association_queryset_distance_none(self):
        """Test DatumObject.association_queryset
        using child direction
        with no distance limit (all associations)
        """
        test_object = self.test.datum_object1
        child_direction = self.test.association_direction3
        test_queryset = test_object.association_queryset(
            direction=child_direction,
            distance_limit=None
        )

        self.assertEqual(6, len(test_queryset))

    def test_association_queryset_additional_filter(self):
        """Test DatumObject.association_queryset
        using parent direction
        with additional filter
        """
        from django.db.models import Q

        test_object = self.test.datum_object4
        parent_direction = self.test.association_direction1
        additional_filter = Q(parent_datum_id__datum_type=self.test.datum_type2)
        test_queryset = test_object.association_queryset(
            direction=parent_direction,
            distance_limit=None,
            additional_filter=additional_filter
        )

        self.assertEqual(1, len(test_queryset))

        actual_datum1 = test_queryset[0].parent_datum
        expected_datum1 = self.test.datum_object3
        self.assertEqual(expected_datum1, actual_datum1)

    def test_association_queryset_additional_filter_bad(self):
        """Test DatumObject.association_queryset
        using parent direction
        with additional filter incorrect object type
        """
        test_object = self.test.datum_object4
        parent_direction = self.test.association_direction1
        additional_filter = {"parent_datum_id__datum_type": self.test.datum_type2}
        with self.assertRaisesMessage(TypeError, "Additional filter must be Q object."):
            test_object.association_queryset(
                direction=parent_direction,
                distance_limit=None,
                additional_filter=additional_filter
            )

    def test_association_queryset_return_method(self):
        """Test DatumObject.association_queryset
        using child direction
        with return method
        """
        test_object = self.test.datum_object2
        child_direction = self.test.association_direction3
        test_queryset = test_object.association_queryset(
            direction=child_direction,
            return_method="values"
        )

        self.assertEqual(1, len(test_queryset))

        actual_type = type(test_queryset[0])
        expected_type = dict
        self.assertEqual(expected_type, actual_type)

    def test_association_queryset_return_method_with_args(self):
        """Test DatumObject.association_queryset
        using parent direction
        with return method and return args
        """
        test_object = self.test.datum_object2
        parent_direction = self.test.association_direction1
        test_queryset = test_object.association_queryset(
            direction=parent_direction,
            return_method="values",
            return_args=["parent_datum__datum_object_id"]
        )

        self.assertEqual(1, len(test_queryset))

        actual_type = type(test_queryset[0])
        expected_type = dict
        self.assertEqual(expected_type, actual_type)

    def test_association_queryset_return_method_with_args_and_kwargs(self):
        """Test DatumObject.association_queryset
        using parent direction
        with return method and return args and kwargs
        """
        test_object = self.test.datum_object2
        parent_direction = self.test.association_direction1
        test_queryset = test_object.association_queryset(
            direction=parent_direction,
            return_method="values_list",
            return_args=["parent_datum__datum_object_id"],
            return_kwargs={"flat":True}
        )

        self.assertEqual(1, len(test_queryset))

        actual_type = type(test_queryset[0])
        expected_type = int
        self.assertEqual(expected_type, actual_type)