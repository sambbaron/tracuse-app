import json

from django.test import TestCase, RequestFactory

from .test_data import TestDataUiObject
from .. import views


class TestUiArrangementTypeAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataUiObject()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test UiArrangementTypeAll.get api"""
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.UiArrangementTypeAll(request=request)
        response = view.dispatch(request=request)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 2
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)

