#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2020/1/31
by Charles Huang

ThinkPython2e - Excercise 5.2
The function can ask for input intergers to be applied to the function, which
test if Fermat's Last Therorem works. Then print out response.

"""
def check_fermat(a,b,c,n):
    """
    First check if a,b,c are positive (as stated in the theorem). Then check if
    the therom works.
    """
    if a>0 and b>0 and c>0:        
        if n > 2 and a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
           print("No, that doesn't work.") 
    else:
        print("No, that doesn't work.")
        
def prompt_check_fermat():
    """
    Ask for a,b,c and n one by one. Take them as input, and trasfer them into
    intergers, then apply to the function.
    """
    print("Please enter a,b,c and n one by one to test the Fermat's Last Theorem.")
    inputa = input("please enter interger a.\n")
    inputb = input("please enter interger b.\n")
    inputc = input("please enter interger c.\n")
    inputn = input("please enter interger n.\n")
    check_fermat(int(inputa),int(inputb),int(inputc),int(inputn))

# Result    
prompt_check_fermat()
