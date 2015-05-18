import json

from django.test import TestCase
from common.tests.test_data import TestDataCommon

from ..serializers import Serializer


class TestSerializerMethods(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def test_serialize_all(self):
        """Test serialize_all method
        using DatumGroup
        """
        from ..serializers import serialize_all
        from app.datum.models import DatumGroup

        test_object = self.test.datum_group1
        test_serializer = serialize_all(DatumGroup, test_object)
        actual = test_serializer["entity_name"]
        expected = "TestDatumGroup1"
        self.assertEqual(expected, actual)


class TestSerializerClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def test_set_serializer_method(self):
        """Test _set_serialize_method
        using DatumObjectSerializer.serial_element_name_value
        """
        from app.datum.serializers import DatumObjectSerializer

        test_serializer = Serializer(data={},
                                     serializer="datum.DatumObjectSerializer.serial_element_name_value"
                                     )
        actual = test_serializer._set_serializer_method()
        expected = DatumObjectSerializer.serial_element_name_value
        self.assertEqual(expected, actual)

    def test_serialize_queryset(self):
        """Test serialize method
        using DatumObjectSerializer.serial_element_name_value
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_queryset = DatumObject.objects.all()
        test_data = Serializer(data=test_queryset,
                               serializer=DatumObjectSerializer.serial_element_name_value
                               ).serialize()

        actual_count = len(test_data)
        expected_count = 1
        self.assertEqual(expected_count, actual_count)

    def test_serialize_instance(self):
        """Test serialize method
        using DatumObjectSerializer.serial_element_name_value
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_object = DatumObject.objects.first()
        test_data = Serializer(data=test_object,
                               serializer=DatumObjectSerializer.serial_element_name_value
                               ).serialize()

        actual = test_data["name"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)

    def test_format_serialize_json(self):
        """Test _format_output method
        with json
        """
        test_data = {"test_string": "string", "test_number": 5}
        test_serializer = Serializer(data=test_data,
                                     serializer="",
                                     format="json"
                                     )
        test_json = test_serializer._format_output(test_data)
        actual = type(test_json)
        expected = str
        self.assertEqual(expected, actual)
        json.loads(test_json)

    def test_add_pk_key(self):
        """Test _add_pk_key method
        """
        test_object = self.test.datum_group1
        test_output = {"test_key": "test_value"}
        test_serializer = Serializer(data=test_output,
                                     serializer="",
                                     add_pk_key=True
                                     )
        test_pk_key = test_serializer._add_pk_key(test_object, test_output)
        actual = test_pk_key.keys()
        expected = self.test.datum_group1.datum_group_id
        self.assertIn(expected, actual)

    def test_serialize_one(self):
        """Test _serialize_one method
        using DatumObjectSerializer.serial_element_name_value
        """
        from app.datum.serializers import DatumObjectSerializer

        test_object = self.test.datum_object1
        test_serializer = Serializer(data=test_object,
                                     serializer=DatumObjectSerializer.serial_element_name_value,
                                     add_pk_key=True
                                     )
        test_data = test_serializer._serialize_one(
            test_object,
            DatumObjectSerializer.serial_element_name_value)
        actual = test_data[self.test.datum_object1.datum_object_id]["name"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)
