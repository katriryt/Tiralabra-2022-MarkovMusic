# Weekly report: Week 2

## Actions taken during this week

During this week, I 
* Started the implementation of the core functionalities
    * Made the first draft of the implementation of generating words based on user input and Damerau-Levenhstein (one distance) algorithm
    * Made the key operations (create trie node and structure, insert words, search words) for the trie data structure
* Made basic configurations for the project (incl. e.g. Poetry)
* Made unit tests with Pytest (unittest) for the aforementioned core functionalities
* Configured the coverage reports; test status is shown in README.md with codecov
* Configured style checkers (Pylint, autopep8)
* Started documenting the application in the user guide (instructions for opening and running the appcalitions), and with Python Docstring (focus on classes)
* Updated the weekly report (week 2)

## Project progress

Project progressed as planned during the week. Stretch target for the week (cleaning WordNet data) remained as a target, rest of the targets for the week were achieved. Application has now the core functionalities - creating alternative words for a given word and a structure where to store the English language words - in place. Based on tests, they seem to work. At this point, the spell checker only returns to the user a list of words (rather, strings) that one can generate from the text that the user typed in. It does not yet have intelligence to say which of the words user typed or the algorithm generated as English.

## Learnings from the week

During this week I learned a lot. I am not familiar with the Damerau-Levenhstein distance, the Wagner-Fischer algorithm, or the trie data structure from previous work, so it was good to see how they are implemented in practice (it seems that the implementations are easier to understand than the theory). 

Further, it was good to recap all the configurations to set up Poetry, Pytest, Pylint, codecov etc. for the project. Programs are evolving constantly, and putting the basic configurations for the project in place took a lot of time. 

## Unclear and/or problematic areas

No new concerns have come up. Next week's challenge will be to clean up the WordNet data to be used to populate the trie data structure, as well as calculating the frequencies for the different words (stretch target), and then start searching for words from the structure to check the spelling. As mentioned in previous week, it will be interesting to see whether I can make the algorithms efficient enough.

## Next steps

Next week, I will
* Start cleaning up the WordNet data, so that words can be added to the application's dictionary
* Add English words to the trie structure
* Check whether words / phrases written by the user are in the application's dictionary
* In case the words written by the user are not in the application's dictionary, try to suggest alternative words
* Stretch target: calculate and add frequencies for the words in the trie structure to improve the suggestions for the user

Other tasks during next week include
* Develop tests for the aforementioned functionalities
* Start writing the testing document
* Update weekly report

## Working hours during the week

During this week I worked ~17 hours in the project.