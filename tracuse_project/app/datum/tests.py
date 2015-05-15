from django.test import TestCase

from model_mommy import mommy

from .test_data import TestDataDatum
from app.association.test_data import TestDataAssociation


class TestModelDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()


    def test_headline_with_element_type(self):
        """Test DatumObject.headline property
        with element type matching str_expression in ElementDatumObject,
        """
        actual = self.test.datum_object1.headline
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_headline_without_element_value(self):
        """Test DatumObject.headline property
        with element type matching str_expression in ElementDatumObject,
        but no element_value in ElementValueModel
        """
        actual = self.test.datum_object2.headline
        expected = "Blank Test Datum Type1"
        self.assertEqual(expected, actual)

    def test_headline_without_element_type(self):
        """Test DatumObject.headline property
        without element type matching str_expression in ElementDatumObject,
        """
        actual = self.test.datum_object3.headline
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
        actual = self.test.datum_object1.element_value(self.test.element_type3)
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

    def test_get_associated_datums_parent_with_distance(self):
        """Test DatumObject.get_associated_datums
        with distance limit
        """
        test_object = self.test.datum_object3
        parent_direction = self.test.association_direction1
        actual = test_object.get_associated_datums(
            direction=parent_direction,
            distance_limit=2
        )
        expected = [self.test.datum_object1,
                    self.test.datum_object2,
                    self.test.datum_object3
                    ]
        self.assertEqual(3, len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_get_associated_datums_child_no_distance(self):
        """Test DatumObject.get_associated_datums
        without distance limit
        """
        test_object = self.test.datum_object1
        child_direction = self.test.association_direction3
        actual = test_object.get_associated_datums(
            direction=child_direction,
            distance_limit=None
        )
        self.assertEqual(7, len(actual))
        self.assertEqual(self.test.datum_object2,
                         actual[0])

    def test_get_associated_datums_both_adjacent(self):
        """Test DatumObject.get_associated_datums
        distance_limit=1
        """
        test_object = self.test.datum_object6
        both_direction = self.test.association_direction2
        actual = test_object.get_associated_datums(
            direction=both_direction,
            distance_limit=1
        )
        expected = [self.test.datum_object1,
                    self.test.datum_object6,
                    self.test.datum_object7
                    ]
        self.assertEqual(3, len(actual))
        self.assertEqual(set(expected), set(actual))


class TestSerializersDatum(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()


    def test_datum_object_element_expr(self):
        """Test datum_object_element_expr
        """
        from .serializers import datum_object_element_expr

        test_object = self.test.datum_object1
        actual = datum_object_element_expr(test_object)
        self.assertEqual("Test Object Name", actual["name"])
