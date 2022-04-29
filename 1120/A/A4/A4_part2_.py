from itertools import count
from operator import contains
from tkinter import W, Y
from xmlrpc.client import TRANSPORT_ERROR


class Rectangle:

    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self,x_input,y_input,w_input,h_input):
        '''num -> Rectangle
            make a Rectangle'''
        if(w_input < 0 or h_input < 0):
            print("Width or heigh can't be negative.")
        try:
            w_input > 0 and h_input > 0

            x_input = int(x_input)
            y_input = int(y_input)
            w_input = int(w_input)
            h_input = int(h_input)
        except ValueError as err:
            print("something worng.")
        if(w_input < 0 or h_input < 0):
            print("Width or heigh can't be negative.")
            return

        self.x = x_input
        self.y = y_input
        self.w = w_input
        self.h = h_input

    def height(self):
        ''''nothing -> num
            return h of a Rectangle'''
        an = self.h
        return an
    def width(self):
        ''''nothing -> num
            return w of a Rectangle'''
        an = self.w
        return an
    def x(self):
        ''''nothing -> num
            return x of a Rectangle'''
        an = self.x
        return an
    def y(self):
        ''''nothing -> num
            return y of a Rectangle'''
        an = self.y
        return an
    
    def __repr__(self):
        ''''nothing -> string
            return information about Rectangle'''

        return "Rectangle [x = {self.x} , y = {self.y}, width = {self.w}, height ={self.h}]".format(self=self)

    def __str__(self):
        ''''nothing -> string
            return information about Rectangle'''
        return "Rectangle [x = {self.x} , y = {self.y}, width = {self.w}, height ={self.h}]".format(self=self)

    def contains(self,x_input,y_input):
        ''''num -> bool
            check if a point is in a Rectangle'''
        try:
            x_input = int(x_input)
            y_input = int(y_input)

        except ValueError as err:
            print("something worng.")
            return

        if(x_input > self.x and x_input < self.w):
            if(y_input < self.y and y_input > (self.y - self.h)):
                return True
        return False
    
    def union(self,rect):
        ''''Rectangle -> Rectangle
            union two Rectangle no matter where they are'''
        if(rect.y > self.y):
            self.y = rect.y
        else:
            pass
        if(rect.x < self.x):
            self.x = rect.x
        else:
            pass
        if(rect.w > self.w):
            self.w = rect.w
        else:
            pass
        if(rect.h > self.h):
            self.h = rect.h
        else:
            pass
        return

    def intersection(self,rect):
        ''''Rectangle -> Rectangle
            put two Rectangles together if they have touch eachother'''
        empty = Rectangle(0,0,0,0)
        lower_rect = rect.y - rect.h
        lower_self = self.y - self.h
        if(self.y < lower_rect or rect.y < lower_self):
            print("y")
            return empty
        elif(self.x > (rect.x + rect.w) or rect.x > (self.x + rect.w)):
            print("x")
            return empty
        else:
            an = self.union(rect)
            return an

    def __eq__(self, rect: object) -> bool:
        ''''Rectangle -> bool
            check if both Rectangle are same'''
        if(self.x == rect.x and self.y == rect.y and self.w == rect.w and self.h == rect.h):
            return True
        else:
            return False

r1 = Rectangle(0,5,5,5)
r2 = Rectangle(0,10,8,7)
r3 = Rectangle(-99,-99,10,10)
r4 = Rectangle(0,5,5,5)
r5 = Rectangle(0,6,6,6)
# print(r1)
# print(r1.contains(2,3))
# print(r1.contains(2,18))
# print(r1.contains(2,-18))
# print(r1.contains("dd",5))
# r1.union(r2)
# print(r1)
# print(r1.intersection(r3))
# print(r1.intersection(r5))
# print(r1)
# print(r1 == r4)
# print(r1 == r3)
    

        



        