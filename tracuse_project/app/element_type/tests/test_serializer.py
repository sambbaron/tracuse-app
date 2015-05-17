from django.test import TestCase

from app.datum.tests.test_data import TestDataDatum

from ..serializers import ElementDatumObjectSerializer


class TestElementDatumObjectSerializer(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataDatum()

    def test_serial_ids_value(self):
        """Test ElementDatumObjectSerializer.serial_ids_value
        """
        test_object = self.test.element_datum_object1
        test_serialized = ElementDatumObjectSerializer. \
            serial_ids_value(test_object)
        actual = test_serialized["element_value"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)
