import unittest
from services.heuristics import DistanceHeuristics


class TestDistanceHeuristics(unittest.TestCase):
    def setUp(self):
        self.distance_heuristic_test = DistanceHeuristics()

    def test_get_keyboard_coordinates(self):
        character = "m"
        output = self.distance_heuristic_test.get_keyboard_coordinates(
            character)
        wanted_answer = (2, 6)
        self.assertEqual(output, wanted_answer)

    def test_calculate_keyboard_distance_for_characters_same(self):
        wanted_character_1 = "g"
        wanted_character_2 = "g"
        output = self.distance_heuristic_test.calculate_keyboard_distance_for_characters(
            wanted_character_1, wanted_character_2)
        wanted_answer = 0
        self.assertEqual(output, wanted_answer)

    def test_calculate_keyboard_distance_for_characters_diagonal(self):
        wanted_character_1 = "j"
        wanted_character_2 = "n"
        output = self.distance_heuristic_test.calculate_keyboard_distance_for_characters(
            wanted_character_1, wanted_character_2)
        wanted_answer = 1
        self.assertEqual(output, wanted_answer)

    def test_calculate_keyboard_distance_for_characters_far(self):
        wanted_character_1 = "z"
        wanted_character_2 = "p"
        output = self.distance_heuristic_test.calculate_keyboard_distance_for_characters(
            wanted_character_1, wanted_character_2)
        wanted_answer = 9.219544457
        self.assertAlmostEqual(output, wanted_answer)

    def test_calculate_all_distances_between_characters(self):
        output = self.distance_heuristic_test.calculate_all_distances_between_characters()
        wanted_answer = 26*25
        self.assertEqual(len(output), wanted_answer)

    def test_median_for_all_keyboard_distances(self):
        output = self.distance_heuristic_test.median_for_all_keyboard_distances()
        wanted_answer = 3
        self.assertEqual(output, wanted_answer)

    def test_calculate_distance_heuristic_for_characters_keyboard_only_same_character(self):
        character_1 = "a"
        character_2 = "a"
        output = self.distance_heuristic_test.calculate_distance_heuristic_for_characters_keyboard_only(
            character_1, character_2)
        wanted_answer = 0
        self.assertEqual(output, wanted_answer)

    def test_calculate_distance_heuristic_for_characters_keyboard_only_diagonal(self):
        character_1 = "c"
        character_2 = "f"
        output = self.distance_heuristic_test.calculate_distance_heuristic_for_characters_keyboard_only(
            character_1, character_2)
        wanted_answer = 0.3333333
        self.assertAlmostEqual(output, wanted_answer)

    def test_calculate_distance_heuristic_for_characters_keyboard_only_long(self):
        character_1 = "a"
        character_2 = "p"
        output = self.distance_heuristic_test.calculate_distance_heuristic_for_characters_keyboard_only(
            character_1, character_2)
        wanted_answer = 3.018461712
        self.assertAlmostEqual(output, wanted_answer)
