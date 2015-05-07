from django.test import TestCase

from fixtures.mock_test_data import TestDataAssociation


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