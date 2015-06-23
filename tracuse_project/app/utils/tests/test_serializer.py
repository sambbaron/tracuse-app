import json

from django.test import TestCase
from common.tests.test_data import TestDataCommon
from utils.serializer import Serializer


class TestUtilsSerializerClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def test_serialize_encode_json(self):
        """Test _format_output method
        with json
        """
        test_data = {"test_string": "string", "test_number": 5}
        test_serializer = Serializer()
        test_json = test_serializer.encode("json", test_data)
        actual = type(test_json)
        expected = str
        self.assertEqual(expected, actual)
        json.loads(test_json)

    def test_serialize_queryset(self):
        """Test serialize method
        using DatumObjectSerializer.serial_default
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_queryset = DatumObject.objects.all()
        test_data = DatumObjectSerializer("serial_default"
                                          ).serialize(test_queryset)

        actual_count = len(test_data)
        expected_count = 1
        self.assertEqual(expected_count, actual_count)

    def test_serialize_instance(self):
        """Test serialize method
        using DatumObjectSerializer.serial_default
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_object = DatumObject.objects.first()
        test_data = DatumObjectSerializer("serial_default"
                                          ).serialize(test_object)

        actual = test_data["datum_type_id"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)

    def test_serialize_instance_object_wrap_pk(self):
        """Test serialize method
        using DatumObjectSerializer.serial_default
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_object = DatumObject.objects.first()
        test_data = DatumObjectSerializer("serial_default"
                                          ).serialize(test_object, object_wrap_pk=True)

        actual = test_data[test_object.pk]["datum_type_id"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)

    def test_serialize_queryset_object_wrap_pk(self):
        """Test serialize method
        using DatumObjectSerializer.serial_default
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_queryset = DatumObject.objects.all()
        test_data = DatumObjectSerializer("serial_default"
                                          ).serialize(test_queryset, object_wrap_pk=True)

        actual_count = len(test_data)
        expected_count = 1
        self.assertEqual(expected_count, actual_count)

        actual = test_data[test_queryset.first().pk]["datum_type_id"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)

    # def test_deserialize_success(self):
    #     """Test deserialize method
    #     """
    #     from app.datum.serializers import DatumGroupSerializer
    #
    #     test_update = {
    #
    #     }
    #     test_data = DatumGroupSerializer(data=test_queryset,
    #                                      "serial_default",
    #                                      object_wrap_pk=True
    #                                      ).serialize()
    #
    # def test_deserialize_failure_bad_field(self):
    #     """Test deserialize with field not in model
    #     """
    #     field_list = [("badfield",)]
    #     data = {"sort": 99}
    #     expected = "'badfield' not a valid field"
    #     actual = model.deserialize(self.test_model, field_list, data)
    #     self.assertEqual(expected, actual)
    #     self.assertEqual(self.test_model.sort, 10)
    #
    # def test_deserialize_failure_field_not_data(self):
    #     """Test deserialize with field not in data
    #     """
    #     field_list = [("sort",)]
    #     data = {"badfield": 99}
    #     expected = "'sort' not in data request"
    #     actual = model.deserialize(self.test_model, field_list, data)
    #     self.assertEqual(expected, actual)
    #     self.assertEqual(self.test_model.sort, 10)
