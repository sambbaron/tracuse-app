import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataDatum
from ..views import DatumObjectAll


class TestDatumObjectAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumObjectAll.get api"""
        request = self.factory.get('/api/datum_groups/')
        request.user = self.test.user1

        view = DatumObjectAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content["datum_object"])
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)

    def test_post_success(self):
        """Test DatumObjectAll.post api"""
        new_datum = {
                     "datum_type": self.test.datum_type1.datum_type_id
                     }
        request = self.factory.post('/api/datum_groups/',
                                    data=json.dumps(new_datum),
                                    content_type="application/json"
                                    )
        request.user = self.test.user1

        view = DatumObjectAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        actual_content = response_content["datum_type"]
        expected_content = self.test.datum_type1.datum_type_id
        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_content, actual_content)
