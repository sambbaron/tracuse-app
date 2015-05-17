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
        test_id = test_object.pk
        test_serialized = ElementDatumObjectSerializer. \
            serial_ids_value(test_object)
        properties = test_serialized[test_id]
        actual = properties["element_value"]
        expected = "Test Object Name"
        self.assertEqual(expected, actual)
