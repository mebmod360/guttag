x = int(input("Enter an integer "))
root, root_check = 1, 1
pwr, pwr_check = 1, 1
while root ** pwr < x:
    while pwr < 6 :
        if root ** pwr == x:
            print("Root is", root, "power is", pwr)
            root_check = root
            pwr_check = pwr
            break
        else:
            pwr += 1
    pwr = 1
    root += 1
if (root_check)**(pwr_check) != x :
    print("No pair of integers exist")