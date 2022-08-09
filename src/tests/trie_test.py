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

    def test_insert_nodes_with_frequency(self):
        word_tested = "new_test_word"
        frequency_tested = 6000
        self.test_trie.insert_nodes(word_tested, frequency_tested)
        output = self.test_trie.search_word_full_data(word_tested)
        wanted_answer = (True, "new_test_word", 6000)
        self.assertEqual(output, wanted_answer)

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

    def test_search_words_starting_with(self):
        word_list = ["abandon", "ability", "able", "about", "ab"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        answer = self.test_trie.search_words_starting_with("ab")
        wanted_answer = ["ab", "abandon", "ability", "able", "about"]
        self.assertEqual(answer, wanted_answer)

    def test_search_word_full_data_false(self):
        word_tested = "word_not_found"
        output = self.test_trie.search_word_full_data(word_tested)
        wanted_answer = False
        self.assertEqual(output, wanted_answer)

    def test_insert_multiple_words_with_word_count_in_trie(self):
        word_list_with_count = [("abandon", 300), ("ability", 4),
                                ("able", 17000), ("about", 30000), ("ab", 3), ("abandoned", 50)]
        self.test_trie.insert_multiple_words_with_word_count_in_trie(
            word_list_with_count)
        output = self.test_trie.search_word_full_data("ability")
        wanted_answer = (True, "ability", 4)
        self.assertEqual(output, wanted_answer)

    def test_get_all_words_only_words(self):
        word_list = ["abandon", "ability", "able", "about",
                     "ab", "pizza", "jones", "manual", "man"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        response = self.test_trie.get_all_words()
        self.assertEqual(sorted(response), sorted(word_list))

    def test_get_all_words_all_data(self):
        word_list = ["abandon", "ability", "able", "about",
                     "ab", "pizza", "jones", "manual", "man"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        response = self.test_trie.get_all_words(True)
        wanted_answer = []
        for word in word_list:
            wanted_answer.append((True, word, 1, len(word)))
        self.assertEqual(sorted(response), sorted(wanted_answer))

    def test_get_all_words_length_available(self):
        word_list = ["abandon", "ability", "able", "about",
                     "ab", "pizza", "jones", "manual", "man"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        original_word_length = 5
        response = self.test_trie.get_all_words(True, original_word_length)
        wanted_answer = 5
        self.assertEqual(len(response), 5)

    def test_get_all_words_length_not_available(self):
        word_list = ["abandon", "ability", "able", "about",
                     "ab", "pizza", "jones", "manual", "man"]
        self.test_trie.insert_multiple_words_in_trie(word_list)
        original_word_length = 10
        response = self.test_trie.get_all_words(True, original_word_length)
        wanted_answer = 0
        self.assertEqual(len(response), wanted_answer)
