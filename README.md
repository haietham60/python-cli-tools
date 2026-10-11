# python-cli-tools

A collection of small Python command-line tools.

This repository is a personal project created to practice Python, command-line programs, code organization and clean documentation.

## Tools

### Text Analyzer

A simple command-line tool that analyzes a text and displays:

- number of characters
- number of words
- number of lines
- most common word

## Usage

```bash
python3 text_analyzer/text_analyzer.py "Python is cool and Python is useful"
```

Example output:

```text
==============================
        Text Analyzer
==============================

Characters       : 36
Words            : 7
Lines            : 1
Most common word : python

==============================
```

You can also test multiple lines with:

```bash
python3 text_analyzer/text_analyzer.py $'hello\nworld\npython'
```

## Skills practiced

- Python basics
- Functions
- Dictionaries
- String manipulation
- Command-line arguments
- Code formatting with flake8
- Type checking with mypy

## Status

First version completed.

More tools will be added later.
