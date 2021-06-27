string=input("enter a string: ")
s=""
a=len(string)
for i in range(0,a):
    if string[i]>="A" and string[i]<="Z":
        s=s+string[i].lower()
    elif string[i]>="a" and string[i]<="z":
        s=s+string[i].upper()
    else:
        s=s+string[i]

print(s)