from repositories.trie import trie as default_trie
from repositories.db_utilities import english_dictionary as default_english_dictionary


class SpellCheck:
    """Class provides core functionalities for spellchecking.
    """

    def __init__(self, trie=default_trie, dictionary=default_english_dictionary):
        """Method initializes the spell checker, the related trie
            data structure, and the English dictionary

            Args:
                trie (Class, optional): Trie data structure populated with English
                words. Defaults to default_trie.
                dictionary (Class, optional): Class opens data file with English
                dictionary and populates the trie structure. Defaults to default_english_dictionary.
        """

#        print("initializing spell checker")
        self.trie = trie
        self.dictionary = dictionary

    def convert_user_input_as_list(self, user_input):
        """Method converts given user input into a list.

        Args:
             user_input (string): Input is one or multiple words in string format.
        """
        # Need to add separation of commas and points here or somewhere else
        #        print(f"starting to convert user inputs to a list {user_input}")
        user_input_as_list = list(user_input.lower().split())
#        print(user_input_as_list)
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

#        print(f"starting to generate alternative words. given word was: {test_word}")
        alternative_words_generated = ""
        alternative_letters = "abcdefghijklmnopqrstuvwxyz"
        split_test_word = [(test_word[:i], test_word[i:])
                           for i in range(len(test_word) + 1)]
#        print(split_test_word)
        deleting_characters = [split_left + split_right[1:]
                               for split_left, split_right in split_test_word if split_right]
#        print(deleting_characters)
        transposing_characters_in_split_words = [split_left + split_right[1] + split_right[0] +
                                                 split_right[2:] for split_left,
                                                 split_right in split_test_word
                                                 if len(split_right) > 1]
#        print(transposing_characters_in_split_words)
        replacing_characters_in_split_words = [split_left + character + split_right[1:]
                                               for split_left, split_right
                                               in split_test_word
                                               if split_right for character in alternative_letters]
#        print(replacing_characters_in_split_words)
        insert_characters_in_split_words = [split_left + character + split_right for split_left,
                                            split_right in split_test_word for character
                                            in alternative_letters]
#        print(insert_characters_in_split_words)

#        print(set(deleting_characters + transposing_characters_in_split_words +
#               replacing_characters_in_split_words + insert_characters_in_split_words))
        alternative_words_generated = set(deleting_characters +
                                          transposing_characters_in_split_words +
                                          replacing_characters_in_split_words +
                                          insert_characters_in_split_words)
#        print(alternative_words_generated)
#        print(len(alternative_words_generated))
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
