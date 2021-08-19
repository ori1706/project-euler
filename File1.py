import math

def question1(n):
    sum = 0
    for i in range(n):
        #print(i if i % 3 == 0 or i % 5 == 0 else 0)
        sum += i if i % 3 == 0 or i % 5 == 0 else 0

    return sum

def question2(max):
    sum = 0
    first = 1
    last = 2
    curr = first + last
    
    while (curr < max):                
        sum += curr if curr % 2 == 0 else 0
        first = last
        last = curr
        curr = first + last
    
    return sum + 2

def isPrime(n):
    if (n == 2 or n == 3):
        return True

    for i in range(3, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def divOfPrime(n):
    for i in range(int(math.sqrt(n)), 2, -1):
        if (n % i == 0 and isPrime(i)):
            return i


print(divOfPrime(600851475143))