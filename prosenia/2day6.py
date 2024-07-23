num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))

if(num1>0 and num2>0):
    print("Both are positive")

elif(num1>0 or  num2>0 ):
    print("One of two numbers is positive")

elif (num1<0 and  num2<0):
    print("Neither is positive")

else:
    print("Thatsss ittt") 