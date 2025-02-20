def isArmstrong(num):
    temp = num
    temp1 = num
    count = 0
    sum = 0

    # Count number of digits
    while temp > 0:
        temp = temp // 10
        count += 1

    while temp1 > 0:
        digit = temp1 % 10
        sum += digit ** count
        temp1 = temp1 // 10

    if sum == num:
        return True
    else:
        return False

print(isArmstrong(153)) 
print(isArmstrong(999))


        

