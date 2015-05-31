import json

from django.test import TestCase, RequestFactory
from django.core.management import call_command

from django.contrib.auth.models import User

from .test_data_filters import TestFilterSetsModel
from .. import views


class TestRunFilter(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("loaddata", "app/filter/tests/test_data_fixture.json")
        cls.test = TestFilterSetsModel()

    def setUp(self):
        self.factory = RequestFactory()

    def test_filter_from_json(self):
        """Test test filter_from_json api"""
        user = User.objects.get(pk=1)

        request_data = self.test.filter_set_dict1
        request = self.factory.post("/api/filter/json/",
                                    data=json.dumps(request_data),
                                    content_type="application/json"
                                    )
        request.user = user

        response = views.RunFilter.filter_from_json(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
        self.assertEqual([12, 13], response_content)

    def test_filter_from_set(self):
        """Test test filter_from_set api"""
        user = User.objects.get(pk=1)

        request_pk = self.test.filter_set1.filter_set_id
        request_path = "/api/filter/{}/".format(request_pk)
        request = self.factory.get(request_path)
        request.user = user

        response = views.RunFilter.filter_from_set(request=request,
                                                   pk=request_pk
                                                   )

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 14
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
        self.assertTrue({1, 3, 8}.issubset(response_content))