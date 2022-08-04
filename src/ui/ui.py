from services.spell_check import SpellCheck


class UI:
    """Class starts the application and provides methods for interacting
    with the user.
    """

    def __init__(self):
        print("initiating ui class")
        self.check_spelling = SpellCheck()

    def start(self):
        print(
            "Welcome to the Verbum Reprehendo - spell checker for English language words!")
        user_input = str(input("Please type in your text to be checked:"))
#        print(user_input)

        user_input_as_list = self.check_spelling.convert_user_input_as_list(
            user_input)
#        print(user_input_as_list)

        for word in user_input_as_list:
            #            answer = self.check_spelling.is_word_english(word)
            if self.check_spelling.is_word_english(word) is True:
                #                print(f"Your word: {word} is English {answer}")
                print(f"Your word: {word} is English")
            else:
                #                print(f"Your word: {word} is not English {answer}")
                print(f"Your word: {word} is not English")
#            for word in user_input_as_list:
                print(
                    f"Here are alternative ways to spell your word {word} in English")
                outputs = self.check_spelling.alternative_words_in_english(
                    word)
                print(
                    f"There are {len(outputs)} ways to write your word in English")
                print(outputs)
