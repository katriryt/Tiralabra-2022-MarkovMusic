import re
from services.spell_check import SpellCheck


class UI:
    """Class provides methods for interaction with the user, and calls
    for the relevant methods from the Spellcheck class.
    """

    def __init__(self):
        """Method initiates the UI class. 
        """
#        print("initiating ui class")
        self.spell_checking_continues = True
        self.exit_checking_continues = True
        self.weighting_checking_continues = True
        self.weighting_used = False
        self.full_original_user_input = []
        self.user_input_as_list = []
        self.check_spelling = SpellCheck()

    def request_input_for_spell_checking(self):
        """Method requests for user inputs and changes it for spell checking.
        """
        user_input = str(input("Please type in your text to be checked:"))
        # print(user_input)
        self.full_original_user_input = self.check_spelling.convert_original_user_input_as_list(
            user_input)
#        print(self.full_original_user_input)
        self.user_input_as_list = self.check_spelling.convert_user_input_as_list(
            user_input)
#        print(self.user_input_as_list)
        print("")

    def check_if_weighting_is_used(self):
        """Method requests user input on whether weighting is to be used in distance calculations.
        """
        while self.weighting_checking_continues is True:
            user_weighting_input = input(
                "Would you like to use more advanced methods (weighting distance metrics) to identify your word? Press 1 if yes, and 2 if no:")
            if user_weighting_input == "1":
                self.weighting_used = True
                self.weighting_checking_continues = False
            elif user_weighting_input == "2":
                self.weighting_used = False
                self.weighting_checking_continues = False
            else:
                print("Your input was not valid. Please try again.")
                self.weighting_checking_continues = True

    def check_for_exiting_spellchecker(self):
        """ Method allows user to exit from the spellchecker.
        """
        while self.exit_checking_continues is True:
            user_recheck_input = input(
                "Would you like to spell check another phrase? Press 1 if yes, and 2 if you would like to exit:")
            if user_recheck_input == "2":
                self.spell_checking_continues = False
                self.exit_checking_continues = False
            elif user_recheck_input == "1":
                self.spell_checking_continues = True
                self.exit_checking_continues = False
            else:
                print("Your input was not valid. Please try again.")

    def format_output_list(self, suggestions_list):
        """ Method formats and prints out the suggested list of words.
        """
        for item in suggestions_list:
            print(
                f"Word: {item[0]}, distance: {item[1]:.2f}, frequency: {item[2]}")

    def print_results_from_spell_checking(self):
        """Method checks whether the word is in English dictionary, and if not, it suggests
        alternative words for the misspelled word. 
        """
        for word in self.user_input_as_list:
            if self.check_spelling.is_word_english(word) is True:
                print(
                    f"Your word: {word} is found from the English dictionary and is correctly spelled\n")
            else:
                if self.check_spelling.word_contains_only_english_characters(word) is False:
                    print(
                        f"Please note that your word {word} does not consist of only English alphabet and cannot be checked\n")
                else:
                    print(
                        f"Your word: {word} is not found from the English dictionary\n")
                    self.check_if_weighting_is_used()
                    print(
                        f"Here are alternative ways to spell your word {word} in English\n")
                    print(
                        f"Option 1: Simplistic method generating words with one Damerau-Levenshtein distance")
                    outputs = self.check_spelling.alternative_words_in_english(
                        word)
                    print(
                        f"There are {len(outputs)} ways to write your word in English")
                    print(outputs)
                    print("")
                    for metric_selector in range(1, 4):
                        if metric_selector == 1:
                            text = "Option 2: All words from dictionary based on Levenshtein distance"
                        elif metric_selector == 2:
                            text = "Option 3: All words from dictionary based on Optimal string alignment distance"
                        elif metric_selector == 3:
                            text = "Option 4: All words from dictionary based on Damerau-Levenshtein distance"
                        print(text)
                        output = self.check_spelling.suggest_words_based_on_distance(
                            word, metric_selector, self.weighting_used)
                        print(f"Top suggestions for your word {word} are:")
                        self.format_output_list(output)
                        print("")
                    print("")

        self.exit_checking_continues = True
        self.weighting_checking_continues = True
        self.weighting_used = False

    def start(self):
        """Method starts the UI, and runs its main methods.
        """
        print(
            "Welcome to the Verbum Reprehendo - spell checker for English language words!")
        while self.spell_checking_continues is True:
            self.request_input_for_spell_checking()
            self.print_results_from_spell_checking()
            self.check_for_exiting_spellchecker()
