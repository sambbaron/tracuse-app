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

    def tearDown(self):
        pass


    def test_element_value(self):
        actual = ""
        expected = ""
        self.assertEqual(expected, actual)
