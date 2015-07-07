import json

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from .test_data import TestDataTracuser
from .. import views


class TestTracuserLandingAll(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataTracuser()

    def setUp(self):
        self.factory = RequestFactory()

    def test_post(self):
        """Test TracuserLandingAll.post api
        success
        """
        new_user = "name=TestUserPost&email=test_post%40test.com&comments="
        request = self.factory.post("",
                                    data=new_user,
                                    content_type="application/x-www-form-urlencoded")
        request.user = AnonymousUser()

        view = views.TracuserLandingAll(request=request)
        response = view.dispatch(request=request)

        response_content = json.loads(response.content.decode())
        actual_content = response_content["name"]
        expected_content = "TestUserPost"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_content, actual_content)
