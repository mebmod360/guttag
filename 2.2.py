# Pg. 18.
# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

# the problem talks about numbers not integers
x=float(input("Enter 1st number "))
y=float(input("Enter 2nd number "))
z=float(input("Enter 3rd number "))

# only odd numbers (which must be integers) are retained all else has -infinity
x= x if x%2==1 else float('-inf')
y= y if y%2==1 else float('-inf')
z= z if z%2==1 else float('-inf')

if x==float('-inf') and y==float('-inf') and z==float('-inf'):
    print("There are no odd number")
else:
    print("The largest odd number is", int(max(x, y, z)))
