import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataDatum
from .. import views


class TestDatumGroupAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumGroupAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumGroupAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestDatumTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumTypeAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumTypeAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestDatumObjectAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumObjectAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumObjectAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)

    def test_post_success(self):
        """Test DatumObjectAll.post api
        success
        """
        new_datum = {
            "datum_type_id": self.test.datum_type1.datum_type_id
        }
        request = self.factory.post("",
                                    data=json.dumps(new_datum),
                                    content_type="application/json"
                                    )
        request.user = self.test.user1

        view = views.DatumObjectAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        actual_content = response_content["datum_type_id"]
        expected_content = self.test.datum_type1.datum_type_id
        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_content, actual_content)

    def test_post_failure(self):
        """Test DatumObjectAll.post api
        failure - bad request content format
        """
        new_datum = {
            "datum_tyXpe_id": self.test.datum_type1.datum_type_id
        }
        request = self.factory.post("",
                                    data=json.dumps(new_datum),
                                    content_type="application/json"
                                    )
        request.user = self.test.user1

        view = views.DatumObjectAll(request=request)
        response = view.dispatch(request=request)

        actual_content = json.loads(response.content.decode())
        expected_content = "'datum_type_id' not in data request"
        self.assertEqual(response.status_code, 400)
        self.assertEqual(expected_content, actual_content)


class TestDatumObjectOne(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumObjectOne.get api"""
        request_id = self.test.datum_object1.datum_object_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumObjectOne(request=request)
        response = view.dispatch(request=request, pk=request_id)

        response_content = json.loads(response.content.decode())
        response_actual = response_content["headline"]
        expected_actual = "Test Object Name"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_actual, response_actual)
