from django.test import TestCase

from .test_data import TestDataAssociation

from ..serializers import AssociationDirectionSerializer


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
