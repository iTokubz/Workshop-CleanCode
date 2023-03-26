def calculate_total(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            if num > 10:
                total += num
            else:
                total += num * 2
        else:
            if num < 0:
                total -= num
            else:
                total += num
    return total
