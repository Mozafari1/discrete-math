def zm_Addion (x, y, m):
    SUM = (x+y)%m
    return SUM 
a = 7
b = 9
m = 11
print("The arbitrary number for m is: ",a+b, "mod", m, end=" = " )
print(zm_Addion(a,b,m))

