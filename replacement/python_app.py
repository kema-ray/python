#!/usr/bin/python3
def replace_word():

    str = "hello my name is rachel"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement:")
    print(str.replace(word_to_replace,word_replacement))

replace_word()