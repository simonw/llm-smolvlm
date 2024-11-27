# llm-smolvlm

[![PyPI](https://img.shields.io/pypi/v/llm-smolvlm.svg)](https://pypi.org/project/llm-smolvlm/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-smolvlm?include_prereleases&label=changelog)](https://github.com/simonw/llm-smolvlm/releases)
[![Tests](https://github.com/simonw/llm-smolvlm/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/llm-smolvlm/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-smolvlm/blob/main/LICENSE)

SmolVLM for LLM

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-smolvlm
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-smolvlm
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
