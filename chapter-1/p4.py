import cmath

# ax**2 + bx + c = 0
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(s1,s2))
