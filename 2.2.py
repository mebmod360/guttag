# Pg. 18.
# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

x=int(input("Enter 1st number "))
y=int(input("Enter 2nd number "))
z=int(input("Enter 3rd number "))
print("You entered", x, y, x)   

x=float('-inf') if x%2==0 else x
y=float('-inf') if y%2==0 else y
z=float('-inf') if z%2==0 else z

if x==float('-inf') and y==float('-inf') and z==float('-inf'):
    print("There are no odd number")
else:
    print("The largest odd number is", max(x, y, z))
