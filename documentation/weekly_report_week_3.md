# Weekly report: Week 3

## Actions taken during this week

During this week, I
* Cleaned the WordNet data for English words (~150,000 words)
* Added English words to the trie structure (application's dictionary)
* Added capability in the UI to check whether words / phrases written by the user are in the application's dictionary, and, hence, are in English (checks individual words)
* In case the words written by the user were not in the application's dictionary, added capability to suggest alternative English words
* Added ability to add frequencies for the words in the trie data structure (default frequency: 1)
* NEW ITEM: Added methods to calculate Levenshtein, optimal string alignment, and Damerau-Levenshtein distances between two words (not yet incorporated to the UI)

Other tasks during this week included
* Developed tests for the aforementioned functionalities
* Started writing the testing document
* Updated weekly report

## Project progress

Project progressed largely as planned during the week. Stretch target to calculate frequencies for the words in the dictionary remained as a target, rest of the targets for the week were achieved. Based on instructor's feedback, I also added methods to calculate e.g. Damerau-Levenshtein distance. These methods are not, however, yet incorporated to the UI, so that they, too, would suggest potentially correct English words to replace the misspelled words.

Application has now the core functionality of English words added in trie data structure, and the ability to check whether the words are in fact English or not. At this point, the spell checker only returns to the user a list of words that are in English and one Damerau-Levenshtein distance away from the wrongly spelled English word (assuming that the word is available in the WordNet based dictionary).

## Learnings from the week

Trie data structure seems to be a very efficient and flexible way of saving, and searching for information. Populating the data structure was actually quite quick after last week's efforts of setting up the main methods and testing them. Also cleaning the WordNet data proved to be faster than expected. Based on this, there seems to be capacity to try out more advanced methods in the application's core capability of suggesting alternative words.

Following instructor's guidance, I also went deeper to the Damerau-Levenshtein distance metric, and added alternative ways of calculating the distance. This brought a lot of ideas how to improve the suggested words, and also how to test the accuracy of the suggested words.

## Unclear and/or problematic areas

Next week's challenge will be in incorporating the different distance metrics to actually suggest English words in a better way to the user, and developing and testing a heuristic to calculate the "cost" of travelling from one key to another, as well as cleaning the corpus data efficiently to calculate the frequencies for the words in the application's dictionary. The idea is to eventually incorporate both metrics (frequency of suggested words in the English language, and heuristic to estimate the cost of distance) to improve the relevance of suggested words for the user.

## Next steps

Next week, I will
* Following [Damerau (1964)](https://dl.acm.org/doi/abs/10.1145/363958.363994), add functionality to go through the application's dictionary, and suggest alternative words to the user based on the shortest distance (see alternative calculation methods above) 
* Strive to make a heuristic to make a more accurate estimate for the distance
* Stretch target: Start developing a heuristic to provide better suggestions for the user, based on e.g. aforementioned frequencies or other metrics (e.g. distance of keys in a keyboard from the typed word) OR
* Stretch target: Expand testing for "correct" words (how accurate are the suggestions)

Other tasks during next week include
* Develop tests for the aforementioned functionalities, expand the testing document
* Start writing the implementation document
* Update weekly report

## Working hours during the week

During this week I worked ~24 hours for the project (stretch targets from week 4 done as well).