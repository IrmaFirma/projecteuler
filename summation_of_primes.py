
import math

def isPrime(p):
    #revision to exclude unnecesary checking even numbers
    if p == 2:
        return True
    if p % 2==0 and p != 2:
        return False
    
    #int(math.sqrt(p)+1) optimizing
    for j in range(3, int(math.sqrt(p)+1), 2):
        if p % j == 0:
            return False #not prime
        
    return True

sum_num = 0

for i in range(2, 2000001):
    if isPrime(i) == True:
        sum_num += i

print(sum_num)
