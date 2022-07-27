from services.spell_check import SpellCheck

class UI:
    def __init__(self):
        #        print("initiating ui class")
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
            print(f"Here are alternative ways to spell your word: {word}")
            outputs = self.check_spelling.alternative_words_with_one_distance(
                word)
            print(f"There are {len(outputs)} to write your word")
            print(outputs)
