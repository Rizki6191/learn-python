import math
a = int(input("Enter frist side: "))
b = int(input("Enter seconnd side: "))
c = int(input("Enter third side: "))

if(((a+b)>c) and ((b+c)>a) and ((c+a)>b)):
    if ((a==b) and (a==c)):
        print("Equilateral Triangle")
    elif((a==b) or (b==c) or (a==c)):
        print("Isoscales Triangle")
    else:
        print("Scalence Triangle")
else:
    print("Triangle is not possible")

s = (a+b+c)/2.0
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle:",area,"sq.unit")
