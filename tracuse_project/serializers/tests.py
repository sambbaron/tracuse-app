# import os
# import json
#
# from unittest import skip
# from django.test import TestCase
#
# from django.conf import settings
# from django.core import serializers
#
# from components.datum.models import DatumType
#
#
# class TestSerializers(TestCase):
#     """Test custom serializers"""
#
#     class_setup = False
#
#     def setUp(self):
#         if not self.class_setup:
#             fixture_path = self.fixture_path("test_serializers.json")
#             deserialized_data = self.deserialize_fixture(fixture_path)
#             self.deserialize_to_db(deserialized_data)
#
#     def fixture_path(self, fixture_name):
#         return os.path.join(settings.FIXTURE_DIRS[0], fixture_name)
#
#     def deserialize_fixture(self, fixture_path):
#         fixture_path = self.fixture_path("test_serializers.json")
#         with open(fixture_path, "r") as f:
#             fixture_data = f.read()
#         return serializers.deserialize(format="json",
#                                        stream_or_string=fixture_data)
#
#     def deserialize_to_db(self, deserialized_data):
#         for obj in deserialized_data:
#             obj.save()
#
#     @skip("Error in test json with old DatumType schema")
#     def test_myjsonflat_serialize(self):
#         """Test myjsonflat serializer format using
#         sample DatumType data in Django json format
#         """
#
#         test_queryset = DatumType.objects.all()
#         actual_json = serializers.serialize(format="myjsonflat",
#                                             queryset=test_queryset
#                                             )
#
#         expected_file = self.fixture_path("test_expected.json")
#         with open(expected_file, "r") as f:
#             expected_json = json.loads(f.read())
#
#         return self.assertJSONEqual(actual_json, expected_json)