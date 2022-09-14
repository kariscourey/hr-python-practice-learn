# This function takes a list of product prices and number of sales of the product. It sums up the total revenue of those sales.

# Here is an example input for the total_revenue function with one product in it.

# products_sold = [
#     {
#         "sales": 10,
#         "price": 6.5,
#     },
# ]
# The total revenue for the example above would be 10 x 6.5 = 65.

# Here's an example with two items:

# products_sold = [
#     { "sales": 11, "price": 9,   },
#     { "sales": 5,  "price": 1.5, },
# ]
# The total revenue for the example above is: (11 x 9) + (5 x 1.5) = 106.5.

# If the list is empty, then the total revenue should be 0.


def total_revenue(product_sales):

    # revenue = 0

    # for i in product_sales:  # .items() returns tuple; .values() returns int
    #     revenue += i.get("sales") * i.get("price")

    #     # print(type(key))
    #     # print(i.get("sales"))
    #     # print(i.get("price"))
    #     # print(type(i))
    #     # print(i)

    # return revenue

    return sum([(i.get("sales") * i.get("price")) for i in product_sales])



products_sold = [
    {
        "sales": 10,
        "price": 6.5,
    },
]

print(total_revenue(products_sold))


products_sold = [
    { "sales": 11, "price": 9,   },
    { "sales": 5,  "price": 1.5, },
]

print(total_revenue(products_sold))
