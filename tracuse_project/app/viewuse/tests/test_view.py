import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataViewuse
from .. import views


class TestViewuseObjectAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ViewuseObjectAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.ViewuseObjectAll(request=request)
        response = view.dispatch(request=request)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestViewuseObjectOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ViewuseObjectOne.get api"""
        request_id = self.test.viewuse_object1.viewuse_object_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.ViewuseObjectOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_actual = response_content["title"]
        expected_actual = "Viewuse 1 Title"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_actual, response_actual)

    def test_put(self):
        """Test ViewuseObjectOne.put success"""
        request_id = self.test.viewuse_object1.viewuse_object_id
        request_data = json.dumps({
            "title": "Change Viewuse Title",
            "description": self.test.viewuse_object1.description,
            "datum_filter": self.test.viewuse_object1.datum_filter,
            "viewuse_arrangement_id": self.test.viewuse_object1.viewuse_arrangement_id
        })
        request = self.factory.put("", request_data, "application/json")
        request.user = self.test.user1

        view = views.ViewuseObjectOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        actual_response = response_content["title"]
        expected_response = "Change Viewuse Title"
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, actual_response)


class TestViewuseArrangementAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataViewuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ViewuseArrangementAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.ViewuseArrangementAll(request=request)
        response = view.dispatch(request=request)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
