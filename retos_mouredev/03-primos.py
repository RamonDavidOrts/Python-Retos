def isPrime(num):
    if num <= 1: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

for i in range(1, 101):
    if isPrime(i): print(i)
