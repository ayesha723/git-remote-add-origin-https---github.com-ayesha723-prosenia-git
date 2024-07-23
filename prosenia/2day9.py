hours_worked=int(input("Enter the number of hours worked "))
hours_rate=int(input("Enter the hourly rate "))

overtime_rate= hours_rate*1.5

if(hours_worked<40):
    gross_pay = hours_worked * hours_rate

else:
    overtime_hour = hours_worked - 40
    gross_pay = (hours_rate * 40 ) + ( overtime_rate *overtime_hour)

print ("Gross pay of employee is " , +gross_pay , "$")
