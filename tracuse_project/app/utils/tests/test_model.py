from django.test import TestCase
from model_mommy import mommy

from utils import model


class TestUtilsModel(TestCase):
    """Test model functions"""

    def setUp(self):
        self.test_model = mommy.make("datum.DatumGroup",
                                     entity_name="TestDatumGroup",
                                     sort=10
                                     )

    def tearDown(self):
        self.test_model.delete()

    def test_convert_field_data_boolean_false(self):
        """Test convert_field_data with boolean value
        """
        test_data = "false"
        test_type = "boolean"
        expected = False
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_boolean_true(self):
        """Test convert_field_data with boolean value
        """
        test_data = "true"
        test_type = "boolean"
        expected = True
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_integer_success(self):
        """Test convert_field_data with integer value
        """
        test_data = "9"
        test_type = "integer"
        expected = 9
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_integer_failure(self):
        """Test convert_field_data with integer value
        """
        test_data = "abc"
        test_type = "integer"
        expected = "err:'integer' data conversion failure"
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_convert_field_data_json(self):
        """Test convert_field_data with json value
        """
        test_data = {"Test": "Data"}
        test_type = "json"
        expected = '{"Test": "Data"}'
        actual = model.convert_field_data(test_data, test_type)
        self.assertEqual(expected, actual)

    def test_update_model_success_with_type(self):
        """Test update_model with explicit field data type
        """
        field_list = [("sort", "integer")]
        data = {"sort": 99}
        actual = model.update_model(self.test_model, field_list, data)
        self.assertEqual(self.test_model, actual)
        self.assertEqual(self.test_model.sort, 99)

    def test_update_model_success_without_type(self):
        """Test update_model with implicit field data type
        """
        field_list = [("sort",)]
        data = {"sort": 99}
        actual = model.update_model(self.test_model, field_list, data)
        self.assertEqual(self.test_model, actual)
        self.assertEqual(self.test_model.sort, 99)

    def test_update_model_failure_bad_field(self):
        """Test update_model with field not in model
        """
        field_list = [("badfield",)]
        data = {"sort": 99}
        expected = "'badfield' not a valid field"
        actual = model.update_model(self.test_model, field_list, data)
        self.assertEqual(expected, actual)
        self.assertEqual(self.test_model.sort, 10)

    def test_update_model_failure_field_not_data(self):
        """Test update_model with field not in data
        """
        field_list = [("sort",)]
        data = {"badfield": 99}
        expected = "'sort' not in data request"
        actual = model.update_model(self.test_model, field_list, data)
        self.assertEqual(expected, actual)
        self.assertEqual(self.test_model.sort, 10)

    def test_update_model_failure_data_conversion(self):
        """Test update_model with bad field data conversion
        """
        field_list = [("sort", "integer")]
        data = {"sort": "abc"}
        expected = "'integer' data conversion failure; Field: sort; Raw data: abc;"
        actual = model.update_model(self.test_model, field_list, data)
        self.assertEqual(expected, actual)
        self.assertEqual(self.test_model.sort, 10)
