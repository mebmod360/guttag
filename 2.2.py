a=int(input("Enter 1st  number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
print("You entered", a, b, c)   

a=float('-inf') if a%2==0 else a
b=float('-inf') if b%2==0 else b
c=float('-inf') if c%2==0 else c

if a==float('-inf') and b==float('-inf') and c==float('-inf'):
    print("There are no odd numbers")
else:
    print("The largest odd number is", max(a, b, c))
