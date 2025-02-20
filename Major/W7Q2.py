def factorial(num):
    fact = 1
    if num == 0:
        return fact
    elif num > 0:
        for i in range(1, num + 1):
            fact *= i
        return fact
    else:
        return "Only positive integers are allowed"
print(factorial(10))