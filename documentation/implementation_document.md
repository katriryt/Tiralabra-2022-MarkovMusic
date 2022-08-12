# Implementation document

## Project structure

Overall program structure with high level architectural pictures to be added. 

## Implemented time and space complexities

Time and space complexities (e.g. big-O analysis of pseudo code) to be added.

Please note that as the project is not focused on applications' performance, comparative performance and complexity analysis are not done.

## Possible flaws and improvements

Possible flaws and ideas for improvements and further development areas to be added.

## Sources

Multiple sources of data, articles to understand the different algorithms, and examples for implementation of the algorithms have been used. Please find the most relevant below.

### Data

Baseline for the **English language words** used in the application is provided by Princeton University's [WordNet](https://wordnet.princeton.edu/), which consists of ~150,000 commonly used English words. This application is developed complying with the [WordNet 3.0 license](https://wordnet.princeton.edu/license-and-commercial-use) that maintains the copyright with the Princeton University. Please see the copyright text below. 

Frequencies for the words used in the application are based on analysis of texts in the [British National Corpus XML Edition](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2554), downloaded from the Oxford Text Archive. (Source: BNC Consortium, 2007, British National Corpus, XML edition, Oxford Text Archive, http://hdl.handle.net/20.500.12024/2554.) Use of this database is restricted and licensed under [BNC User Licence](http://www.natcorp.ox.ac.uk/docs/licence.html). As a result, no data directly from the database is shared here; only frequencies calculated based on the texts are used in this application. Similar analysis of data is available at [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists). BNC containts texts with ~100,000,000 words from both written and spoken English from the beginning of the 1990s.

In total, this application's dictionary consists of ¨150,000 words. ~57,000 of these words have frequency data available; for the rest the frequency is assumed to be 1. When the full dictionary is limited only to words consisting of characters in the English alphabet, the application handles ~77,000 words on a continuous basis.

Sources for misspelled English words used in the automated tests to be added.

### Distance metrics

Approach for calculating the distance metrics follows [Damerau (1964)](https://dl.acm.org/doi/abs/10.1145/363958.363994). There are a few minor differences, though. For example, while Damerau(1964) limits the spellchecking to words longer than 3 characters, and checks only high occurrency words from the dictionary for words with 4-6 characters, no such limitations are needed here, as computer's calculation power is nowadays higher. 

In the implementation, multiple sources have been studied. The most important have been: [Wikipedia: Damerau-Levenhstein distance (2022)](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)), [Wikipedia: Wagner-Fischer algorithm article (2022)](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)), [Wikipedia: Levenshtein distance (2022)](https://en.wikipedia.org/wiki/Levenshtein_distance), and examples of distance metrics calculation and implementation from [Jensen (2022)](https://www.lemoda.net/text-fuzzy/damerau-levenshtein/index.html), [Grashchenko (2021)](https://www.baeldung.com/cs/levenshtein-distance-computation), and [Norvig (2016)](http://norvig.com/spell-correct.html).

In the keyboard heuristics, QWERTY US keyboard is used as the baseline keyboard, because QWERTY is the most widespread layout in use (source: [Wikipedia: QWERTY, (2022)](https://en.wikipedia.org/wiki/QWERTY). US variant is used, because there is no need for regional variants (only English alphabets are allowed in the application). Examples to consider keyboard distances was provided by [Burton, 2002](https://metacpan.org/pod/String::KeyboardDistance).

### Trie data structure

Comments to be added.

### Other

Comments to be added.

### Key licenses

Please note that the English words used in the application are provided by the **Princeton University's [WordNet](https://wordnet.princeton.edu/)** based on the following copyright: 

WordNet 3.0 license: (Download)

WordNet Release 3.0 This software and database is being provided to you, the LICENSEE, by Princeton University under the following license. By obtaining, using and/or copying this software and database, you agree that you have read, understood, and will comply with these terms and conditions.: Permission to use, copy, modify and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database and documentation, including modifications that you make for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS" AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS. The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database. Title to copyright in this software, database and any associated documentation shall at all times remain with Princeton University and LICENSEE agrees to preserve same.