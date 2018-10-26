# qwerty_word.py
from sys import argv
print("Programmed by SM")
word = argv[1]
change_word = word.lower()
set_the_word = set(change_word)
qwerty_letters = ("qwertyuiop").split()
letters = set("qwertyuiop")
if set_the_word <= letters:
    print("{} is a Qwerty word.".format(word))
else:
    print("{} is not a Qwerty word.".format(word))
