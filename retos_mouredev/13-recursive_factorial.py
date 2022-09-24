def factorial(num):
    if num < 0:
        return None
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(-2))
