from django.test import TestCase

from .test_data import TestDataViewuse

from ..serializers import (ViewuseObjectSerializer,
                           ViewuseArrangementSerializer,
                           ViewuseDatumSerializer)


class TestViewuseObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_basic(self):
        """Test ViewuseObjectSerializer.serial_basic
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "Viewuse1"
        self.assertEqual(expected, actual)

    def test_serial_related_list(self):
        """Test ViewuseObjectSerializer.serial_related_list
        """
        test_object = self.test.viewuse_object1
        test_serialized = ViewuseObjectSerializer. \
            serial_related_list(test_object)
        actual = test_serialized["filters"][0]
        expected = {'TestFilter': 'TestFilter'}
        self.assertEqual(expected, actual)

class TestViewuseArrangementSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_basic(self):
        """Test ViewuseArrangementSerializer.serial_basic
        """
        test_object = self.test.viewuse_arrangement1
        test_serialized = ViewuseArrangementSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "Arrangement1"
        self.assertEqual(expected, actual)

class TestViewuseDatumSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def test_serial_basic(self):
        """Test ViewuseDatumSerializer.serial_basic
        """
        test_object = self.test.viewuse_datum1
        test_serialized = ViewuseDatumSerializer. \
            serial_basic(test_object)
        actual = test_serialized["entity_name"]
        expected = "Datum1"
        self.assertEqual(expected, actual)
