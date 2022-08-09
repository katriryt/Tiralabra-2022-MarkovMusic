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
                        f"Option 2: All words from dictionary with Levenshtein distance")
                    output2 = self.check_spelling.suggest_words_based_on_distance(
                        word, 1)
                    print(
                        f"Shortest distance found was {output2[0]}. There are {len(output2[1])} ways to write your word in English")
                    print(output2[1])
                    print("")

                    print(
                        f"Option 3: All words from dictionary with Optimal string alignment distance")
                    output3 = self.check_spelling.suggest_words_based_on_distance(
                        word, 2)
                    print(
                        f"Shortest distance found was {output3[0]}. There are {len(output3[1])} ways to write your word in English")
                    print(output3[1])
                    print("")

                    print(
                        f"Option 4: All words from dictionary with Damerau-Levenshtein distance")
                    output4 = self.check_spelling.suggest_words_based_on_distance(
                        word, 3)
                    print(
                        f"Shortest distance found was {output4[0]}. There are {len(output4[1])} ways to write your word in English")
                    print(output4[1])
