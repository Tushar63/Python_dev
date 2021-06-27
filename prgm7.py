def find3Numbers(A, size, sum):
 
    A=sort_array(A)
 
    for i in range(0, size-2):
        x = i + 1
        y = size-1
        while (x < y):
         
            if( A[i] + A[x] + A[y] == sum):
                print("Triplet is", A[i],', ', A[x], ', ', A[y])
                return True
             
            elif (A[i] + A[x] + A[y] < sum):
                x += 1
            else: 
                y -= 1
 
    print("Such triplet does not exist")
    return False

def sort_array(A):
    l=len(A)
    for i in range(l):
        for j in range(0,l-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    
    return A

n=int(input("Enter the size of the array :"))
B = []
print("Enter the values of the array :")
for i in range(0,n):
    a=int(input())
    B.append(a)
sum = int(input("enter the sum value :"))
size = len(B)

find3Numbers(B, size, sum)