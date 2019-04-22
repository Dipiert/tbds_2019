#!/usr/bin/python3

import pdb
from string import ascii_uppercase as au, ascii_lowercase as al


def rotate(text, key):
    pdb.set_trace()
    result = ""
    for letter in text:
        if letter in au:
            result += shiftletter(letter, key, au)
        elif letter in al:
            result += shiftletter(letter, key, al)
        else:
            result += letter
    return result

def shiftletter(letter,key,lst):
    newpos = (lst.index(letter) + key) % len(lst)
    return lst[newpos]

if __name__ == '__main__':
    rotate('Hola pdb', 13)
