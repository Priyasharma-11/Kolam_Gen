"""ternary operator
bitwise & operatoe
1.arithmetic(+,-,*,/,%,//,**)
2.relational(<,>,>=,<=,==,!=)
3.logical(and,or,not)
4.assignment
5.bitwise
6.ternary

fundamental datatypes and sequential datatypes
what is diffeence between mutable and immutable
what is diff btw list tuple set dictionary
6 basics operators in python
what is object reusability concept ?
"""
"""Functions
 1. function declaration and defination
 2.function call
 void welcome() - in other programming lang but not in py
 """
def welcome(str):
    return "welcome "+str
def calculator(num1,num2):
    return (num1+num2),(num1-num2),(num1*num2),(num1/num2)
print(welcome("Vinay"))
print(calculator(45,3))
re1,re2,re3,re4=calculator(46,2)
print("addition :",re1)
print("subtraction :",re2)
print("multiplication :",re3)
print("division :",re4)

def myadd(num1,*num2):
    sum=num1
    for i in num2:
       num1=num1+i
    return num1
def myadd(num1,*num2):
    print(num1)
    print(num2)
    for i in num2:
     num1=num1+i
    return num1
print(myadd(3,4,5,6,7,8,9,33,67))
"""HW
keyword variable length """
