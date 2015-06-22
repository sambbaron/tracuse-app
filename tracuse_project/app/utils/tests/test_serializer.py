import json

from django.test import TestCase
from common.tests.test_data import TestDataCommon
from utils.serializer import Serializer


class TestUtilsSerializerClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def test_format_serialize_json(self):
        """Test _format_output method
        with json
        """
        test_data = {"test_string": "string", "test_number": 5}
        test_serializer = Serializer(data=test_data,
                                     template="",
                                     format="json"
                                     )
        test_json = test_serializer._format_output(test_data)
        actual = type(test_json)
        expected = str
        self.assertEqual(expected, actual)
        json.loads(test_json)

    def test_serialize_no_data(self):
        """Test serialize method
        with no data
        """
        from app.datum.serializers import DatumObjectSerializer

        test_serializer = DatumObjectSerializer(data=None,
                                                template="serial_default"
                                                )

        with self.assertRaisesMessage(ValueError, "Serializer has empty 'data' attribute"):
            test_serializer.serialize

    def test_serialize_queryset(self):
        """Test serialize method
        using DatumObjectSerializer.serial_default
        """
        from app.datum.models import DatumObject
        from app.datum.serializers import DatumObjectSerializer

        test_queryset = DatumObject.objects.all()
        test_data = DatumObjectSerializer(data=test_queryset,
                                          template="serial_default"
                                          ).serialize

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
        test_data = DatumObjectSerializer(data=test_object,
                                          template="serial_default"
                                          ).serialize

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
        test_data = DatumObjectSerializer(data=test_object,
                                          template="serial_default",
                                          object_wrap_pk=True
                                          ).serialize

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
        test_data = DatumObjectSerializer(data=test_queryset,
                                          template="serial_default",
                                          object_wrap_pk=True
                                          ).serialize

        actual_count = len(test_data)
        expected_count = 1
        self.assertEqual(expected_count, actual_count)

        actual = test_data[test_queryset.first().pk]["datum_type_id"]
        expected = self.test.datum_type1.datum_type_id
        self.assertEqual(expected, actual)
