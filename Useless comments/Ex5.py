def calculate_average(nums):
    # define variable to hold the sum
    total = 0
    # iterate over the list of numbers
    for num in nums:
        # add each number to the total
        total += num
    # calculate the average and return it
    average = total / len(nums)
    return average
