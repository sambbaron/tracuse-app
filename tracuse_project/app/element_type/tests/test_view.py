import json

from django.test import TestCase, RequestFactory

from app.datum.tests.test_data import TestDataDatum
from .. import views


class TestElementTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ElementTypeAll.get api"""
        request = self.factory.get('/api/element_types/')
        request.user = self.test.user1

        view = views.ElementTypeAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content["element_type"])
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestElementDatumTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test ElementDatumTypeAll.get api"""
        request = self.factory.get('/api/element_datum_types/')
        request.user = self.test.user1

        view = views.ElementDatumTypeAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content["element_datum_type"])
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
