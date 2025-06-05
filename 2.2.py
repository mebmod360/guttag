# Pg. 18.
# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

a=int(input("Enter 1st integer "))
b=int(input("Enter 2nd integer "))
c=int(input("Enter 3rd integer "))
print("You entered", a, b, c)   

a=float('-inf') if a%2==0 else a
b=float('-inf') if b%2==0 else b
c=float('-inf') if c%2==0 else c

if a==float('-inf') and b==float('-inf') and c==float('-inf'):
    print("There are no odd integers")
else:
    print("The largest odd integer is", max(a, b, c))
