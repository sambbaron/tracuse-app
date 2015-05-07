from model_mommy import mommy

from django.test import TestCase, mock

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

    def test_get_create_adjacent_association(self):
        """Test AssociationAdjacent.get_create_adjacent_association method
        """
        test_object = self.test.adjacent_association2
        actual = test_object.get_create_adjacent_association()
        self.assertIsNotNone(actual)
        self.assertEqual(test_object.parent_datum, actual.parent_datum)
        self.assertEqual(test_object.child_datum, actual.child_datum)
        self.assertEqual(1, actual.depth)

    def test_save_create_adjacent_association(self):
        """Test AssociationAdjacent.save method
        to test creation of adjacent association in AssociationAll
        """
        test_object = mommy.make("association.AssociationAdjacent",
                               parent_datum=self.test.datum_object3,
                               child_datum=self.test.datum_object5
                               )
        test_object.save()
        actual = test_object.get_create_adjacent_association()
        self.assertIsNotNone(actual)
        self.assertEqual(test_object.parent_datum, actual.parent_datum)
        self.assertEqual(test_object.child_datum, actual.child_datum)
        self.assertEqual(1, actual.depth)



class TestModelAssociationAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()


    def test_get_create_associations(self):
        """Test AssociationAll.get_create_association static method
        """
        from components.association.models import AssociationAll

        actual = AssociationAll.get_create_association(
            parent_datum=self.test.datum_object1,
            child_datum=self.test.datum_object2,
            depth=0
        )
        self.assertIsInstance(actual, AssociationAll)
        self.assertEqual(self.test.datum_object1, actual.parent_datum)
        self.assertEqual(self.test.datum_object2, actual.child_datum)