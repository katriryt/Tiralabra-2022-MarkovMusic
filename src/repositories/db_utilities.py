from pathlib import Path
import json
from repositories.trie import trie as default_trie


class EnglishDictionary:
    """Class fetches words used in the application's dictionary, and
        populates the spellchecker's trie data structure with
        English words and their frequencies.
    """

    def __init__(self, trie=default_trie):
        """Method initiatilizes the English dictionary by calling
        the key methods in the class.

        Args:
            trie (Class, optional): Class for the trie data structure.
            Defaults to default_trie.
        """
        self.trie = trie
        self.words_in_original_dictionary = 0
        self.frequencies_in_original_dictionary = 0
        self.words_in_trie = 0
        self.frequencies_in_trie = 0

        self.file_name = self.get_english_word_file_location()
        self._populate_trie_based_on_file()

    def get_english_word_file_location(self):
        """ Method returns the location of the English dictionary file.
        """

        script_location = Path(__file__).absolute().parent.parent.parent
        file_location = script_location/"data"/"english_word_frequency_dictionary.json"
        return file_location

    def _populate_trie_based_on_file(self):
        """Method populates trie with the words and their frequencies from
        the English dictionary that only contain English alphabets
        e.g. words with numbers are excluded.
        """

        words_frequencies_dictionary = json.load(open(self.file_name, 'r'))

        for key, value in words_frequencies_dictionary.items():
            self.words_in_original_dictionary += 1
            self.frequencies_in_original_dictionary += value
            word = str(key)
            if word.isalpha() is True:
                self.trie.insert_nodes(word, value)
                self.words_in_trie += 1
                self.frequencies_in_trie += value

#        print(f"Original dictionary. Words: {self.words_in_original_dictionary} and frequencies: {self.frequencies_in_original_dictionary}")
#        print(f"Trie. Words: {self.words_in_trie} and frequencies: {self.frequencies_in_trie}")


english_dictionary = EnglishDictionary()
