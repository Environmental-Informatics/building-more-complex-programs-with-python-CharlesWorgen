# -*- coding: utf-8 -*-
"""
2020/1/31
by Charles Huang

ThinkPython2e - Excercise 6.5
The function can calculate the largest number that divides the input
parameters a and b.

"""
def gcd(a,b):
    """
    In case b is 0 which cannot be divided. Otherwise can be calculated following
    the instruction.
    """
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def gcd_prompt():
    """
    Intergers a and b are asked as input values.
    """
    a = input("please enter interger a.\n")
    b = input("please enter interger b.\n")
    print(gcd(int(a),int(b)))

# Result
gcd_prompt()