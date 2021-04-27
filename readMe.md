# [Hangman](https://en.wikipedia.org/wiki/Hangman_(game))

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.

## GUI

I created this game with [Tkinter](https://docs.python.org/3/library/tkinter.html)   

```python
from tkinter import *
import tkinter
```

![alt text](https://github.com/hoco1/Hangman/blob/main/images/Screenshot%202021-04-27%20174753.jpg?raw=true)

## Data

I use this dataset from this [repository](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt) of GitHub  
You are free to use any dataset I prefer to use this one because it has hard and simple words

```python
import os
import urllib.request

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/dwyl/english-words/master/'
WORDS_PATH = os.path.join('datasets','words')
WORDS_URL = DOWNLOAD_ROOT + 'words_alpha.txt'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
