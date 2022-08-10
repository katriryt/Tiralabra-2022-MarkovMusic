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

    def test_convert_user_input_as_list(self):
        user_input = "Mom! BUI123 sur.prise"
        output = self.check_spelling.convert_user_input_as_list(user_input)
        wanted_answer = ["mom", "bui123", "sur", "prise"]
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

    def test_calculate_levenshtein_distance_words_same_length(self):
        test_user_word = "intention"
        test_dictionary_word = "execution"
        output = self.check_spelling.calculate_levenshtein_distance(
            test_user_word, test_dictionary_word)
        wanted_answer = 5
        self.assertEqual(output, wanted_answer)

    def test_calculate_levenshtein_distance_words_different_length(self):
        test_user_word = "sunday"
        test_dictionary_word = "saturday"
        output = self.check_spelling.calculate_levenshtein_distance(
            test_user_word, test_dictionary_word)
        wanted_answer = 3
        self.assertEqual(output, wanted_answer)

    def test_calculate_optimal_string_alignment_distance(self):
        test_user_word = "a_cat"
        test_dictionary_word = "an_act"
        output = self.check_spelling.calculate_optimal_string_alignment_distance(
            test_user_word, test_dictionary_word)
        wanted_answer = 2
        self.assertEqual(output, wanted_answer)

    def test_calculate_damerau_levenshtein_distance(self):
        test_user_word = "a_cat"
        test_dictionary_word = "an_act"
        output = self.check_spelling.calculate_damerau_levenshtein_distance(
            test_user_word, test_dictionary_word)
        wanted_answer = 2
        self.assertEqual(output, wanted_answer)

    def test_generate_damerau_levenshtein_distance_differs_optimal_string(self):
        test_user_word = "ca"
        test_dictionary_word = "abc"
        output_osa = self.check_spelling.calculate_optimal_string_alignment_distance(
            test_user_word, test_dictionary_word)
        output_dl = self.check_spelling.calculate_damerau_levenshtein_distance(
            test_user_word, test_dictionary_word)
        self.assertEqual((output_osa, output_dl), (3, 2))
