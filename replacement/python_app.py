#!/usr/bin/python3
# The replace() method replaces each matching occurrence of a 
# substring with another string.

def replace_word():

    str = "hello my name is rachel"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement:")
    print(str.replace(word_to_replace,word_replacement))

replace_word()