# -*- coding: utf-8 -*-
"""
2020/1/31
by Charles Huang

ThinkPython2e - Excercise 7.1
The function can take in an interger and calculate the square root from 1 to
that interger using the calculating method in the text and the function in math.
It also provides the differences between such two methods.

"""
import math

def mysqrt(a):
    """
    The square root function in the text. x is not required as argument, so
    there is -0.5 to make it work for range starting at 1.0. The true/return 
    value is given as if the estimated result does not change any more.
    """
    x = a-0.5
    while True:
        y = (x+a/x)/2
        if abs(y-x) < 0.0000001:
            break
        x = y
    return y

def test_square_root(max):
    """
    The function can take in the maximum interger in the range, and calculate 
    the mysqrt, the math,sqrt and the difference between them for each interger.
    """
    print("a","mysqrt(a)","math.sqrt(a)","diff")
    for a in range(1,max):
        print(float(a),mysqrt(a),math.sqrt(a),abs(mysqrt(a)- math.sqrt(a)))
        
# Result    
test_square_root(9) 
   
    
