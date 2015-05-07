from model_mommy import mommy

from django.test import TestCase

from fixtures.mock_test_data import TestDataAssociation


class TestModelAssociationAdjacent(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_str(self):
        """Test AssociationMixin.__str__
        using AssociationAdjacent object
        """
        actual = self.test.adjacent_association1.__str__()
        expected = "Test Object1 -> Test Object2"
        self.assertEqual(expected, actual)

    # def test_save_set_associations(self):
    #     """Test AssociationAdjacent.save method
    #     to test creation of adjacent association in AssociationAll
    #     """
    #     test_object = mommy.make("association.AssociationAdjacent",
    #                              parent_datum=self.test.datum_object3,
    #                              child_datum=self.test.datum_object5
    #                              )
    #     test_object.save()
    #     actual = test_object.get_create_adjacent_association()
    #     self.assertIsNotNone(actual)
    #     self.assertEqual(test_object.parent_datum, actual.parent_datum)
    #     self.assertEqual(test_object.child_datum, actual.child_datum)
    #     self.assertEqual(1, actual.depth)

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


class TestModelAssociationAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_get_create_associations(self):
        """Test AssociationAll.get_create_association static method
        """
        from components.association.models import AssociationAll

        test_object1 = mommy.make("datum.DatumObject")
        test_object2 = mommy.make("datum.DatumObject")
        actual = AssociationAll.get_create_association(
            parent_datum=test_object1,
            child_datum=test_object2,
            depth=0
        )
        self.assertIsInstance(actual, AssociationAll)
        self.assertEqual(test_object1, actual.parent_datum)
        self.assertEqual(test_object2, actual.child_datum)