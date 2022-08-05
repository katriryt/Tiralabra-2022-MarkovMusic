# Testing document

## Overview of the tests

Application has been tested both manually and automatically with unit and integration tests with unittest.

## Unit and integration tests

Unit and integration tests are automated and cover all classes, excluding UI (very preliminary version available), following common approach in the faculty's classes. 

Unit and integration tests can be run with the following command: 

```bash
poetry run invoke test
```

Unit and integration tests are also automatically run as part of the application's GitHub Actions CI pipeline when the the application is pushed to the GitHub repository. Results are visible in codecov. 

![GitHub Actions](https://github.com/katriryt/Tiralabra-2022-VerbumReprehendo/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/katriryt/Tiralabra-2022-VerbumReprehendo/branch/main/graph/badge.svg?token=2QWJAKX877)](https://codecov.io/gh/katriryt/Tiralabra-2022-VerbumReprehendo)

### Services (core functionality)

`SpellCheck` class is tested with [TestSpellCheck](../src/tests/spell_check_test.py) test class. Inputs used are strings of realistic words, as the program at the moment simply rejects words which cannot be identified as proper English words.

### Repositories Classes

Repository classes `TrieNode` and `Trie` are tested with [TestTrie](../src/repositories/trie.py) test class. `English Dictionary` is covered through other test classes' tests. 

### Test coverage

An HTML-format test coverage report can be generated with the following command:

```bash
poetry run invoke coverage-report
```

The report is generated in the _htmlcov_ folder.

Please see the overall test coverage below. 

![](./pictures/coverage_report.png)

Tests focus on the most relevant methods and features.

## System testing

Application's test in different operating system - Windows and Ubuntu - has been done manually. Automated tests are run on both environments.

## Other testing

Tests for application's performance (e.g. how quickly the algorithms can suggest  spellchecked words) and relevance of suggestions (e.g. comparing suggestions from the different distance metrics (Levenshtein, optimal string alignment, Damerau-Levenshtein) and based on different heuristics for misspelt words) are yet to be developed.

## Remaining quality errors

Pylint and autopep8 are used to help identifying and correcting for quality errors. At the moment, the application does not check for the user input; methods to limit errors from arising from this are yet to be put in place. 

