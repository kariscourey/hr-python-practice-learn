# Implement the function sum_all() which returns the sum of all of its arguments.

# Sample inputs/outputs

# numbers	output
# (none)	0
# 9	9
# 2, 3, 4, 5	14

def find_shortest(lists):
    # if lists:
    #     return min(lists, key=len)


    if len(lists) == 0:
        return None

    shortest = lists[0]
    # can't initialize with empty list

    # for lst in lists:
    for lst in lists[1:]:  # this makes a copy of the list, if no [1:], wouldn't make a copy; however, not copying things in the list, only copying the list pointer
        if len(lst) < len(shortest):
            shortest = lst

    return shortest


lists = [[1, 2, 3], [3, 2], [1, 2, 11, 200]]
nope = []

print(find_shortest(lists))
print(find_shortest(nope))
