# Weekly report: Week 1

## Actions taken during this week

During this week I 
* Went through the course materials
* Participated in the lecture starting the course
* Studied approaches for four different ideas for the project and how to implement them
    * Use of Markov chains to create music
    * Recognition of hand written numbers 
    * A variation of a translator for languages using [Cooke-Young-Kasami algorithm](https://materiaalit.github.io/intro-to-ai/part5/) to identify whether texts are written in English, and 
    * A spell checker for the English language
* Decided to develop an application for a spell checker for the English language in Python, using trie data structure and applying Damerau-Levenhstein distance
* Studied further details how to implement a spell checker
* Wrote the first draft of the project specification document
* Wrote the weekly report
* Created the project in GitHub and registered in Labtool

## Project progress

I will start the coding of the application next week. I think I have a fairly good idea for the overall outline of the application. Also, I have good reference materials to understand the trie data structure, the Damerau-Levenhstein distance, and the Wagner-Fischer algorithms in detail.

## Learnings from the week

During this week I learned a lot. I have not previously generated music digitally, so it was good to get a first look on the complexities related to it. I am somewhat familiar with the algorithms related to the recognition of hand written numbers as well as recognizing the grammaire of a particular language, but it was good to review how an application could be developed in these areas.

Regarding the two last options, I learned about
* The digitally available English language corpi and dictionaries and their copyrights
* Logic and high level implemenation of the trie data structure (I am not familiar with this data structure previously)
* Logic of and high level implementation for calculating the Damerau-Levenhstein distance (this is a new approach for me as well)

Regarding the task at hand, there are plenty of libraries available for implementing a spellchecker in Python. However, building this capability from scratch will require a lot of work.

## Unclear and/or problematic areas

I think I have a fairly good idea about calculating the Damerau-Levenhstein distance, and the implementation of the trie data structure. I am, however, somewhat concerned about the speed of the application - the amount of data is large, and I am not sure whether I can make the algorithms efficient enough. The approach to tackle this is by starting with the implementation of these two to have enough time for guidance and potentially testing alternative approaches to improve the efficiency.

Further, assuming that the above two can be completed, I am not sure what would be the best way to suggest the options of the corrected word for the user. In the project specification document, I outlined two alternative approaches (show full list of alternatives or show the most likely word), of which especially the latter one would require calculating the probabilities from a full English language corpus. I am yet undecided whether to use conditional or unconditional probabilities in the suggestions to ensure needed effiency in the application (unconditional is the most probable approach).

It would be great to get feedback regarding the project specification document in general, whether the approach sounds reasonable and feasible. Also, any tips on the points outlined above would be appreciated.

## Next steps

Next week, I will:
* First make an implementation of the generation of words based on Damerau-Levenhstein (one distance) with Wagner-Fischer algorithm for one word
* Then I will try to make the operations for the trie data structure, testing the structure
* If time allows, I will start cleaning up the WordNet data, so that words can be added to the application's dictionary

Other tasks during next week include:
* Start documenting the program in the user guide (Python Docstrings and instruction for opening and running the app)
* Start testing for the methods and classes done (unittest)
* Show test status in the Git project (codecov)
* Configure style checker (Pylint)
* Update weekly report

## Working hours during the week

During this week I worked ~17 hours in the project.





