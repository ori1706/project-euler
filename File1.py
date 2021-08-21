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

    for i in range(3, n):
        if (n % i == 0):
            return False
    return True

def question3(n):
    for i in range(int(math.sqrt(n)), 2, -1):
        if (n % i == 0 and isPrime(i)):
            return i

def isPalindrome(n):
    strNum = str(n)    
    length = len(strNum) - 1
    for i in range(length):
        if (strNum[i] != strNum[length - i]):
            return False
    return True

def question4(digits):
    biggest = 0
    for i in range(int(math.pow(10, digits)) - 1, int(math.pow(10, digits - 1)) - 1, -1):
        for j in range(int(math.pow(10, digits)) - 1, int(math.pow(10, digits - 1)) - 1, -1):
            if (isPalindrome(i * j) and i * j > biggest):
                biggest = i * j
                
    return biggest

def isDivisable(n, divBy):
    for i in range(2, divBy + 1):
        if (n % i != 0): 
            return False
    return True

def question5(divBy): #long
    i = 1
    while True:
        if (isDivisable(i, divBy)):
            return i
        i += 1

def question6(length):
    firstSum = 0
    secondSum = 0
    for i in range(1, length + 1):
        firstSum += math.pow(i, 2)
    for i in range(1, length + 1):
        secondSum += i
    secondSum = math.pow(secondSum, 2)
    return secondSum - firstSum

def question7(n):
    primeNums = 1
    i = 4
    while True:
        if (isPrime(i)):
            primeNums += 1
            if (primeNums == n):
                return i
        i += 1
    return 0

def question8(length):
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    res = [int(x) for x in str(num)]
    biggest = 0
    for i in range(len(res) - length):
        prod = 1
        for j in range(length):
            prod *= res[i + j]
        if (prod > biggest):
            biggest = prod

    return biggest

def isPythagorian(a, b, c):
    return (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2))

def question9(n):    
    for a in range(1, n):
        for b in range(a, n - a):
            if (isPythagorian(a, b, n - a - b)):
                return a * b * (n - a - b)

print(question9(1000))