s=input("Enter floats in the following format: 32.45,65.7,12.0,23.0 ")
s=s+","
sum=0.0
extract = ""
for digit in s :
    if digit == ",":
        sum=sum+float(extract)
        extract=""
    else:
        extract = extract + digit
print(sum)