class SpellCheck:
    """Class provides core functionalities for spellchecking.
    """
    #def __init__(self):
    #    pass

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
