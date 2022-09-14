command = "Hello, World!"

match command:
    case "Hello, World!":  # only does equality
        print("Hello to you, too!")
    case "Goodbye, World!":
        print("See you later")
    case _:  # means other, best practice
        print("no match found")


lst = [2,2,3,4]

match lst:
    case [1,*rest]:
        print("This list starts with a 1")
    case [2,*rest]:
        print("This list starts with a 2")
    case [3 | 4, *rest]:
        print("This list starts with a 3 or 4")
    case other:
        print("no match found")
