# Scientific Calculator

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def arcsin(x):
    return math.degrees(math.asin(x))

def arccos(x):
    return math.degrees(math.acos(x))

def arctan(x):
    return math.degrees(math.atan(x))

def log(x, base):
    return math.log(x, base)

def factorial(x):
    return math.factorial(x)

num1=int(input("please enter your first number:"))
choice = input("Enter choice(+/-/*///**/sin/cos/tan/arcsin/arccos/arctan/log/factorial):")
num2=int(input("please enter your second number:"))

if choice == '+':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '-':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '*':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '/':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == 'sin':
    print(num1,sin(num1))
elif choice == 'cos':
    print(num1,cos(num1))  
elif choice == 'tan':
    print(num1,tan(num1))  
elif choice == 'arcsin':
    print(num1,arcsin(num1))  
elif choice == 'arccos':
    print(num1,arccos(num1))   
elif choice == 'arctan':
    print(num1,arctan(num1))
elif choice == 'log':
    print(num1,log(num1))  
elif choice == 'factorial':
    print(num1,factorial(num1))                     
else:
    print("invalid input")   
    
