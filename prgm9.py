def func(A,n):

    while n<x:
        A=sort_array(A)
        if A[n-1]!=A[n-2]:
            s=A[n-1]
            return s
        else:
            n=n+1

    return 0
    
def sort_array(A):
    l=len(A)
    for i in range(l):
        for j in range(0,l-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    
    return A

x=int(input("enter the size of the array: "))
A=[]
print("enter the array elements: ")
for i in range(0,x):
    a=int(input())
    A.append(a)

n=int(input("enter the value of n: "))

if func(A,n)>0:
    print("the ",n,"th smallest no. in the array is :",func(A,n))
else:
    print("No such value exist")