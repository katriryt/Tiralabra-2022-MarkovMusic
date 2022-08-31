from pathlib import Path
import pandas as pd
import random
from services.spell_check import SpellCheck


class RelevanceTests():
    """Purpose of this class is to define and conduct the relevance tests.
    """
    def __init__(self):
        """Method initiates the relevance test class. 
        Test word lists consist of tuples in the format of (wrong_word, right_word).
        Number of test words to be run in the test is defined here.
        """
        self.input_file_name = self.get_test_word_file_location()
        self.number_of_test_words = 5
        self.all_test_words = []
        self.test_words = []
        self.final_results = []
        self.final_results_only_top_1 = []
        self.check_spelling = SpellCheck()

    def get_test_word_file_location(self):
        """ Method returns the location of the test word file.
        Three different test sets can be used: 
        Most common misspelled words in English: relevance_test_right_wrong_words.txt
        Princeton University's dictionary words, with one random mistake: relevance_test_random_test_words.txt
        Princeton University's dictionary words, with two random mistakes: relevance_test_random_test_words2.txt
        """
        script_location = Path(__file__).absolute().parent
#        print(script_location)
        file_location = script_location/"relevance_test_right_wrong_words.txt"
        print(file_location)
        return file_location

    def get_test_words(self):
        """Method gets all the test words in the chosen test file in the format of tuples (wrong_word, right_word). 
        It removes cases with multiple options or cases with where the answer could be multiple words.
        """
#        self.test_words = []
        with open (self.input_file_name) as new_file:
            contents = new_file.readlines()
#            print(len(contents))
        #    print(contents)
            for item in contents:
        #        print(item)
                row = item.strip("\n")
        #        print(row)
                empty = " "
                if empty not in row:
        #            print(f"this row is valid {row}")
                    row = row.split("->")
        #            print(row)
                    misspelled_word = row[0].lower()
                    correct_word = row[1].lower()
                    if self.check_spelling.word_contains_only_english_characters(misspelled_word) and self.check_spelling.word_contains_only_english_characters(correct_word): 
                        self.all_test_words.append((misspelled_word, correct_word))
        #        else: 
        #            print(f"not valid row: {row} ")
        print(len(self.all_test_words))
#        print(self.all_test_words)
    
    def get_subset_of_test_words(self):
        """Method limits the number of test words, and picks a random selection among the alternative test words.
        """
        self.test_words = random.sample(self.all_test_words, k=self.number_of_test_words)
        print(self.test_words)
        print(len(self.test_words))

    def get_suggested_word(self, test_word, method, weighting):
        """Method tests whether the test word is found with the application.

        Args:
            test_word (string): Test word given
            method (integer): Defines the test method: 1 for Levenshtein distance, 2 for Optimal string alignment, and 3 for Damerau-Levenshtein distance.
            weighting (Boolen): False value indicates that no weighting is to be used in the distance metric, True indicates that weighting in heuristics is to be used.
        """
        suggestions = self.check_spelling.suggest_words_based_on_distance(test_word, method, weighting)
        suggested_words = []
        for item in suggestions:
            suggested_words.append(item[0])
        return suggested_words

    def run_tests(self):
        """Method runs for all the test words and for all the combinations of tests. 
        It generates a list of results as tuples that show the method used (0, 1, 2, 3)
        (0 stands for the simplistics approach, other numbers as indicated above), 
        whether the weighting was used (False or True), and whether the right word was found (True or False). 
        Final results list indicates all the cases where the test word was found among the algorithms'
        suggestions, and Final results only top 1 indicates all the cases where the test word was
        the first suggestion by the algorithm.

        """
        self.get_test_words()
        self.get_subset_of_test_words()

        methods = [1, 2, 3]
        weighting = [False, True]
        self.final_results = []
        self.final_results_only_top_1 = []
        number_of_words_tested = 0

        for word_pair in self.test_words:
            print("")
            number_of_words_tested += 1
            print(f"number of word being tested: {number_of_words_tested}")
            print(word_pair)
            correct_word = word_pair[1]

            simplistic_results = self.check_spelling.alternative_words_in_english(word_pair[0])
#            print(f"simplistic results are: {simplistic_results}")
            if correct_word in simplistic_results:
                print("simplistic correct")
                self.final_results.append((0, False, True))
            else:
                print("simplistic not correct")
                self.final_results.append((0, False, False))

            for method in methods:
                for weight in weighting: 
                    print(f"method: {method}, weight: {weight}")
                    results = self.get_suggested_word(word_pair[0], method, weight)
#                    print(f"distance results are: {results}")
                    if correct_word == results[0]:
                        print("correct word is #1")
                        self.final_results_only_top_1.append((method, weight, True))
                    else: 
                        self.final_results_only_top_1.append((method, weight, False))

                    if correct_word in results: 
                        print("correct word found!")
                        self.final_results.append((method, weight, True))
                        
                    else:
                        print("correct not found")
                        self.final_results.append((method, weight, False))

#        print(self.final_results)
#        print(len(self.final_results))

#        print(self.final_results_only_top_1)
#        print(len(self.final_results_only_top_1))

    def calculate_result_frequencies(self):
        """Method calculates and prints out results from the relevance tests. 
        """
        results_from_tests = pd.DataFrame(self.final_results)
#        print(results_from_tests)

        results = results_from_tests.groupby([0, 1]).agg({2: ['sum', 'count']}).reset_index()
        results.columns = results.columns.get_level_values(0)
        results.columns = ['Method', 'Weighting_used','Correct_number', 'Total_number']
        results['Perc_Correct'] = (results['Correct_number'].astype(float)/results['Total_number'].astype(float))*100
        print("Results from relevance tests: How many of the words are correctly suggested (among top 10)?")
        print(results)

    def calculate_result_top_1_frequencies(self):
        """Method calculates and prints out results from the relevance tests. 
        """
        results_from_tests = pd.DataFrame(self.final_results_only_top_1)
#        print(results_from_tests)

        results = results_from_tests.groupby([0, 1]).agg({2: ['sum', 'count']}).reset_index()
        results.columns = results.columns.get_level_values(0)
        results.columns = ['Method', 'Weighting_used','Correct_number_number_one', 'Total_number']
        results['Perc_Correct'] = (results['Correct_number_number_one'].astype(float)/results['Total_number'].astype(float))*100
        print("Results from relevance tests: How many of the words are correctly suggested as top 1?")
        print(results)
