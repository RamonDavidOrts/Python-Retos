n0 = 0
n1 = 1

for i in range(1, 51):
    print(n0)
    fib = n0 + n1
    n0 = n1
    n1 = fib
