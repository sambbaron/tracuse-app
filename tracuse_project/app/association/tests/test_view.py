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
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 3
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestDatumAssociationParent(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumAssociationParent.get api"""
        request_id = self.test.datum_object4.datum_object_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumAssociationParent(request=request)
        response = view.dispatch(request=request, datum_pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 4
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)


class TestDatumAssociationChild(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataAssociation()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        """Test DatumAssociationChild.get api"""
        request_id = self.test.datum_object1.datum_object_id
        request = self.factory.get("")
        request.user = self.test.user1

        view = views.DatumAssociationChild(request=request)
        response = view.dispatch(request=request, datum_pk=request_id)
        try:
            response_content = json.loads(response.content.decode())
        except:
            raise Exception(response.content.decode())

        response_count = len(response_content)
        expected_count = 7
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_count, response_count)
