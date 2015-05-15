import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataCommon

class TestApiCommon(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def setUp(self):
        self.factory = RequestFactory()

    def test_datum_groups_get(self):
        """Test datum_groups_get api"""
        from .api import datum_groups_get
        request = self.factory.get('/app/datum_groups')
        request.user = self.test.user1
        response = datum_groups_get(request)
        response_content = json.loads(response.content.decode())
        response_count = len(response_content["datum_group"])
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
        
    def test_datum_types_get(self):
        """Test datum_types_get api"""
        from .api import datum_types_get
        request = self.factory.get('/app/datum_types')
        request.user = self.test.user1
        response = datum_types_get(request)
        response_content = json.loads(response.content.decode())
        response_count = len(response_content["datum_type"])
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
           
    def test_datum_objects_get(self):
        """Test datum_objects_get api"""
        from .api import datum_objects_get
        request = self.factory.get('/app/datum_objects')
        request.user = self.test.user1
        response = datum_objects_get(request)
        response_content = json.loads(response.content.decode())
        response_count = len(response_content["datum_object"])
        expected_count = 1
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)

