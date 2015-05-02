from django.test import TestCase

from model_mommy import mommy

from .models import DatumGroup, DatumType, DatumObject


class TestModelDatumObject(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.datum_group1 = mommy.make(DatumGroup,
                                      entity_name="TestGroup")
        cls.datum_type1 = mommy.make(DatumType,
                                     entity_name="TestType",
                                     datum_group=cls.datum_group1)
        cls.datum_object1 = mommy.make(DatumObject,
                                       datum_type=cls.datum_type1)

    def tearDown(self):
        pass


    def test_str_no_name(self):
        pass

    def test_str_has_name(self):
        pass

    def test_datum_group(self):
        """Test DatumObject.datum_group property"""
        actual = self.datum_object1.datum_group
        expected = self.datum_group1
        self.assertEqual(expected, actual)
