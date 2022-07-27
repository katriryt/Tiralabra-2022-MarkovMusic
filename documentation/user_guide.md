# User guide

## Introduction 

Application requires using Python ^3.8.

## Installing the application 

Install dependencies with the following command: 

```bash
poetry install
```

## Commands on the command line 

Please see the relevant commands below.

### Running the application 

Start the application with the following command: 

```bash
poetry run invoke start
```

### Testing

Tests can be run with the following command: 

```bash
poetry run invoke test
```

### Test coverage 

An HTML-format test coverage report can be generated with the following command:

```bash
poetry run invoke coverage-report
```

The report is generated in the _htmlcov_ folder.

### Pylint

Checks as defined by .pylintrc can be implemented with the following command: 
```bash
poetry run invoke lint
```

### autopep8 formatting

Formats code according to pep8 standard: 
```bash
poetry run invoke format
```

## Using the application

To be added

## Other comments

To be added