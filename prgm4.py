def find_gcd(x, y):

    if(x==0):
        return y
     
    return find_gcd(y%x,x)

n =int(input("enter the size of the array : "))       
a=[]
print("enter the array elements:")
for i in range(0,n):
    t=int(input())
    a.append(t)

num1=a[0]
num2=a[1]
gcd=find_gcd(num1,num2)

for i in range(2, n):
    gcd = find_gcd(gcd, a[i])
       
print("Gcd = ",gcd)