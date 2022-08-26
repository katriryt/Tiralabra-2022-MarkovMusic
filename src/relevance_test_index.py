from select import select
from utilities.relevance_test_script import RelevanceTests


class Main:
    test_set = RelevanceTests()

    test_set.run_tests()
    test_set.calculate_result_frequencies()
    test_set.calculate_result_top_1_frequencies()


if __name__ == "__main__":
    relevance_testing = Main()
