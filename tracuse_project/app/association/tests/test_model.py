from model_mommy import mommy

from django.test import TestCase

from association.tests.test_data import TestDataAssociation


class TestManagerAssociationManager(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_filter_distance_with_limit(self):
        """Test AssociationManager.filter_distance
        with limit value
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.filter_distance(2).all().count()
        expected = 16
        self.assertEqual(expected, actual)

    def test_filter_distance_without_limit(self):
        """Test AssociationManager.filter_distance
        without limit value - default to 1
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.filter_distance().all().count()
        expected = 13
        self.assertEqual(expected, actual)

    def test_filter_distance_none_limit(self):
        """Test AssociationManager.filter_distance
        with none limit value - all associations
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.filter_distance(None).all().count()
        expected = 17
        self.assertEqual(expected, actual)

    def test_exclude_self_true(self):
        """Test AssociationManager.exclude_self
        with true
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.exclude_self(True).all().count()
        expected = 10
        self.assertEqual(expected, actual)

    def test_exclude_self_false(self):
        """Test AssociationManager.exclude_self
        with false - all associations
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.exclude_self(False).all().count()
        expected = 17
        self.assertEqual(expected, actual)

    def test_exclude_self_without_option(self):
        """Test AssociationManager.exclude_self
        without boolean option - default True
        """
        from app.association.models import AssociationAll

        actual = AssociationAll.objects.exclude_self().all().count()
        expected = 10
        self.assertEqual(expected, actual)


class TestModelAssociationDirection(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def test_parent(self):
        """Test AssociationDirection.parent class method"""
        from app.association.models import AssociationDirection

        actual = AssociationDirection.parent()
        self.assertEqual(-1, actual.pk)
        self.assertEqual("parent", actual.entity_name)

    def test_both(self):
        """Test AssociationDirection.both class method"""
        from app.association.models import AssociationDirection

        actual = AssociationDirection.both()
        self.assertEqual(0, actual.pk)
        self.assertEqual("both", actual.entity_name)

    def test_child(self):
        """Test AssociationDirection.child class method"""
        from app.association.models import AssociationDirection

        actual = AssociationDirection.child()
        self.assertEqual(1, actual.pk)
        self.assertEqual("child", actual.entity_name)


class TestModelAssociationAdjacent(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_str(self):
        """Test AssociationAdjacent.__str__
        """
        actual = self.test.adjacent_association1.__str__()
        expected = "Test Object1 -> Test Object2 = Default Association Type"
        self.assertEqual(expected, actual)

    def test_all_associations(self):
        """Test AssociationAdjacent.all_associations property
        """
        test_object = self.test.adjacent_association6
        actual = test_object.all_associations
        expected_count = 3
        self.assertEqual(expected_count, len(actual))

    def test_delete_associations(self):
        """Test AssociationAdjacent.delete_associations method
        """
        test_object = self.test.adjacent_association4
        test_object._delete_associations()
        actual = test_object.all_associations
        expected_count = 0
        self.assertEqual(expected_count, len(actual))

    def test_create_associations_1_adjacent(self):
        """Test AssociationAdjacent._create_associations method
        2 nodes, 1 Adjacent
        """
        test_object = self.test.adjacent_association4
        actual = test_object._create_associations()
        expected_count = 3
        self.assertEqual(expected_count, len(actual))

    def test_create_associations_2_adjacent(self):
        """Test AssociationAdjacent._create_associations method
        3 nodes, 2 Adjacent
        """
        test_object = self.test.adjacent_association6
        actual = test_object._create_associations()
        expected_count = 4
        self.assertEqual(expected_count, len(actual))

    def test_create_associations_3_adjacent(self):
        """Test AssociationAdjacent._create_associations method
        4 nodes, 3 Adjacent
        """
        test_object = self.test.adjacent_association1
        actual = test_object._create_associations()
        expected_count = 5
        self.assertEqual(expected_count, len(actual))

    def test_save_create_associations(self):
        """Test AssociationAdjacent.save method
        to test creation of associations in AssociationAll
        """
        new_datum1 = mommy.make("datum.DatumObject")
        new_datum2 = mommy.make("datum.DatumObject")
        test_object = mommy.make("association.AssociationAdjacent",
                                 parent_datum=new_datum1,
                                 child_datum=new_datum2
                                 )
        test_object.save()
        actual = test_object.all_associations
        expected_count = 3
        self.assertEqual(expected_count, len(actual))


class TestModelAssociationAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_str(self):
        """Test AssociationAll.__str__
        """
        test_object = mommy.prepare("association.AssociationAll",
                                    parent_datum=self.test.datum_object1,
                                    child_datum=self.test.datum_object2,
                                    distance=3
                                    )
        actual = test_object.__str__()
        expected = "Test Object1 -> Test Object2 = 3"
        self.assertEqual(expected, actual)

    def test_get_create_associations(self):
        """Test AssociationAll.get_create_association static method
        """
        from app.association.models import AssociationAll

        test_object1 = mommy.make("datum.DatumObject")
        test_object2 = mommy.make("datum.DatumObject")
        actual = AssociationAll.get_create_association(
            parent_datum=test_object1,
            child_datum=test_object2,
            distance=2
        )
        self.assertIsInstance(actual, AssociationAll)
        self.assertEqual(test_object1, actual.parent_datum)
        self.assertEqual(test_object2, actual.child_datum)
        self.assertEqual(2, actual.distance)