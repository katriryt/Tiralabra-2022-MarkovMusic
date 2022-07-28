class TrieNode:
    """Class creates one node in the trie data structure."""

    def __init__(self, given_character):
        # when frequency values are added to the tree, add the frequency value here
        self.character = given_character
        self.node_is_end_of_word = False
        self.children = {}

    def __repr__(self):
        # node_content = f"Character is {self.character}, end of word is:
        # {self.node_is_end_of_word} and children are {self.children.keys()}"
        # return node_content
        return f"{self.character}"


class Trie:
    """Class creates the overall trie structure and provides
    the key operations (insertion and searching)."""

    def __init__(self):
        self.root = TrieNode("")

    def insert_nodes(self, word):
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

        # If the frequencies are already part of data, add the frequency metrics here

    def depth_first_search(self, node, previous_node):
        if node.node_is_end_of_word is True:
            # when frequency values are added to the tree, change what is returned here
            # print("last node is reached")
            self.output.append((previous_node + node.character))

        for child in node.children.values():
            #print(
            #    f"ei olla vielä lopussa, ollaan noden lapsessa {child}, jatketaan syvyyshakua")
            self.depth_first_search(child, previous_node + node.character)

    def search_alternative_spellings_for_word(self, given_string):
        # print(f"searching for string: {given_string}")
        node = self.root
        for character in given_string:
            if character in node.children:
                node = node.children[character]
            else:
                return []
        self.output = []
        # print(given_string[:-1])
        self.depth_first_search(node, given_string[:-1])

        return self.output

    def search_if_word_in_trie(self, word):
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return False
        return node.node_is_end_of_word
        # Update this when frequencies are added

    def insert_multiple_words_in_trie(self, given_list):
        for word in given_list:
            self.insert_nodes(word)
