from django.test import TestCase, mock

from .test_data import TestDataElement


class TestModelElementOption(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_sort_parts(self):
        """Test ElementOption.sort_parts property"""
        actual = self.test.element_option1.sort_parts
        expected = [self.test.element_type1.sort]
        self.assertEqual(expected, actual)


class TestModelElementDatumType(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_str(self):
        """Test ElementDatumType.__str__ property"""
        actual = self.test.element_datum_type1.__str__()
        expected = self.test.element_datum_type1.readable_name
        self.assertEqual(expected, actual)

    def test_entity_name_default(self):
        test_object = self.test.element_datum_type1
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.entity_name
        expected = "TestDatumType1Name"
        self.assertEqual(expected, actual)

    def test_entity_name_input(self):
        test_object = self.test.element_datum_type1
        test_object.entity_name = "custom_entity_name"
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.entity_name
        expected = "custom_entity_name"
        self.assertEqual(expected, actual)

    def test_readable_name_default(self):
        test_object = self.test.element_datum_type1
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.readable_name
        expected = "Test Datum Type1 - Name"
        self.assertEqual(expected, actual)

    def test_readable_name_input(self):
        test_object = self.test.element_datum_type1
        test_object.readable_name = "Custom Readable Name"
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.readable_name
        expected = "Custom Readable Name"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_default(self):
        test_object = self.test.element_datum_type1
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.readable_plural_name
        expected = "Test Datum Type1s - Names"
        self.assertEqual(expected, actual)

    def test_readable_plural_name_input(self):
        test_object = self.test.element_datum_type1
        test_object.readable_plural_name = "Custom Readable Plural Name"
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.readable_plural_name
        expected = "Custom Readable Plural Name"
        self.assertEqual(expected, actual)

    def test_schema_name_default(self):
        test_object = self.test.element_datum_type1
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.schema_name
        expected = "test_datum_type1_name"
        self.assertEqual(expected, actual)

    def test_schema_name_input(self):
        test_object = self.test.element_datum_type1
        test_object.schema_name = "custom_schema_name"
        with mock.patch("common.models.BaseModel.save"):
            test_object.save()

        actual = test_object.schema_name
        expected = "custom_schema_name"
        self.assertEqual(expected, actual)


class TestModelElementDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test = TestDataElement()

    def test_str(self):
        """Test ElementDatumObject.__str__ property"""
        actual = self.test.element_datum_object1.__str__()
        expected = "Test Object Name - Name"
        self.assertEqual(expected, actual)

    def test_element_datum_type(self):
        """Test ElementDatumObject.element_datum_type property"""
        actual = self.test.element_datum_object1.element_datum_type
        expected = self.test.element_datum_type1
        self.assertEqual(expected, actual)

    def test_calculated_value(self):
        """Test ElementDatumObject.calculated_value method"""
        actual = self.test.element_datum_object3.calculated_value()
        expected = "Test Object Name Test Object Description"
        self.assertEqual(expected, actual)