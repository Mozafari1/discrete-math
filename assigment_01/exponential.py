import math

a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
p = int(input("Enter value for P: "))

def polynom(x, y,n):
    while(y):
        x,y = (x**n - x*y**n-1)%n
    

    return x
print("The polynomial function is: ",end=" = ")
print(polynom(a,b,p))
