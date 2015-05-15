from django.test import TestCase, RequestFactory

from .test_data import TestDataCommon

class TestApiCommon(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataCommon()

    def setUp(self):
        self.factory = RequestFactory()
        # self.user = User.objects.create_user(
        #     username='jacob', email='jacob@…', password='top_secret')

    def test_datum_groups_get(self):
        from .api import datum_groups_get
        request = self.factory.get('/app/datum_groups')
        response = datum_groups_get(request)
        self.assertEqual(response.status_code, 200)