# Write a function that given a list of lists, return the list with the fewest integers.

# Sample inputs/outputs

# numbers	output
# []	None
# [[1, 2, 3], [1]]	[1]
# [[1, 2, 3], [3, 2], [1, 2, 11, 200]]	[3, 2]

def sum_all(*numbers):
    return sum(numbers)


print(sum_all(2,3,4,5))
print(sum_all(9))
print(sum_all(0))
