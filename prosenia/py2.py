x=10
y=5

z=x/y

def divide (x,y) -> str:
    x=int(x)
    y=float(y)
    
    
    if y != 0:
        return "The division of two numbers is"
    else:
        return "Error: Division by zero is not allowed"

print (divide( x,y) , +z)