import os
from unittest import TestCase, mock

from mock_django.query import QuerySetMock

from django.conf import settings
from django.core import serializers
from django.db.models import QuerySet

from components.datum.models import DatumType


class TestSerializers(TestCase):
    """Test custom serializers"""

    def fixture_path(self, fixture_name):
        return os.path.join(settings.FIXTURE_DIRS[0], fixture_name)

    def test_myjsonflat(self):
        """Test myjsonflat serializer format using
        sample DatumType data in Django json format
        """

        fixture_path = self.fixture_path("test_serializers.json")
        with open(fixture_path, "r") as f:
            fixture_data = f.read()
        deserialized_data = serializers.deserialize(format="json",
                                                    stream_or_string=fixture_data)

        # with mock.patch("django.db.models.QuerySet") as mock_queryset:


        fixture_objects = []
        for obj in deserialized_data:
            with mock.patch("components.datum.models.DatumType") as mock_object:
                mock_object = obj.object
                # mock_object._meta = DatumType._meta
                fixture_objects.append(mock_object)

        mock_queryset = QuerySetMock(DatumType, *fixture_objects)
        mock_queryset.model = DatumType

        expected_string = ""
        actual = serializers.serialize(format="myjsonflat",
                                       queryset=mock_queryset
                                       )
        expected = expected_string

        fixture_path = settings.FIXTURE_DIRS[0] + "\\test_results.json"
        with open(fixture_path, "w") as f:
            f.write(actual)

        return self.assertEqual(expected, actual)