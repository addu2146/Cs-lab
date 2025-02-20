def isPerfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

num = int(input("Enter a number: "))
if isPerfect(num):
    print("Perfect")
else:
    print("Not perfect")
