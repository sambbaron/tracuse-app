import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataElement
from .. import views


class TestElementTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ElementTypeAll.get api"""
        request = self.factory.get('/api/element_types/')
        request.user = self.test.user1

        view = views.ElementTypeAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestElementDatumTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ElementDatumTypeAll.get api"""
        request = self.factory.get('/api/element_datum_types/')
        request.user = self.test.user1

        view = views.ElementDatumTypeAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestElementDatumObjectAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ElementDatumObjectAll.get api"""
        request = self.factory.get('/api/element_datum_objects/')
        request.user = self.test.user1

        view = views.ElementDatumObjectAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestElementDatumObjectOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def setUp(self):
        self.factory = RequestFactory()

    def test_put(self):
        """Test ElementDatumObjectOne.put api"""
        test_object = self.test.element_datum_object1
        test_pk = test_object.pk
        test_data = json.dumps({"element_value": "Change Name"})
        test_path = "/api/element_datum_object/{}/".format(test_pk)

        request = self.factory.put(
            test_path,
            test_data,
            "application/json"
        )
        request.user = self.test.user1

        view = views.ElementDatumObjectOne(request=request)
        response = view.dispatch(request=request, pk=test_pk)
        response_content = json.loads(response.content.decode())

        actual_response = response_content["element_value"]
        expected_response = "Change Name"
        self.assertEqual(expected_response, actual_response)
