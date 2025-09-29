namenput("enter your name :")
age=int(input("enter your age:"))
print(name,"your age is",age)
print("Hello" , name,"you are welcome")
"""current_year=int(input("enter current year :"))
birth_year=current_year-age
print(name,"your age is ", age , "and your birth year is ",birth_year)"""
birth_year=int(input("enter your birth year :"))
current_year=birth_year+age
print(name,"your age is ", age , "and your current year is ",current_year)



"""Armstrong Numbers"""
num=input("Enter one number :\n")
"""Input function by default take data in string format """
le=len(num)
sum=0
for i in num:
    sum=sum+((int(i)**le))
print ("Number is arm" if(num==sum) else "Number is not armstrong")#ternary operator
"""
Reverse the number , without usingslicking operation"""
num=input("enter number:\n")
#print(num[::-1]
rev=""
for i in num :
  rev=i+rev
print(f"reverse number is {rev}")


"""write a code to check given number is even or odd without using modulus(%)"""
num=int(input("enterone number \n"))
print(4&1)
print(5&1)
