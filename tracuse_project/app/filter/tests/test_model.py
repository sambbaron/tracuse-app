from django.test import TestCase
from django.core.management import call_command

from model_mommy import mommy

from .test_data_filters import TestFilterSets
from ..models import FilterSet


class TestModelFilter(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("loaddata", "app/filter/tests/test_data_fixture.json")
        cls.test = TestFilterSets()

    def test_run_filter_set1(self):
        """Test
        """
        test_filter_set = FilterSet()
        actual = test_filter_set.run_filter_from_dict(**self.test.filter_set1)
        expected = {12}
        self.assertEqual(expected, actual)
