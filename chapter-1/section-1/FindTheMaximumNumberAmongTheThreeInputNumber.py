num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

if(num1 >= num2) and (num2 >= num3):
    Max=num1
elif (num2 >= num1) and (num2 >= num3):
    Max=num2
else:
    Max=num3
print("The maximum number is", Max)
