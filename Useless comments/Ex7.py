def find_largest_number(numbers):
    # set the largest number to be the first one in the list
    largest_number = numbers[0]
    # iterate through each number in the list
    for number in numbers:
        # check if the current number is larger than the largest number found so far
        if number > largest_number:
            # if it is, set it as the new largest number
            largest_number = number
    # return the largest number found
    return largest_number
