# Weekly report: Week 4

## Actions taken during this week

During this week, I targeted to get the core functionalities for the application in place. This was largely achieved. 

During the week, I 
* Added search functionalities to the trie data structure, returning full list of words in the dictionary, with and without other data related to them (e.g. frequencies for the words)
* Following the spell checking process in [Damerau (1964)](https://dl.acm.org/doi/abs/10.1145/363958.363994), added functionality to go through the application's dictionary, and suggest alternative words to the user based on the shortest distance (alternative calculation methods (Levenshtein, Optimal string alignment, and Damerau-Levenshtein distance metric) added previous week)
* Added heuristic based on between keyboard characters' distance to make a more accurate estimate for the distance metrics mentioned above
* Calculated frequencies for different English words based on data from British National Corpus, and added those frequencies to the words from Princeton University's WordNet used in the application
* Made first draft of the suggestion for misspelled words based on both distance metrics (with and without keyboard heuristic incorporated) and word frequencies
* Added heuristics and frequency based suggestions to the UI
* Polished UI and added checks allowing only the use of English alphabets in the spellchecked words

Other tasks 
* Developed tests for the aforementioned functionalities
* Updated the testing document
* Started writing the implementation document
* Updated weekly report
* Started manually testing for the accuracy of suggestions (based on instructor's feedback, performance/speed testing has not been prioritized)

## Project progress

The project progressed largely as planned during this week. The target was to get the core functionalities in place, and to get most of the work for both weeks 4 and 5 done, because during next week I will have only limited time to work on the project. As a result, I pushed to get stretch goals done as well. The only bigger area that remains, is conducting tests for accuracy of suggestions automatically, and based on those outputs, adjust the keyboard heuristics and the selection of suggestions for the misspelled words based on keyboard heuristics and word frequencies.

## Learnings from the week

[Damerau (1964)](https://dl.acm.org/doi/abs/10.1145/363958.363994) outlined a fairly straightforward process for spell checking, which was fairly easy to follow. Bigger challenges were related to the keyboard heuristics: their calculation as such was pretty clear, but I want to conduct tests whether the current heuristics results in good suggestions (based on manual tests, it seems to work fairly well). 

Calculating the frequencies for the English words was a bit tedious, and the main new skills developed were related to cleaning the data, and calculating frequencies efficiently from a large amount of data. As British National Corpus data is copyright protected, these steps are not shared in the project documentation.

Combining the two approaches - keyboard heuristics and the word frequencies - to one relevant suggestion requires a bit more thinking, depending on the test results.

## Unclear and/or problematic areas

Next week's word will center around testing the accuracy of the suggestions in larger scale and adjusting the heuristics and combined metrics (keyboard heuristics and word frequencies) accordingly.

## Next steps

Next week, I have limited time to work on the application, and I will focus on
* Conducting automated tests for the accuracy of the application's suggestions
* Adjusting the keyboard heuristics and the use of the combined metrics accordingly
* (Stretch target) refactor/clean-up the code in a few areas

Other tasks during next week include
* Conduct peer review
* Update testing document
* Expand implementation document
* Update weekly report
* (Stretch target) Update used guide

## Working hours during the week

During this week I worked ~27 hours for the project (cumulative hours for the project are ~85 hours).
