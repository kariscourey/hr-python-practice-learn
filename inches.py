# This function converts feet & inches to just inches. Here are three examples:

# feet & inches	inches
# 1, 4	16
# 3, 3	39
# 4, 5	53
# There are 12 inches in a foot.


def feet_to_inches(feet, inches):
    return feet * 12 + inches


print(feet_to_inches(1,4))
