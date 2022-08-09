from pathlib import Path
from repositories.trie import trie as default_trie


class EnglishDictionary:
    """Class populates the spellchecker's trie data structure with
        English words.
    """

    def __init__(self, trie=default_trie):
        #        print("initializing dictionary")
        self.trie = trie
#        self._populate_trie_with_words()
        self.file_name = self.get_english_word_file_location()
        self._populate_trie_based_on_file()

    def get_english_word_file_location(self):
        """ Method returns the location of the English dictionary file.
        """
#        print("getting file location")
        script_location = Path(__file__).absolute().parent.parent.parent
        file_location = script_location/"data"/"english_words.csv"
        return file_location

    def _populate_trie_based_on_file(self):
        """Method populates trie with the words from English dictionary that
        only contain English alphabets e.g. words with numbers are excluded.
        """
        #        print("getting words")
        with open(self.file_name) as given_file:
            contents = given_file.readlines()
            # This row may be limited during testing [600:900]
            for row in contents:
                if row.strip().isalpha() is True:
                    self.trie.insert_nodes(row.strip())
#        print("words saved")


english_dictionary = EnglishDictionary()
