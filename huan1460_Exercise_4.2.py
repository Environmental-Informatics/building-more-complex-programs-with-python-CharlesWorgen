# -*- coding: utf-8 -*-
"""
2020/1/31
by Charles Huang

ThinkPython2e - Excercise 4.2
The function can accept four arguments (turtle object, number of petals,
radius/length of the petal,and angle/width of the petal) to draw a flower.

"""
import turtle
import math

bob = turtle.Turtle() # Assign turtle to object bob
   
def polyline(t,n,length,angle):
    """
    Draws n line segment with the given length and
    angle between them. t is the turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
           
def arc(t,r,angle):
    """
    Draws an arc using the turtle t with r as radius and assigned angle.
    The segements required for the polyline fucntion is calculated by the
    arclength.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n,step_length,step_angle)
    
def petal(t,r,angle):
    """
    Draws a petal by calling the arc function again after flipping it.
    """
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)
        
def flower(t,n,r,angle):
    """
    n is the number of petal required.
    """
    for i in range(n):
        petal(t,r,angle)
        t.lt(360.0/n)

# Result
flower(bob,7,100,360/7)

flower(bob,10,80,80)

flower(bob,20,180,18)

turtle.mainloop()

