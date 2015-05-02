from django.test import TestCase

from fixtures.test_data_simple import TestDataSimple


class TestModelElementTypeDatumType(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataSimple()

    def test_str(self):
        """Test ElementTypeDatumType.__str__ property"""
        actual = self.test.element_type_datum_type1.__str__()
        expected = "Test Datum Type - Test Element Type1"
        self.assertEqual(expected, actual)


# Test that there is an element value table for each element data type