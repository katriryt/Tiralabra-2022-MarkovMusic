import math
import string
import statistics


class DistanceHeuristics:
    """Class provides methods to calculate distance heuristic between two
    characters in a keyboard.
    """

    def __init__(self):
        """Method sets up basic assumptions for the distance heuristic calculations,
        incl. QWERTY US keyboard (only for alphabets).

        """
        self.keyboard_matrix = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                                ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                                ["z", "x", "c", "v", "b", "n", "m"]]

        self.all_distances = self.calculate_all_distances_between_characters()
        self.median_for_distances = self.median_for_all_keyboard_distances()

    def get_keyboard_coordinates(self, wanted_character):
        """Method returns coordinates in the keyboard matrix for one requested character.

        Args:
            wanted_character (string): Character requested.
        """
        for row in range(0, len(self.keyboard_matrix)):
            for column in range(0, len(self.keyboard_matrix[row])):
                if self.keyboard_matrix[row][column] == wanted_character:
                    return(row, column)

    def calculate_keyboard_distance_for_characters(self, character_1, character_2):
        """Method calculates and returns the absolute distance in keyboard between
        two different characters.

        Args:
            character_1 (string): First character requested
            character_2 (string): Second character requested
        """
        coordinates_1 = self.get_keyboard_coordinates(character_1)
        coordinates_2 = self.get_keyboard_coordinates(character_2)

        if (abs(coordinates_1[0]-coordinates_2[0]) == 1
                and abs(coordinates_1[1]-coordinates_2[1]) == 1):
            keyboard_distance = 1

        else:
            keyboard_distance = math.sqrt(
                (coordinates_1[0]-coordinates_2[0])**2 + (coordinates_1[1]-coordinates_2[1])**2)

        return keyboard_distance

    def calculate_all_distances_between_characters(self):
        """Method returns the absolute distances in keyboard between all different characters
        as a list. It excludes the distances when they are zero, i.e. the characters are the same.
        """
        alphabet = string.ascii_lowercase

        all_distances = []
        for character_1 in alphabet:
            for character_2 in alphabet:
                if character_1 != character_2:
                    keyboard_distance = self.calculate_keyboard_distance_for_characters(
                        character_1, character_2)
                    all_distances.append(
                        (keyboard_distance, character_1, character_2))

        return all_distances

    def median_for_all_keyboard_distances(self):
        """Method calculates and returns median absolute distance between all different characters
        in the keyboard.
        """
        all_distances = self.calculate_all_distances_between_characters()
        only_distances = []
        for distance in all_distances:
            only_distances.append(distance[0])

        return statistics.median(only_distances)

    def calculate_distance_heuristic_for_characters_keyboard_only(self, character_1, character_2):
        """Method calculates and returns a distance heuristic between two characters.
        It only considers absolute keyboard distances between two characters, and makes them
        relative to each other.
        Args:
            character_1 (string): First character requested
            character_2 (string): Second character requested
        """
        absolute_distance = self.calculate_keyboard_distance_for_characters(
            character_1, character_2)
        distance_heuristic = absolute_distance / self.median_for_distances
        return distance_heuristic

    def distance_heuristic_always_the_same(self, character_1, character_2):
        """Irrespective of the physical distance of the keyboard characters,
        method always returns 0 if the characters are the same and 1 if they
        are different

        Args:
            character_1 (string): First character requested
            character_2 (string): Second character requested

        Returns:
            Integer: 0 is returned if characters are the same, and 1 if they are different.
        """
        if character_1 == character_2:
            return 0
        else:
            return 1


distance_heuristics = DistanceHeuristics()
