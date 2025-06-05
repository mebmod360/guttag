string1=input("Enter string 1 ")
string2=input("Enter string 2 ")
print(isIn(string1,string2))


def isIn (a,b):
    if a in b or b in a:
        return True
    else: 
        return False
    

