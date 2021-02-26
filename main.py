from wrapper import BytesToBits

client = BytesToBits()

print(client.get_meme().title)

print(client.get_speedtext())

print(client.get_word())

madlib = client.get_madlib()

print(madlib.substitute(madlib.get_responses()))

