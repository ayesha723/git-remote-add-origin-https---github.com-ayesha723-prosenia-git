x = 'Hello hy ' 
try:
    num=int(x)
except ValueError:
    num=987654321

#This will print 987654321 in except
print ("Series", +num)
