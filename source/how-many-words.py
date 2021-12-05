#!/bin/python3
import re


#
# Complete the 'howMany' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sentence as parameter.
#
def howMany(sentence):
    strip = """,.?!"""
    _sentence = ""
    for word in sentence:
        if word not in strip:
            _sentence = _sentence + word
    list_of_words = _sentence.split(" ")

    pattern = "^[a-zA-Z-]+"
    list_of_words = [
        item
        for item in list_of_words
        if item != "" and re.fullmatch(pattern, item) and not item.isdigit()
    ]

    # print(list_of_words)
    return len(list_of_words)


if __name__ == "__main__":
    sentence = input()

    result = howMany(sentence)

    print(result)
