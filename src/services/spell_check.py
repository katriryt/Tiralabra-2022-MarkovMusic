import string
import re
import numpy as np
from repositories.trie import trie as default_trie
from repositories.db_utilities import english_dictionary as default_english_dictionary
from services.heuristics import distance_heuristics as default_distance_heuristics


class SpellCheck:
    """Class provides core functionalities for spellchecking using different algorithms:
    suggesting words generated with one Damerau-Levenshtein distance, and by
    choosing between different words by calculating Levenshtein distance,
    optimal string alignment distance, and full Damerau-Levenshtein distance.
    """

    def __init__(self, trie=default_trie, dictionary=default_english_dictionary,
                 distance_heuristics=default_distance_heuristics):
        """Method initializes the spell checker, the related trie
            data structure, and the English dictionary.

            Args:
                trie (Class, optional): Trie data structure populated with English
                words. Defaults to default_trie.
                dictionary (Class, optional): Class opens data file with English
                dictionary and populates the trie structure. Defaults to default_english_dictionary.
        """

        self.trie = trie
        self.dictionary = dictionary
        self.distance_heuristics = distance_heuristics

    def word_contains_only_english_characters(self, user_input):
        """Method checks if the word contains only English characters.
        It returns False is there are any characters that are not in
        in the English alphabet, and True if all characters are in English alphabet.

        Args:
            user_input (string): Word from user

        Returns:
            Boolean: False if any character is not in English alphabet. True, if
            all characters are in English alphabet.
        """

        allowed_characters = string.ascii_lowercase
        for character in user_input:
            if character not in allowed_characters:
                return False
        return True

    def convert_original_user_input_as_list(self, user_input):
        """Method converts the given user input into a list of strings, 
        split based on empty spaces.

        Args:
            user_input (string): Input is one or multiple words in string format.

        Returns:
            list: Method returns a list of strings.
        """

        original_user_input_as_list = user_input.split()
        return original_user_input_as_list

    def convert_user_input_as_list(self, user_input):
        """Method converts given user input into a list of strings in lower case,
        splitting the user input to words at empty spaces and different punctuation marks.

        Args:
             user_input (string): Input is one or multiple words in string format.
        """

        user_input_as_list = re.findall(r"[\w']+", user_input.lower())
        return user_input_as_list

    def is_word_english(self, test_word):
        """Method returns whether the given word is English or not.

           Args:
                test_word (string): Word input by user (string).
            Returns:
                Boolean: Method returns whether the given word is English (True) or not (False).
        """

        return self.trie.search_if_word_in_trie(test_word)

    def alternative_words_with_one_distance(self, test_word):
        """For a given input_word, the method generates all the alternative words that
        are one Damerau-Levenhstein distance away.

        Args:
            input_word (string): A word written by the user (string).
        """

        alternative_words_generated = ""
        alternative_letters = "abcdefghijklmnopqrstuvwxyz"
        split_test_word = [(test_word[:i], test_word[i:])
                           for i in range(len(test_word) + 1)]
        deleting_characters = [split_left + split_right[1:]
                               for split_left, split_right in split_test_word if split_right]
        transposing_characters_in_split_words = [split_left + split_right[1] + split_right[0] +
                                                 split_right[2:] for split_left,
                                                 split_right in split_test_word
                                                 if len(split_right) > 1]
        replacing_characters_in_split_words = [split_left + character + split_right[1:]
                                               for split_left, split_right
                                               in split_test_word
                                               if split_right for character in alternative_letters]
        insert_characters_in_split_words = [split_left + character + split_right for split_left,
                                            split_right in split_test_word for character
                                            in alternative_letters]

        alternative_words_generated = set(deleting_characters +
                                          transposing_characters_in_split_words +
                                          replacing_characters_in_split_words +
                                          insert_characters_in_split_words)

        return alternative_words_generated

    def alternative_words_in_english(self, test_word):
        """Method generates alternative words, and returns which ones of them are English.

            Args:
                test_word (string): A word written by the user (string).

            Returns:
                List: Method returns a list of alternative English words
        """
        all_alternative_words = self.alternative_words_with_one_distance(
            test_word)
        alternative_english_words = []

        for word in all_alternative_words:
            if self.trie.search_if_word_in_trie(word) is True:
                alternative_english_words.append(word)

        return alternative_english_words

    def generate_matrix(self, user_word_length, dictionary_word_length):
        """Method generates a distance matrix used when calculating Levenshtein
        distance and Optimal string alignment distance.

        Args:
            user_word_length (int): Length of the word typed by user
            dictionary_word_length (int): Length of the word taken from dictionary
        """
        baseline_matrix = np.full(
            (user_word_length, dictionary_word_length), float(
                user_word_length+dictionary_word_length))
        first_column = np.arange(1, user_word_length+1, 1)
        first_column = first_column.reshape(-1, 1)
        first_row = np.arange(0, dictionary_word_length+1, 1)
        first_row = first_row.reshape(-1, 1)
        first_row = first_row.T
        matrix = np.append(first_column, baseline_matrix, axis=1)
        matrix = np.append(first_row, matrix, axis=0)

        return matrix

    def generate_damerau_leven_matrix(self, user_word_length, dictionary_word_length):
        """Method generates a distance matrix used when calculating Damerau-Levenshtein
        distance.

        Args:
            user_word_length (int): Length of the word typed by user
            dictionary_word_length (int): Length of the word taken from dictionary
        """

        baseline_matrix = np.full(
            (user_word_length+2, dictionary_word_length+2), float(
                user_word_length+dictionary_word_length))
        for i in range(1, user_word_length+2):
            baseline_matrix[i][1] = i-1
        for j in range(1, dictionary_word_length+2):
            baseline_matrix[1][j] = j-1

        return baseline_matrix

    def cost_heuristic_for_characters(self, character_1, character_2, weighting=False):
        """Method returns heuristic to estimate the distance between
        two characters.

        Args:
            character_1 (string): One character
            character_2 (string): Another character
        """

        if weighting is False:
            return self.distance_heuristics.distance_heuristic_always_the_same(character_1,
                                                                               character_2)
        elif weighting is True:
            return self.distance_heuristics.calculate_distance_heuristic_for_characters_keyboard_only(
                character_1, character_2)

    def calculate_levenshtein_distance(self, user_word, dictionary_word, weighting_used=False):
        """Method calculates Levenshtein distance between two words, which allows
        insertions, deletions, and symbol substitutions to transform from
        user word to dictionary word. Full matrix is used for illustrative purposes.

        Args:
            user_word (string): Word typed by user
            dictionary_word (string): Word taken from dictionary
        """
        distance_matrix = self.generate_matrix(
            len(user_word), len(dictionary_word))

        for i in range(1, len(user_word)+1):
            for j in range(1, len(dictionary_word)+1):
                distance = self.cost_heuristic_for_characters(
                    user_word[i-1], dictionary_word[j-1], weighting_used)
                distance_matrix[i][j] = min((distance_matrix[i-1][j]+1),
                                            (distance_matrix[i][j-1]+1),
                                            (distance_matrix[i-1][j-1]+distance))

        shortest_distance = distance_matrix[len(
            user_word), len(dictionary_word)]

        return shortest_distance

    def calculate_optimal_string_alignment_distance(self, user_word, dictionary_word,
                                                    weighting_used=False):
        """Method calculates optimal string alignment distance between two words, which allows
        insertions, deletions, and symbol substitutions to transform from
        user word to dictionary word as well as transposition.
        It does not allow for multiple transformation on the same substring.
        Full matrix is used for illustrative purposes.

        Args:
            user_word (string): Word typed by user
            dictionary_word (string): Word taken from dictionary
        """

        distance_matrix = self.generate_matrix(
            len(user_word), len(dictionary_word))

        for i in range(1, len(user_word)+1):
            for j in range(1, len(dictionary_word)+1):
                distance = self.cost_heuristic_for_characters(
                    user_word[i-1], dictionary_word[j-1], weighting_used)
                distance_matrix[i][j] = min((distance_matrix[i-1][j]+1),
                                            (distance_matrix[i][j-1]+1),
                                            (distance_matrix[i-1][j-1]+distance))

                if (i > 1) and (j > 1) and (user_word[i-1] == dictionary_word[j-2]) and (user_word[i-2] == dictionary_word[j-1]):
                    distance_matrix[i, j] = min(
                        distance_matrix[i][j], distance_matrix[i-2][j-2]+1)

        shortest_distance = distance_matrix[len(
            user_word), len(dictionary_word)]

        return shortest_distance

    def generate_baseline_row_for_characters(self):
        """Method generates a dictionary that shows for each English character,
        and one symbol ("_") what was the last row in the Damerau-Levenhstein distance
        matrix where it was present.
        """

        baseline_row_for_characters = {}
        characters = string.ascii_lowercase
        for char in characters:
            baseline_row_for_characters[char] = 0
        baseline_row_for_characters["_"] = 0

        return baseline_row_for_characters

    def calculate_damerau_levenshtein_distance(self, user_word, dictionary_word,
                                               weighting_used=False):
        """Method calculates Damerau-Levenshtein distance between two words, which allows
        insertions, deletions, and symbol substitutions to transform from
        user word to dictionary word as well as transposition.
        It also allows for multiple transformation on the same substring.
        Full matrix is used for illustrative purposes.

        Args:
            user_word (string): Word typed by user
            dictionary_word (string): Word taken from dictionary
        """

        distance_matrix = self.generate_damerau_leven_matrix(
            len(user_word), len(dictionary_word))
        latest_row_for_character = self.generate_baseline_row_for_characters()

        for i in range(2, len(user_word)+2):
            latest_column_for_character = 0
            for j in range(2, len(dictionary_word)+2):
                last_matching_row = latest_row_for_character[dictionary_word[j-2]]
                last_matching_column = latest_column_for_character

                if user_word[i-2] == dictionary_word[j-2]:
                    distance_cost = 0
                    latest_column_for_character = j
                else:
                    distance_cost = self.cost_heuristic_for_characters(
                        user_word[i-2], dictionary_word[j-2], weighting_used)

                distance_matrix[i][j] = min(distance_matrix[i-1][j-1]+distance_cost,
                                            distance_matrix[i][j-1]+1,
                                            distance_matrix[i-1][j]+1,
                                            (distance_matrix[last_matching_row-1][last_matching_column-1]
                                            + (i-last_matching_row-1)+(j-last_matching_column-1)+1)
                                            )

            latest_row_for_character[user_word[i-2]] = i

        return distance_matrix[-1][-1]

    def suggest_words_based_on_distance(self, given_user_word, indicator_for_metric=3,
                                        weighting_used=False):
        """Method identifies all the words in the English dictionary (trie data structure)
        that are within +/-1 character length from the word given by the user,
        calculates their distance to the user word, and suggests the ones with the
        shortest distance.

        Args:
            given_user_word (string): Word written by the user.
            indicator_for_metric (int, optional): Indicates which distance metric is
            to be used in the distance calculation. Defaults to 3 (Damerau-Levenshtein).
        """

        suggestions = []

        alternatives_from_dictionary = self.trie.get_all_words(
            True, len(given_user_word))

        for item in alternatives_from_dictionary:
            dictionary_word = item[1]
            if indicator_for_metric == 1:
                distance = self.calculate_levenshtein_distance(
                    given_user_word, dictionary_word, weighting_used)
            elif indicator_for_metric == 2:
                distance = self.calculate_optimal_string_alignment_distance(
                    given_user_word, dictionary_word, weighting_used)
            else:
                distance = self.calculate_damerau_levenshtein_distance(
                    given_user_word, dictionary_word, weighting_used)

            frequency = item[2]
            suggestions.append((dictionary_word, distance, frequency))

        return self.select_top_suggestions(suggestions)

    def select_top_suggestions(self, all_suggestions):
        """Method prioritizes among all suggestions identified the best suggestions
        for the misspelled word.

        Args:
            all_suggestions (list): List contains words that are English, whose
            length is maximum +/- one character from the misspelled word,
            and their distance metric and frequency in the dictionary.
        """
        full_suggestion_list = all_suggestions
        sorted_suggestions = sorted(
            full_suggestion_list, key=lambda element: (element[1], -element[2]))
        top_suggestions = sorted_suggestions[0:10]

        return top_suggestions
