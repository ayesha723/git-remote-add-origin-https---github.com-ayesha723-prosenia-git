num = int(input("Enter a number to find its reverse"))

reverse_num=0

while num>0:
    remainder = num% 10
    reverse_num =reverse_num * 10 + remainder
    num = num //10 #double hash gives a int reverse

print ("The reverse is " , +reverse_num)