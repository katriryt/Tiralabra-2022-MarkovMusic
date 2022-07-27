import unittest
from services.spell_check import SpellCheck


class TestSpellCheck(unittest.TestCase):
    def setUp(self):
        self.check_spelling = SpellCheck()

    def test_convert_user_input_as_list(self):
        user_input = "mom EATS food"
        output = self.check_spelling.convert_user_input_as_list(user_input)
        wanted_answer = ["mom", "eats", "food"]
        self.assertEqual(output, wanted_answer)

    def test_alternative_words_with_one_distance(self):
        user_input = "mom"
        output = len(
            self.check_spelling.alternative_words_with_one_distance(user_input))
        wanted_answer = 182
        self.assertEqual(output, wanted_answer)
