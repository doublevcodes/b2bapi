# B2B API

API Wrapper in Python For the BytesToBits API

# Classes

## *b2bapi*.BytesToBits()

### __Methods__

#### `*b2bapi.BytesToBits()*.get_word()`

This method `GET`s a random word from the:
`https://api.bytestobits.dev/word` endpoint

It returns a `Word` object

#### `*b2bapi.BytesToBits()*.get_meme()`

This method `GET`s a random meme from a random subreddit using the:
`https://api.bytestobits.dev/meme` endpoint

It returns a `Meme` object

#### `*b2bapi.BytesToBits()*.get_speedtext()`

This method `GET`s a random selection of text from the:
`https://api.bytestobits.dev/speedtext2` endpoint

It returns a `Speedtext` object

#### `*b2bapi.BytesToBits()*.get_madlib()`

This method `GET`s a random madlib to use by requesting the:
`https://api.bytestobits.dev/madlibs` endpoint

It returns a `Madlib` object