# Implement the function sum_all() which returns the sum of all of its arguments.

# Sample inputs/outputs

# numbers	output
# (none)	0
# 9	9
# 2, 3, 4, 5	14

def find_shortest(lists):
    if lists:
        return min(lists, key=len)

lists = [[1, 2, 3], [3, 2], [1, 2, 11, 200]]
nope = []

print(find_shortest(lists))
print(find_shortest(nope))
