from django.test import TestCase

from .test_data import TestDataTracuser

from ..serializers import TracuserLandingSerializer


class TestTracuserLandingSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataTracuser()

    def test_serial_default(self):
        """Test TracuserLandingSerializer.serial_default
        """
        test_object = self.test.landing1
        test_serialized = TracuserLandingSerializer \
            ("serial_default").serialize(test_object)
        actual = test_serialized["name"]
        expected = "TestUser1"
        self.assertEqual(expected, actual)
