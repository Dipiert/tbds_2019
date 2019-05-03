#!/usr/bin/python3

import cProfile, pdb, pstats, io
from string import ascii_uppercase as au, ascii_lowercase as al

def profile(fnc):
    """A decorator that uses cProfile to profile a function"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner

@profile
def rotate(text, key):
    #pdb.set_trace()
    result = ""
    for letter in text:
        if letter in au:
            result += shiftletter(letter, key, au)
        elif letter in al:
            result += shiftletter(letter, key, al)
        else:
            result += letter
    return result

@profile
def shiftletter(letter,key,lst):
    newpos = (lst.index(letter) + key) % len(lst)
    return lst[newpos]

if __name__ == '__main__':
    print(rotate('Hola pdb', 13))
