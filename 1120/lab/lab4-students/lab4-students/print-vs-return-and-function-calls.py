def foo1(a, b):
     '''type contract looks like this:
          (number,number)->None'''
     print(a+b)

def foo2(a, b):
     '''type contract looks like this:
          (number,number)->number'''
     return a+b

def foo3(a,b):
     ''' type contract looks like this:
          (number,number)->number'''
     print("Welcome to my silly function")
     print("First I will print a +b:")
     print("a+b=", a+b)
     print("Now I will also return that value")
     return a+b

def foo4(a, b):
     '''type contract looks like this:
          (number,number)->None'''
     print(a+b)
     return

# 1st uncomment the next line and save. What will the program print when you press Run Module
foo1(5,5)
# 10

# 2nd uncomment the next line and save. What will the program print when you press Run Module 
foo2(5,5)
# 10 from the function above, this return thing is not been printed


# 3rd uncomment the next line and save. What will the program print when you press Run Module 

x1=foo1(5,5)
x2=foo2(5,5)
x3=foo3(5,5)
x4=foo4(5,5)

# # 10
# 10
# Welcome to my silly function
# First I will print a +b:
# a+b= 10
# Now I will also return that value
# 10

# 4th uncomment the following 8 lines, and save. What will the program print when you press Run Module 

print("x1=", x1)
print("type of x1 is ", type(x1))
print("x2=", x2)
print("type of x2 is ", type(x2))
print("x3=", x3)
print("type of x3 is ", type(x3))
print("x4=", x4)
print("type of x4 is ", type(x4))

# 10
# 10
# Welcome to my silly function
# First I will print a +b:
# a+b= 10
# Now I will also return that value
# 10
# x1= None
# type of x1 is  <class 'NoneType'>
# x2= 10
# type of x2 is  <class 'int'>
# x3= 10
# type of x3 is  <class 'int'>
# x4= None
# type of x4 is  <class 'NoneType'>

# 5th uncomment the following 2 lines, and save. What will the program print when you press Run Module 

num1=x2*x3
print("x2*x3=", num1)

# 10
# 10
# Welcome to my silly function
# First I will print a +b:
# Now I will also return that value
# x1= None
# type of x1 is  <class 'NoneType'>
# x2= 10
# type of x2 is  <class 'int'>
# x3= 10
# type of x3 is  <class 'int'>
# x4= None
# type of x4 is  <class 'NoneType'>
# PS E:\daima\1120\lab4-students\lab4-students>  e:; cd 'e:\daima\1120\lab4-students\lab4-students'; & 'C:\Users\lenovo\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\lenovo\.vscode\extensions\ms-python.python-2022.0.1814523869\pythonFiles\lib\python\debugpy\launcher' '59284' '--' 'e:\daima\1120\lab4-students\lab4-students\print-vs-return-and-function-calls.py' 
# 10
# 10
# Welcome to my silly function
# First I will print a +b:
# a+b= 10
# Now I will also return that value
# 10
# x1= None
# type of x1 is  <class 'NoneType'>
# x2= 10
# type of x2 is  <class 'int'>
# x3= 10
# type of x3 is  <class 'int'>
# x4= None
# type of x4 is  <class 'NoneType'>
# x2*x3= 100

# 6th uncomment the following 2 lines, and save. What will the program print when you press Run Module 
num2=x1*x2
print("x1*x2=", num2)
# bug can't times a NoneType with int
