from django.test import TestCase
from django.core.management import call_command

from .test_data_filters import TestFilterSets
from .. import utils


class TestFilterSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("loaddata", "app/filter/tests/test_data_fixture.json")
        cls.test = TestFilterSets()

    def test_filter_set_user1(self):
        """Test single user rule"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_user1)
        self.assertEqual(22, len(test_filter))

    def test_filter_set_group1(self):
        """Test single group rule"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_group1)
        self.assertEqual(14, len(test_filter))
        self.assertTrue({1, 3, 8}.issubset(test_filter))

    def test_filter_set_group2(self):
        """Test two group rules with or conditional"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_group2)
        self.assertEqual(6, len(test_filter))
        self.assertTrue({12, 13, 20}.issubset(test_filter))

    def test_filter_set_type1(self):
        """Test single type rule"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_type1)
        self.assertEqual(3, len(test_filter))
        self.assertTrue({16, 17, 18}.issubset(test_filter))

    def test_filter_set_type2(self):
        """Test two type rules with and conditional - should return nothing"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_type2)
        self.assertEqual(0, len(test_filter))

    def test_filter_set_association1(self):
        """Test single association rule for child direction and no distance"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_association1)
        self.assertEqual(7, len(test_filter))
        self.assertTrue({3, 21, 6}.issubset(test_filter))

    def test_filter_set_association2(self):
        """Test single association rule for parent direction and distance limit"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_association2)
        self.assertEqual(5, len(test_filter))
        self.assertTrue({12, 13, 14}.issubset(test_filter))

    def test_filter_set_element1(self):
        """Test single element rule for string"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_element1)
        self.assertEqual(3, len(test_filter))
        self.assertTrue({6, 7, 11}.issubset(test_filter))
 
    def test_filter_set_element2(self):
        """Test single element rule for number"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_element2)
        self.assertEqual(1, len(test_filter))
        self.assertEqual({12}, test_filter)

    def test_filter_set_element3(self):
        """Test two element rules with string and number"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_element3)
        self.assertEqual(1, len(test_filter))
        self.assertEqual({13}, test_filter)

    def test_filter_set_data_type1(self):
        """Test single data type rule for string"""
        test_filter = utils.run_filter_from_dict(**self.test.filter_set_data_type1)
        self.assertEqual(2, len(test_filter))
        self.assertEqual({12, 25}, test_filter)
 