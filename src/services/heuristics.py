import math
import string
import statistics


class DistanceHeuristics:
    """Class provides methods to calculate distance heuristic between two
    characters in a keyboard (and later also between two words).
    """

    def __init__(self):
        """Method sets up basic assumptions for the distance heuristic calculations,
        incl. QQWERTY US keyboard (only for alphabets).

        """
        self.keyboard_matrix = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                                ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                                ["z", "x", "c", "v", "b", "n", "m"]]

    def get_keyboard_coordinates(self, wanted_character):
        """Method returns coordinates in the keyboard matrix for one requested character.

        Args:
            wanted_character (string): Character requested.
        """
        for row in range(0, len(self.keyboard_matrix)):
            for column in range(0, len(self.keyboard_matrix[row])):
                if self.keyboard_matrix[row][column] == wanted_character:
                    #                print(row, column)
                    return(row, column)

    def calculate_keyboard_distance_for_characters(self, character_1, character_2):
        """Method calculates and returns the absolute distance in keyboard between
        two different characters.

        Args:
            character_1 (string): First character requested
            character_2 (string): Second character requested
        """
    #    print(character_1, character_2)
        coordinates_1 = self.get_keyboard_coordinates(character_1)
        coordinates_2 = self.get_keyboard_coordinates(character_2)

    #    print(coordinates_1, coordinates_2)

        if (abs(coordinates_1[0]-coordinates_2[0]) == 1
            and abs(coordinates_1[1]-coordinates_2[1]) == 1):
            #        print("these are diagonally 1 distance away")
            keyboard_distance = 1

        else:
            #        print("these are not diagonally side by side")
            keyboard_distance = math.sqrt(
                (coordinates_1[0]-coordinates_2[0])**2 + (coordinates_1[1]-coordinates_2[1])**2)

        return keyboard_distance

    def calculate_all_distances_between_characters(self):
        """Method returns the absolute distances in keyboard between all different characters
        as a list. It excludes the distances when they are zero, i.e. the characters are the same.
        """
        alphabet = string.ascii_lowercase
        # print(alphabet)

        all_distances = []
        for character_1 in alphabet:
            for character_2 in alphabet:
                if character_1 != character_2:
                    keyboard_distance = self.calculate_keyboard_distance_for_characters(
                        character_1, character_2)
                    all_distances.append(
                        (keyboard_distance, character_1, character_2))

    #    print(all_distances)
        return all_distances

    def median_for_all_keyboard_distances(self):
        """Method calculates and returns median absolute distance between all different characters
        in the keyboard.
        """
        all_distances = self.calculate_all_distances_between_characters()
        only_distances = []
        for distance in all_distances:
            only_distances.append(distance[0])

#        print(only_distances)
    #    print(statistics.median(map(float, only_distances)))

        return statistics.median(only_distances)

    def calculate_distance_heuristic_for_characters_keyboard_only(self, character_1, character_2):
        """Method calculates and returns a distance heuristic between two characters.
        It only considers absolute keyboard distances between two characters, and makes them
        relative to each other.
        Args:
            character_1 (_type_): _description_
            character_2 (_type_): _description_
        """
        median_keyboard_distance = self.median_for_all_keyboard_distances()
#        print(median_keyboard_distance)
        absolute_distance = self.calculate_keyboard_distance_for_characters(
            character_1, character_2)
        distance_heuristic = absolute_distance / median_keyboard_distance
        return distance_heuristic
