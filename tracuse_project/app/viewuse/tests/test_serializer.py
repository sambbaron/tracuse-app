from django.test import TestCase

from .test_data import TestDataViewuse

from ..serializers import (ViewuseObjectSerializer,
                           ViewuseArrangementSerializer,
                           ViewuseDatumSerializer,
                           ViewuseNestedSerializer)


class TestViewuseObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseObjectSerializer.serial_default
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer\
            ("serial_default").serialize(test_object)
        actual = test_serialized["title"]
        expected = "Viewuse 1 Title"
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test ViewuseObjectSerializer.serial_related
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer\
            ("serial_related").serialize(test_object)
        actual = test_serialized["title"]
        expected = "Viewuse 1 Title"
        self.assertEqual(expected, actual)


class TestViewuseArrangementSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseArrangementSerializer.serial_default
        """
        test_object = self.test.viewuse_arrangement1
        test_serialized = ViewuseArrangementSerializer\
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Arrangement1"
        self.assertEqual(expected, actual)


class TestViewuseDatumSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseDatumSerializer.serial_default
        """
        test_object = self.test.viewuse_datum1
        test_serialized = ViewuseDatumSerializer\
            ("serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Datum1"
        self.assertEqual(expected, actual)


class TestViewuseNestedSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseNestedSerializer.serial_default
        """
        test_object = self.test.viewuse_nested1
        test_serialized = ViewuseNestedSerializer\
            ("serial_default").serialize(test_object)
        actual = test_serialized["parent_viewuse_id"]
        expected = self.test.viewuse_object1.viewuse_object_id
        self.assertEqual(expected, actual)
