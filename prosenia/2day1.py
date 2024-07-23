number = int (input("Enter a number to ckeck it :"))

is_positive=number>0
is_negative=number<0
is_zero=number==0

if(is_positive):
    print("The number is positive:")
elif(is_negative):
    print("The number is negative :")
else:
    print("The number is zero")
