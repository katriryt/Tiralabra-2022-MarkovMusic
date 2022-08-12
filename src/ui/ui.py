import re
from services.spell_check import SpellCheck


class UI:
    """Class starts the application and provides methods for interacting
    with the user.
    """

    def __init__(self):
        """Method initiates the UI class. 
        """
#        print("initiating ui class")
        self.spell_checking_continues = True
        self.exit_checking_continues = True
        self.full_original_user_input = []
        self.user_input_as_list = []
        self.check_spelling = SpellCheck()

    def request_input_for_spell_checking(self):
        """Method requests for user inputs and changes it for spell checking.
        """
        user_input = str(input("Please type in your text (please limit to one word) to be checked:"))
        #print(user_input)
        self.full_original_user_input = self.check_spelling.convert_original_user_input_as_list(user_input)
#        print(self.full_original_user_input)
        self.user_input_as_list = self.check_spelling.convert_user_input_as_list(
            user_input)
#        print(self.user_input_as_list)
        print("")

    def print_results_from_spell_checking(self):
        for word in self.user_input_as_list:
            if self.check_spelling.is_word_english(word) is True:
                print(f"Your word: {word} is English")
                print("")
            else:
                print(f"Your word: {word} is not English")
                print("")
                if word.isalpha() is False:
                    print(
                        f"Please note that your word {word} does not consist of alphabets and is not checked")
                    print("")
                else:
                    print(
                        f"Here are alternative ways to spell your word {word} in English")
                    print("")
                    print(
                        f"Option 1: Simplistic method generating words with one Damerau-Levenshtein distance")
                    outputs = self.check_spelling.alternative_words_in_english(
                        word)
                    print(
                        f"There are {len(outputs)} ways to write your word in English")
                    print(outputs)
                    print("")
                    print(
                        f"Option 2: All words from dictionary based on Levenshtein distance")
                    output2 = self.check_spelling.suggest_words_based_on_distance(
                        word, 1)
                    print(
                        f"Shortest distance found was {output2[0]}. There are {len(output2[1])} ways to write your word in English")
                    print(output2[1])
                    print("")
                    print(
                        f"Option 3: All words from dictionary based on Optimal string alignment distance")
                    output3 = self.check_spelling.suggest_words_based_on_distance(
                        word, 2)
                    print(
                        f"Shortest distance found was {output3[0]}. There are {len(output3[1])} ways to write your word in English")
                    print(output3[1])
                    print("")
                    print(
                        f"Option 4: All words from dictionary based on Damerau-Levenshtein distance")
                    output4 = self.check_spelling.suggest_words_based_on_distance(
                        word, 3)
                    print(
                        f"Shortest distance found was {output4[0]}. There are {len(output4[1])} ways to write your word in English")
                    print(output4[1])
                    print("")
                    print("")

        self.exit_checking_continues = True

    def check_for_exiting_spellchecker(self):
        """ Method allows user to exit from the spellchecker.
        """
        while self.exit_checking_continues is True: 
            user_recheck_input = input("Would you like to spell check another phrase? Press 1 if yes, and 2 if you would like to exit:")
            if user_recheck_input == "2": 
                self.spell_checking_continues = False
                self.exit_checking_continues = False
            elif user_recheck_input == "1":
                self.spell_checking_continues = True
                self.exit_checking_continues = False
            else:
                print("Your input was not valid. Please try again.")

    def start(self):
        """Method starts the UI, and runs its main methods.
        """
        print(
            "Welcome to the Verbum Reprehendo - spell checker for English language words!")
        while self.spell_checking_continues is True:
            self.request_input_for_spell_checking()
            self.print_results_from_spell_checking()
            self.check_for_exiting_spellchecker()
