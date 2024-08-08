# wtok: rebalance training sets for whisper

[![PyPI](https://img.shields.io/pypi/v/wtok.svg)](https://pypi.org/project/wtok/)
[![Changelog](https://img.shields.io/github/v/release/proger/wtok?include_prereleases&label=changelog)](https://github.com/proger/wtok/releases)
[![Tests](https://github.com/proger/wtok/workflows/Test/badge.svg)](https://github.com/proger/wtok/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/proger/wtok/blob/master/LICENSE)

Count and truncate text based on tokens one sentence at a time

## Background

Whisper models conditional distributions of a token given a sequence of past tokens

This tool can count tokens, using OpenAI's [tiktoken](https://github.com/openai/tiktoken) library.

It can also truncate text to a specified number of tokens.

## Installation

Install this tool using `pip`:
```bash
pip install wtok
```

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

```bash
cd wtok
python -m venv venv
source venv/bin/activate
```

Now install for editing:

```bash
pip install -e .
```
