from django.test import TestCase

from .test_data import TestDataViewuse

from ..serializers import (ViewuseObjectSerializer,
                           ViewuseArrangementSerializer,
                           ViewuseDatumSerializer)


class TestViewuseObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_default(self):
        """Test ViewuseObjectSerializer.serial_default
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer\
            (template="serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Viewuse1"
        self.assertEqual(expected, actual)

    def test_serial_related(self):
        """Test ViewuseObjectSerializer.serial_related
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer\
            (template="serial_related").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Viewuse1"
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
            (template="serial_default").serialize(test_object)
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
            (template="serial_default").serialize(test_object)
        actual = test_serialized["entity_name"]
        expected = "Datum1"
        self.assertEqual(expected, actual)
