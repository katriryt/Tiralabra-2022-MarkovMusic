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

    def test_is_word_english_true(self):
        user_input = "mom"
        output = self.check_spelling.is_word_english(user_input)
        wanted_answer = True
        self.assertEqual(output, wanted_answer)

    def test_is_word_english_false(self):
        user_input = "nomimono"
        output = self.check_spelling.is_word_english(user_input)
        wanted_answer = False
        self.assertEqual(output, wanted_answer)

    def test_alternative_words_with_one_distance(self):
        user_input = "mom"
        output = len(
            self.check_spelling.alternative_words_with_one_distance(user_input))
        wanted_answer = 182
        self.assertEqual(output, wanted_answer)

    def test_alternative_words_in_english(self):
        user_input = "foret"
        output = len(
            self.check_spelling.alternative_words_in_english(user_input))
        wanted_answer = len(
            ['forest', 'fret', 'fore', 'fort', 'forget', 'floret', 'forte'])
        self.assertEqual(output, wanted_answer)
