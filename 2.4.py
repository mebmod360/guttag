# Pg. 24
# Finger exercise: Write a program that asks the user to input 10 integers, and then
# prints the largest odd number that was entered. If no odd number was entered, it
# should print a message to that effect.

x=float('-inf') #dummy variable whoch starts with lowest possible value

for i in range(10):
    y=int(input("Enter an integer "))
    if y%2==1 and y>x: #checks if the entered value is odd and greater than the dummy variable
        x=y
print("The largest odd integer is", x) if x != float('-inf') else print("There are no odd integers")
