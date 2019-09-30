# Regner i Zm, for vilkårlige m
a = int(input("Enter a value of A: \n"))
b = int(input("Enter a value for B: \n"))
m = int(input("Enter a value for m: \n"))

# Addion
def ZmAddion(x, y, m):
    SUM = x + y
    SUM = SUM% m
    return SUM

print("Det vilkorlige m er:",a+b,"mod",m,  end=" = ")
print(ZmAddion(a,b,m))

# Multiplication
def ZmMultiplication (x, y, m):
    SUM = x*y
    SUM = SUM%m
    return SUM

print("Det vilkorlige m er:",a*b,"mod",m,  end=" = ")
print(ZmMultiplication(a,b,m))
# Subtraction
def ZmSubtraction (x, y, m):
    SUM = x-y
    SUM = SUM%m
    return SUM

print("Det vilkorlige m er:",a-b,"mod",m,  end=" = ")
print(ZmSubtraction(a,b,m))

#   Division

def ZmDivision (x, y, m):
    SUM = x/y
    SUM = SUM%m
    return SUM

print("Det vilkorlige m er:",a/b,"mod",m,  end=" = ")
print(ZmDivision(a,b,m))

