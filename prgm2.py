def findTrailingZeros(n):
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    return count

 
n = int(input("enter a no.: "))
print("Count of trailing 0s in",n,"! is", findTrailingZeros(n))