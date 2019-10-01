# Regner i Zm, for vilkårlige m
# Calculate for Zm for arbitrary number for m
print("How to use it: It takes three inputs.\nEnter an integer value for each and it will calculate it the result and shows on the screen ")
a = int(input("Enter a value of A: \n"))
b = int(input("Enter a value for B: \n"))
m = int(input("Enter a value for m: \n"))

# Addion
def ZmAddion(x, y, m):
    SUM = (x + y)%m
    return SUM

print("The arbitrary number for m is:",a+b,"mod",m,  end=" = ")
print(ZmAddion(a,b,m))

# Multiplication
def ZmMultiplication (x, y, m):
    SUM = (x*y)%m
    return SUM

print("The arbitrary number for m is as follows: ",a*b,"mod",m,  end=" = ")
print(ZmMultiplication(a,b,m))
# Subtraction
def ZmSubtraction (x, y, m):
    SUM = (x-y)%m
    return SUM

print("The arbitrary number for m is as follows: ",a-b,"mod",m,  end=" = ")
print(ZmSubtraction(a,b,m))

#   Division

def ZmDivision (x, y, m):
    SUM = (x/y)%m
    return SUM

print("The arbitrary number for m is as follows: ",a/b,"mod",m,  end=" = ")
print(ZmDivision(a,b,m))
print("Thanks to python to do our work much easier!")

