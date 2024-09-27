from unittest import TestCase

from corn_flakes.corn_flakes2 import biggest_odd, biggest_odd2
from corn_flakes.corn_flakes3 import compare_string
from corn_flakes.task import comma_separate





class Test_Corn_Flask(TestCase):

    def test_biggest_odd(self):
        numbers = '23956'
        self.assertEqual(biggest_odd(numbers), 9)

    def test_biggest_odd2(self):
        numbers = '23956'
        self.assertEqual(biggest_odd2(numbers), 9)

    def test_compare_string(self):
        string1 = 'love'
        string2 = 'evol'
        self.assertEqual(compare_string(string1, string2), True)

    def test_compare_string2(self):
        string1 = 'abcde'
        string2 = 'world'
        self.assertEqual(compare_string(string1, string2), False)

    def test_compare_string3(self):
        string1 = 'abcde'
        string2 = 'edcba'
        self.assertEqual(compare_string(string1, string2), True)

    def test_To_Seperate_using_comma(self):
        inputs = 34, 67, 55, 33, 12, 98
        result = ['34', '67', '55', '33', '12', '98']
        result2 = ['34', '67', '55', '33', '12', '98']
        self.assertEqual(comma_separate(inputs), result, result2)

