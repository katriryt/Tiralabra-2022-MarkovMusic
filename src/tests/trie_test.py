import unittest
from repositories.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.test_trie = Trie()

    def test_insert_nodes(self):
        word_tested = "ability"
        self.test_trie.insert_nodes(word_tested)
        answer = self.test_trie.search_if_word_in_trie(word_tested)
        wanted_answer = True
        self.assertEqual(answer, wanted_answer)

    def test_insert_words_words_found(self):
        word_list = ["abandon", "ability", "able", "about", "ab"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        answer = []
        for word in word_list:
            response = self.test_trie.search_if_word_in_trie(word)
            answer.append(response)
        wanted_answer = [True, True, True, True, True]
        self.assertEqual(answer, wanted_answer)

    def test_insert_words_word_not_found(self):
        word_list = ["abandon", "ability", "able", "about", "ab"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        test_word = "nomimono"
        answer = self.test_trie.search_if_word_in_trie(test_word)
        wanted_answer = False
        self.assertEqual(answer, wanted_answer)

    def test_search_alternative_spellings_for_word(self):
        word_list = ["abandon", "ability", "able", "about", "ab"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        answer = self.test_trie.search_alternative_spellings_for_word("ab")
        wanted_answer = ["ab", "abandon", "ability", "able", "about"]
        self.assertEqual(answer, wanted_answer)
