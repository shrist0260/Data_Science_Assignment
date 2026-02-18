# write a program that asks for three number and prints the largest using a function

a= int(input("One"))
b= int(input("two"))
c= int(input("three"))
def largest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
largest(a,b,c)