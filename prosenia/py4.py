print("***CALCULATOR***")
print("**123**")
print("**456**")
print("**789**")

num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
op= input ("Enter any operator + , - , / , * :")

if op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
else :
    print("Syntax Error")