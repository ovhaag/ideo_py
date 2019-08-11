#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
condtionals: if statement

@author: ovinci
"""

def chained_comparison(small, medium, large):
    # harmful
    # if x <= y and y <= z:
    #     return True 
    #
    # ideomatic
    if small <= medium <= large:
        return True 
    
def main():
    c = chained_comparison(1, 12, 123)
    print(c)
    
    
if __name__ == '__main__':
    main()