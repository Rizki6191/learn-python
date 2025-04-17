sum=0
average=0

number=int(input("Enter total number of element:"))
for i in range(1,number+1):
    value=float(input("Enter number %d:"%i))
    sum+=value

average=sum/number
print("Sum =",sum)
print("Average =",average)
