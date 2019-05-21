# Wordsearch

A circle the word search game.

## Instructions to play

git clone the source code to you machine:

```
git clone https://github.com/androiddrew/wordsearch.git
```

Create a virtual environment and install the dependencies:

```
cd ./wordsearch
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then run wordsearch module:

```
python -m wordsearch
```

## Tests

To execute the tests install the dev_requirements.txt and execute the pytest runner:

```
pip install -r dev_requirements.txt
pytest 
```