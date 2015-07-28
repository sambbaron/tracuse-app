import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataWindowuse
from .. import views


class TestWindowuseObjectAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test WindowuseObjectAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.WindowuseObjectAll(request=request)
        response = view.dispatch(request=request)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestWindowuseObjectOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test WindowuseObjectOne.get api"""
        request_id = self.test.windowuse_object1.windowuse_object_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.WindowuseObjectOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_actual = response_content["title"]
        expected_actual = "Windowuse 1 Title"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_actual, response_actual)

    def test_put(self):
        """Test WindowuseObjectOne.put success"""
        request_id = self.test.windowuse_object1.windowuse_object_id
        request_data = json.dumps({
            "title": self.test.windowuse_object1.title,
            "description": self.test.windowuse_object1.description,
            "datum_filter": '{"TestFilter1": "Change Filter"}'
        })
        request = self.factory.put("", request_data, "application/json")
        request.user = self.test.user1

        view = views.WindowuseObjectOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        actual_response = response_content["datum_filter"]
        expected_response = '{"TestFilter1": "Change Filter"}'
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, actual_response)


class TestWindowuseViewuseAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test WindowuseViewuseAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.WindowuseViewuseAll(request=request)
        response = view.dispatch(request=request)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestWindowuseViewuseOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataWindowuse()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test WindowuseViewuseOne.get api"""
        request_id = self.test.windowuse_viewuse1.windowuse_viewuse_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.WindowuseViewuseOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_actual = response_content["windowuse_object_id"]
        expected_actual = self.test.windowuse_object1.windowuse_object_id
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_actual, response_actual)

    def test_put(self):
        """Test WindowuseViewuseOne.put success"""
        request_id = self.test.windowuse_viewuse1.windowuse_viewuse_id
        request_data = json.dumps({
            "sort": self.test.windowuse_viewuse1.sort,
            "active": self.test.windowuse_viewuse1.active,
            "windowuse_object_id": self.test.windowuse_object2.windowuse_object_id,
            "viewuse_object_id": self.test.windowuse_viewuse1.viewuse_object_id,
        })
        request = self.factory.put("", request_data, "application/json")
        request.user = self.test.user1

        view = views.WindowuseViewuseOne(request=request)
        response = view.dispatch(request=request, pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        actual_response = response_content["windowuse_object_id"]
        expected_response = self.test.windowuse_object2.windowuse_object_id
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_response, actual_response)
