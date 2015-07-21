from django.test import TestCase

from .test_data import TestDataViewuse

from ..serializers import ViewuseObjectSerializer


class TestViewuseObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseObjectSerializer.serial_default
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["title"]
        expected = "Viewuse 1 Title"
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test ViewuseObjectSerializer.serial_related
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer \
            ("serial_related").serialize(test_object)
        actual = test_serialized["title"]
        expected = "Viewuse 1 Title"
        self.assertEqual(expected, actual)
