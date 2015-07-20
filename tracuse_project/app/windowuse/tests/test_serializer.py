from django.test import TestCase

from .test_data import TestDataWindowuse

from ..serializers import (WindowuseObjectSerializer,
                           WindowuseViewuseSerializer)


class TestWindowuseObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def test_serial_default(self):
        """Test WindowuseObjectSerializer.serial_default
        """
        test_object = self.test.windowuse_object1
        test_serialized = WindowuseObjectSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["title"]
        expected = "Windowuse 1 Title"
        self.assertEqual(expected, actual)


class TestWindowuseViewuseSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def test_serial_default(self):
        """Test WindowuseViewuseSerializer.serial_default
        """
        test_object = self.test.windowuse_viewuse1
        test_serialized = WindowuseViewuseSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["windowuse_object_id"]
        expected = self.test.windowuse_object1.windowuse_object_id
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test WindowuseViewuseSerializer.serial_related
        """
        test_object = self.test.windowuse_viewuse1
        test_serialized = WindowuseViewuseSerializer \
            ("serial_related").serialize(test_object)
        actual = test_serialized["viewuse_object"]
        expected = self.test.viewuse_object1.viewuse_object_id
        self.assertEqual(expected, actual)
