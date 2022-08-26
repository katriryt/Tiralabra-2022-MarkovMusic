from distutils.cygwinccompiler import Mingw32CCompiler
import unittest
from services.spell_check import SpellCheck


class TestSpellCheck(unittest.TestCase):
    def setUp(self):
        self.check_spelling = SpellCheck()

    def test_word_contains_only_english_characters_true(self):
        test_word = "mwm"
        output = self.check_spelling.word_contains_only_english_characters(
            test_word)
        self.assertTrue(output)

    def test_word_contains_only_english_characters_false(self):
        test_word = "mäm"
        output = self.check_spelling.word_contains_only_english_characters(
            test_word)
        self.assertFalse(output)

    def test_convert_original_user_input_as_list(self):
        user_input = "Mom! BUI123 sur.prise"
        output = self.check_spelling.convert_original_user_input_as_list(
            user_input)
        wanted_answer = ["Mom!", "BUI123", "sur.prise"]
        self.assertEqual(output, wanted_answer)

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
        self.assertTrue(output)

    def test_is_word_english_false(self):
        user_input = "nomimono"
        output = self.check_spelling.is_word_english(user_input)
        self.assertFalse(output)

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

    def test_calculate_levenshtein_distance_weighting_used(self):
        test_user_word_1 = "hiuse"
        test_user_word_2 = "hquse"
        test_dictionary_word = "house"
        weighting_used = True
        output_1 = self.check_spelling.calculate_levenshtein_distance(
            test_user_word_1, test_dictionary_word, weighting_used)
        output_2 = self.check_spelling.calculate_levenshtein_distance(
            test_user_word_2, test_dictionary_word, weighting_used)
        self.assertTrue(output_1 < output_2)

    def test_suggest_words_based_on_distance(self):
        test_word = "mwm"
        test_weighting_used = True
        output_levenshtein = self.check_spelling.suggest_words_based_on_distance(
            test_word, 1, test_weighting_used)
        output_osa = self.check_spelling.suggest_words_based_on_distance(
            test_word, 2, test_weighting_used)
        output_damerau_leven = self.check_spelling.suggest_words_based_on_distance(
            test_word, 3, test_weighting_used)
        answer = [len(output_levenshtein), len(
            output_osa), len(output_levenshtein)]
        wanted_number_of_suggestions = [10, 10, 10]
        self.assertEqual(answer, wanted_number_of_suggestions)
