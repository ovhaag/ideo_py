#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
condtionals: for loop

@author: ovinci
"""

def print_words(text):
    """use enumerate"""
    #
    # ideomatic: use enumerate to track the index in a loop 
    words = text.split(' ')
    for index, word in enumerate(words):
        print("{index} -- {word}".format(index=index, word=word))

def main():
    print_words('few words make small texts and many ...')
        
if __name__ == '__main__':
    main()