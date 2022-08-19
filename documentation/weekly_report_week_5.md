# Weekly report: Week 5

## Actions taken during this week

This week's main focus was in relevance tests. 

During this week, I
* Developed and conducted automated tests for the accuracy of the application's suggestions
* Conducted peer review

Other tasks during this week included
* Updated testing document
* Updated implementation document
* Updated user guide
* Updated weekly report

## Project progress

The project progressed largely as planned during this week. The main target was to develop, conduct, and document automated relevance tests to see how accurate the application's suggestions were. The results were very interesting. As the overall results were quite good (application finds 70-80% of the correct words), and it seemed that adjusting the heuristics would not improve the relevance of the suggestions - neither adjusting keyboard heuristics nor the use of freqeuencies would help to improve relevance - I concluded not to tweak the calculation of the heuristics any further. Furthermore, as the relevance tests took longer more time than anticipated, I did not implement the stretch target to refactor/clean-up the code, or update the user guide.

## Learnings from the week

From the peer review, I had a chance to learn a bit about regular expressions, using shunting yard algorithm. In my own work, it was very interesting to conduct relevance tests, and to see how the Damerau-Levenshtein distance metric compared to other distance metrics used, and to see the impact of heuristics used. The conclusions are in the testing document. It seems that if one wanted to make the algorithm more accurate, one would need especially expand the dictionary. Further, as the focus of the work has been in learning the algorithms and the data structures - not in optimizing speed of the application - the algorithm currently does not implement measures to speed up the search, it seems that when the words are long, the algorithm is quite slow.

## Unclear and/or problematic areas

Based on results from this week, and the received feedback, I do not plan to do further changes in the application's core functionalities or tests. Next week's focus will be in finalizing documentation, responding to peer reviews, and preparing the demo. 

## Next steps

Next week, I will
* Respond to feedback from peer reviews
* Clean-up the code (currently a lot of comments in the code base)
* Prepare demo for week 7

Other tasks during next week include
* Conduct second peer review
* Finalize user guide 
* Finalize testing document (update coverage report)
* Finalize implementation document (add estimation of implemented time and space complexities)
* Update weekly report

## Working hours during the week

During this week I worked ~13 hours for the project (cumulative hours for the project are ~98 hours).