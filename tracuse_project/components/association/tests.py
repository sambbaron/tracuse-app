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