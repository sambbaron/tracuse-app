import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataAssociation
from .. import views


class TestAssociationDirectionAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test AssociationDirectionAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.AssociationDirectionAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
