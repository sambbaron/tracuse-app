from django.test import TestCase

from .test_data import TestDataAssociation

from ..serializers import AssociationDirectionSerializer, AssociationAllSerializer
from ..models import AssociationAll


class TestAssociationDirectionSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def test_serial_default(self):
        """Test AssociationDirectionSerializer.serial_default
        """
        test_object = self.test.association_direction1
        test_serialized = AssociationDirectionSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "parent"
        self.assertEqual(expected, actual)


class TestAssociationAllSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def test_serial_related(self):
        """Test AssociationAllSerializer.serial_related
        """
        test_object = AssociationAll.objects.first()
        test_serialized = AssociationAllSerializer \
            ("serial_related").serialize(test_object)
        actual = test_serialized["parent_datum"]
        expected = test_object.parent_datum_id
        self.assertEqual(expected, actual)

    def test_serial_parent(self):
        """Test AssociationAllSerializer.serial_parent
        """
        test_object = AssociationAll.objects.first()
        test_serialized = AssociationAllSerializer \
            ("serial_parent").serialize(test_object)
        actual = test_serialized["datum_object_id"]
        expected = test_object.parent_datum_id
        self.assertEqual(expected, actual)

    def test_serial_child(self):
        """Test AssociationAllSerializer.serial_child
        """
        test_object = AssociationAll.objects.first()
        test_serialized = AssociationAllSerializer \
            ("serial_child").serialize(test_object)
        actual = test_serialized["datum_object_id"]
        expected = test_object.child_datum_id
        self.assertEqual(expected, actual)
