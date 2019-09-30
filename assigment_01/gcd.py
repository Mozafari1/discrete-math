
#This is a simple code to compute gcd numbers
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))
def gcd(x,y):
    while (y):
        x, y = y, x%y
        #print([y])
    return  x

print ("The gcd for A =",a, "and B =",b, end=" => \n")
print(gcd(a,b))
