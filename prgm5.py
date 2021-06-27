def perfect(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i==0:
            sum+=i+n/i
        i+=1

    if sum == n and n!=1:
        return True
    else:
        return False

n=int(input("enter a no."))
a=2
while n>0:
    if perfect(a):
        print(a,end=" ")
        n-=1
    a+=1
