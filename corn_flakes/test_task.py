from unittest import TestCase
from morning_task import separate_letters
from morning_task import get_character_count


class TestTask(TestCase):

    def test_task(self):
        sample = "google"
        assert {'g': 2, 'o': 2, 'l': 1, 'e': 1} == separate_letters(sample)

    def test_task2(self):
        sample = "goog le"
        assert {'g': 2, 'o': 2, 'l': 1, 'e': 1} == separate_letters(sample)

    def test_that_character_count_function_exit(self):
        get_character_count("awe")
