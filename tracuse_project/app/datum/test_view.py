import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from .test_data import TestDataDatum


class TestApiCommon(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_datum_groups_get(self):
        """Test DatumObjectList.get api"""
        from .views import DatumObjectList

        request = self.factory.get('/api/datum_objects')
        force_authenticate(request, user=self.test.user1)

        response = DatumObjectList.as_view()(request)
        response.render()
        response_content = json.loads(response.content.decode())

        response_type = len(response_content)
        expected_type = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_type, response_type)

    def test_datum_groups_post(self):
        """Test DatumObjectList.post api"""
        from .views import DatumObjectList

        test_object = self.test.datum_object1
        test_object_data = {"datum_type": test_object.datum_type_id}
        request = self.factory.post('/api/datum_objects', data=test_object_data, format="json")
        force_authenticate(request, user=self.test.user1)

        response = DatumObjectList.as_view()(request)
        response.render()
        response_content = json.loads(response.content.decode())

        response_type = response_content["datum_type"]
        expected_type = self.test.datum_type1.pk
        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_type, response_type)
