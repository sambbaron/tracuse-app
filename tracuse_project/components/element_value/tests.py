from django.test import TestCase

from fixtures.test_data_simple import TestDataSimple

from components.element_value.models import ElementValueModel, ElementValueString


class TestModelElementValueModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def test_init(self):
        """Test ElementValueModel.__init__
        with data type name
        """
        actual = ElementValueModel("String")
        expected = ElementValueString
        self.assertEqual(expected, actual)
