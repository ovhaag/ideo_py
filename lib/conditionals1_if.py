#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
condtionals: if statement

@author: ovinci
"""

def is_seq(small, medium, large):
    """chained_comparison""" 
    #
    # harmful: explicit chain with "and"
    # ideomatic:  chained_comparison (direct, without and)
    if small <= medium <= large:
        return True 
    
def note_for(flag):
    """ternary_operator_replacement"""
    #
    # Python has no ternary operator (e.g. “x ? True : False”), so
    # ideomatic: use if, else
    note = 'flag was true' if flag else 'flag was false'
    return note

def word_in_text(word, text):
    """use in"""
    #
    # harmful: compound if
    # ideomatic: use "in"
    words = text.split(' ')
    return word in words

def main():
    s, m, l = 1, 22, 333
    up = is_seq(s, m, l)
    note = note_for(up)
    found = word_in_text("true", note)
    if found:
        print("happy")
    else: 
        print("sad")
        
if __name__ == '__main__':
    main()
    