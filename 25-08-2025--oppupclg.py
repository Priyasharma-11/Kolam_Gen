"""write a program to check given string is palindrome or not without using any predefined function"""
str=input("enter a string\n").lower()
length=len(str)
str_rev=''
while(length>0):
    str_rev=str_rev+str[length-1]
    length=length-1
if(str==str_rev):
     print("yes it is palindrome")
else:
     print("no")
"Type-casting"
print(int(12.e38))#float
print(int(True))#boolean
#print(int(10+2j))#complex
#print(int("face"))#string
print(int("145"))#string
#comple->int,=>not possible ; string when converted to int should be in base 10 otherwise not possible

print(float(10))#10.0
#print(float("10+2j))#error Typeerror:float()argument must be a string or a real number
print(float(True))#1.0
print(float(10))
print(float(10.8))
#print(float("adypu"))#erroe ValueError: could not convert string to float :'adypu'
print(float(0b1101))
print(float(0o123))
print(float(0xface))
#print(float("0b1101"))ValuError : could not convert string to float : '0b1101'

print(complex(10))
print(complex(0b111))
print(complex(0o123))
print(complex(0xface))
print(complex(10.8))
print(complex(12e5))
print(complex(True))
print(complex("10"))
print(complex("10.89"))
#print(complex("0b1101"))ValueError: complex() arg is a malformed string
print(complex(10,10))
print(complex(10.8,10.8))
print(complex(0b111,10))
print(complex(0b111,0xface))
#print(complex('10',10))TypeError: complex() can't take second arg if first is a string

print(bool(1))#true
print(str(10))
print(str(2e10))
print(str(10+2j))
print(str(true))
print(t)


