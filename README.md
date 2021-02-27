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

#### `BytesToBits().get_madlib()`

This method `GET`s a random madlib to use by requesting the:
`https://api.bytestobits.dev/madlibs` endpoint

It returns a `Madlib` object

## *b2bapi*.Word(word)

### **Attributes**:

1. *Word()*.**word** (`str`) => The word that the word object represents

### __Methods__:

None

## *b2bapi*.Meme(title, url, link, subreddit)

### **Attributes**
1. *Meme()*.**title** (`str`) => The title of the meme
2. *Meme()*.**url** (`str`) => The URL of the meme image
3. *Meme()*.**link** (`str`) => The URL of the actual reddit post
4. *Meme()*.**subreddit** (`str`) => The name of the subreddit the meme is from

### __Methods__:
None

## *b2bapi*.Speedtext(text)

### **Attributes**
1. *Speedtext()*.**text** (`str`) => The text that the object represents

### __Methods__:
1. *Speedtext()*.**typewriter()** (`None`) => Prints out the text to `sys.stdout`, character by character to give a typing effect.

## *b2bapi*.Madlib(title, text, no_of_questions, questions, responses = [])

### **Attributes**
1. *Madlib()*.**title** (`str`) => The title of the madlib
2. *Madlib()*.**text** (`str`) => The text currebtly held by the madlib (if this madlib was returned by the `BytesToBits().get_madlib()` method, then this text will contain placeholders)
3. *Madlib()*.**no_of_questions** (`int`) => The number of placeholders in the text
4. *Madlib()*.**questions** (`list[str]`) => A list of strikgs which describe what type of word should go in the corresponding placeholder.

### __Methods__:
1. *Madlib()*.**get_responses()** (`list[str]`) => Prompts the user in `sys.stdout` to enter a word based on each question in `Madlib().questions`.
2. *Madlib()*.**substitute()** (`str`) => Will return the text with all the placeholders filled assuming `Madlib().responses` contains the correct number of strings. Also reassigns `Madlib().text` this new filled in version of the text.