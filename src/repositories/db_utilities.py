from pathlib import Path
import json
from repositories.trie import trie as default_trie


class EnglishDictionary:
    """Class populates the spellchecker's trie data structure with
        English words and their frequencies.
    """

    def __init__(self, trie=default_trie):
        #        print("initializing dictionary")
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
#        print("getting file location")
        script_location = Path(__file__).absolute().parent.parent.parent
        file_location = script_location/"data"/"english_word_frequency_dictionary.json"
        return file_location

    def _populate_trie_based_on_file(self):
        """Method populates trie with the words and their frequencies from
        English dictionary that only contain English alphabets
        e.g. words with numbers are excluded.
        """
        words_frequencies_dictionary = json.load(open(self.file_name, 'r'))

        for key, value in words_frequencies_dictionary.items():
        #    print(f"{key}: {value}")
            self.words_in_original_dictionary += 1
            self.frequencies_in_original_dictionary += value
            word = str(key)
            if word.isalpha() is True:
                self.trie.insert_nodes(word, value)
                self.words_in_trie += 1
                self.frequencies_in_trie += value

        print(f"""original dictionary. Words: {self.words_in_original_dictionary}
                and frequencies: {self.frequencies_in_original_dictionary}""")
        print(f"trie. Words: {self.words_in_trie} and frequencies: {self.frequencies_in_trie}")


english_dictionary = EnglishDictionary()
