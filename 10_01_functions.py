def fun():
    print("Func")


def summa(a, b):
    return a + b


# Fibonacci number
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


# Factorial
def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


fun()
print(summa(2, 3))
print(fibb(10))
print(factorial(10))
