for num in range(1, 1001):
    order = len(str(num)) 
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num:
        print(num)