import string


class TrieNode:
    """Class creates one node in the trie data structure."""

    def __init__(self, given_character):
        """Method initiatializes one node in the trie structure
        with its characteristics.

        Args:
            given_character (string): Node is given a string of character.
        """
#        print("trie-noodin konstruktorissa")
        self.character = given_character
        self.node_is_end_of_word = False
        self.children = {}
        self.word_in_node = None
        self.word_count = 0
        self.word_length = 0

    def __repr__(self):
        # node_content = f"Character is {self.character}, end of word is:
        # {self.node_is_end_of_word} and children are {self.children.keys()}"
        # return node_content
        return f"{self.character}"


class Trie:
    """Class creates the overall trie structure and provides
    the key operations (insertion and searching)."""

    def __init__(self):
        """ Method initializes the trie data structure (tree).
        """
#        print("alustaa trie-puuta")
        self.root = TrieNode("")
        self.all_words = []

    def insert_nodes(self, word, given_word_count=1):
        """Method inserts one node in the trie data structure.

        Args:
            word (string): Method is given a word, based on which nodes for
            its characters are added.
            given_word_count (int, optional): Method may be given a frequency number
            indicating how often the word is used in English language normally.
            Defaults to 1.

        """
        node = self.root

        for character in word:
            if character in node.children:
                # print(f"character {character} is already among the node's children")
                node = node.children[character]
            else:
                # print(f"character {character} is not among the node's children")
                new_node = TrieNode(character)
                node.children[character] = new_node
                node = new_node
                # print(f"Insertion continues along the new node {node}")

        node.node_is_end_of_word = True
        node.word_in_node = word
        node.word_count = given_word_count
        node.word_length = len(word)

    def select_word_for_list(self, node, data_wanted=False, original_word_length=None):
        """Method selects what data for the end node in question is to be returned for the user.

        Args:
            node (TrieNode): Indicates the node in question.
            data_wanted (bool, optional): Boolean variable. False indicates that only the word
            is wanted from the trie structure. True indicates that also other
            data available for the node, e.g. its frequency, is wanted. Defaults to False.
            original_word_length (int, optional): Integer indicating the length of the
            original word typed by the user. Defaults to None.
        """
#        print(f"selecting word, node is {node.word_in_node}")
        accepted_distance_from_original_word = 1

        if original_word_length is None:
            #            print(f"length does not matter")
            if data_wanted is False:
                #                print("selecting word, lisäämässä sanaa listalle")
                self.all_words.append(node.word_in_node)
            else:
                #                print("selecting word, lisäämässä kaikkea tietoa listalle")
                self.all_words.append(
                    (node.node_is_end_of_word, node.word_in_node, node.word_count,
                     node.word_length))

        elif (original_word_length is not None) and ((node.word_length == original_word_length) or (node.word_length == original_word_length+accepted_distance_from_original_word) or (node.word_length == original_word_length-accepted_distance_from_original_word)):
            #            print(f"length within parameters {accepted_distance_from_original_word}")
            if data_wanted is False:
                #                print("selecting word, lisäämässä sanaa listalle")
                self.all_words.append(node.word_in_node)
            else:
                #                print("selecting word, lisäämässä kaikkea tietoa listalle")
                self.all_words.append(
                    (node.node_is_end_of_word, node.word_in_node, node.word_count,
                     node.word_length))

#        else:
#            print("requirements not met")

    def depth_first_search(self, node, previous_node, data_wanted=False, original_word_length=None):
        """Method is the basic depth first search, targeting to find the end nodes in the
        trie data structure.

        Args:
            node (TrieNode): Indicates the node that is being searched.
            previous_node (TrieNode): Indicates the previous node where the search came from.
            data_wanted (bool, optional): Boolean variable. False indicates that only the word
            is wanted from the trie structure. True indicates that also other
            data available for the node, e.g. its frequency, is wanted. Defaults to False.
            original_word_length (int, optional): Integer indicating the length of the
            original word typed by the user. Defaults to None.
        """
        if node.node_is_end_of_word is True:
            # when frequency values are added to the tree, change what is returned here
            #            print(f"last node is reached, data wanted is {data_wanted}")
            self.output.append((previous_node + node.character))
            self.select_word_for_list(node, data_wanted, original_word_length)

        for child in node.children.values():
            # print(
            #    f"ei olla vielä lopussa, ollaan noden lapsessa {child}, jatketaan syvyyshakua")
            self.depth_first_search(
                child, previous_node + node.character, data_wanted, original_word_length)

    def search_words_starting_with(self, given_string, data_wanted=False,
                                   original_word_length=None):
        """Method searches for all the words that start with the given string from the trie
        data structure. It returns a list of the words starting with the given string.

        Args:
            given_string (string): String to be searched from the trie data structure
            data_wanted (bool, optional): Boolean variable. If false, the method returns
            only the word in the trie structure. If true, the method returns also other
            data available for the word, e.g. its frequency. Defaults to False.
            original_word_length (integer, optional): Integer indicating the length of the
            original word typed by the user. Defaults to None.

        Returns:
            _type_: _description_
        """
#        print(f"searching words starting with a character, data wanted is {data_wanted}")
        # name previously: search_alternative_spellings_for_word
        # print(f"searching for string: {given_string}")
        node = self.root
        for character in given_string:
            if character in node.children:
                node = node.children[character]
            else:
                return []
        self.output = []
        self.depth_first_search(
            node, given_string[:-1], data_wanted, original_word_length)
        return self.output

    def get_all_words(self, data_wanted=False, original_word_length=None):
        """Method launches search for all words in the trie data structure that
        start with all characters in the English alphabet.
        It returns a list of all the words and their related data in the trie data
        structure, based on given parameters.

        Args:
            data_wanted (bool, optional): Boolean variable. If false, the method returns
            only the words in the trie structure. If true, the method returns also other
            data available for the words, e.g. their frequency. Defaults to False.
            original_word_length (int, optional): Integer indicating the length of the
            original word typed by the user. Defaults to None.
        """
#        print(f"get all words, data_wanted is {data_wanted}")
        self.all_words = []
        word_starts = string.ascii_lowercase
        for word_prefix in word_starts:
            self.search_words_starting_with(
                word_prefix, data_wanted, original_word_length)
#            print(self.output)
#        print(self.output)
        return self.all_words

    def search_if_word_in_trie(self, word):
        """Method searches the trie data structure, and returns
        whether the given word is within it.

        Args:
            word (string): A word typed by the user, or generated by the program.

        Returns:
            Boolean: Method returns a Boolean value whether the given word is
            in the trie structure (True) or not (False).
        """
#        print(f"etsimässä {word}")
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return False
        return node.node_is_end_of_word

    def search_word_full_data(self, word):
        """Method searches the trie data structure, and returns
        whether the given word is within it, and its related characteristics.

        Args:
            word (string): A word typed by the user, or generated by the program.

        Returns:
            Boolean value or tuple: Method returns a Boolean value if the word is
            not in trie, or a tuple consisting of word's related characteristics.
        """
#        print(f"etsimässä tietoa: {word}")
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return False
        return (node.node_is_end_of_word, node.word_in_node, node.word_count)

    def insert_multiple_words_in_trie(self, given_list):
        """Method inserts multiple words in the trie data structure.

        Args:
            given_list (list): List of words given by application.
        """
        for word in given_list:
            self.insert_nodes(word)

    def insert_multiple_words_with_word_count_in_trie(self, given_list):
        """Method inserts multiple words, with a given frequency, from a list
        to trie data structure.

        Args:
            given_list (list): List of tuples, each tuple consists of word (string),
            and frequency number (integer).
        """
        for item in given_list:
            #            print(item)
            self.insert_nodes(item[0], item[1])


trie = Trie()
