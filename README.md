# B2B API

API Wrapper in Python For the BytesToBits API

# Classes

## *b2bapi*.BytesToBits()

### **Attributes**:

None

### __Methods__

#### `BytesToBits().get_word()`

This method `GET`s a random word from the:
`https://api.bytestobits.dev/word` endpoint

It returns a `Word` object

#### `BytesToBits().get_meme()`

This method `GET`s a random meme from a random subreddit using the:
`https://api.bytestobits.dev/meme` endpoint

It returns a `Meme` object

#### `BytesToBits().get_speedtext()`

This method `GET`s a random selection of text from the:
`https://api.bytestobits.dev/speedtext2` endpoint

It returns a `Speedtext` object

#### `*b2bapi.BytesToBits()*.get_madlib()`

This method `GET`s a random madlib to use by requesting the:
`https://api.bytestobits.dev/madlibs` endpoint

It returns a `Madlib` object

## *b2bapi*.Word()

### **Attributes**:
1. *Word()*.**word** => A `str` containing the word

### __Methods__:
None
