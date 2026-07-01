#! /usr/bin/env python3

# test = "ValueError" # passing a value of wrong type to a function
# test = "IndexError" # index out of range
# test = "TypeError" # performing an action with an unexpected type
# test = "ZeroDivisionError"
# test = "FileNotFoundError" # raised when performing an action with an non-existent file
# test = "KeyError" # occured when trying to access a non-existent key's value
# test = "AttributeError"
    # mis-spelled method names
    # calling a method that is not supported by an object
    # accessing a non-existent class attribute
# test = "default"

match test:
    case "ValueError":
        x = float("hello")
        print(x)
    case "TypeError":
        x = "hello" + 15
    case "ZeroDivisionError":
        1 / 0
    case "FileNotFoundError":
        file = open("test.txt")
    case "KeyError":
        info = {"name": "zehra", "age": 21}
        print(info["job"])
    case "IndexError":
        x = ["apple", "banana", "cherry"]
        print(x[4])
    case "AttributeError":
        # case 1 - uppper() instead of upper()
        # message = "hello world"
        # print(message.uppper())

        # case 2 - append() can be used only with lists
        # text = "zehra"
        # text.append("!")

        # case 3 - trying to reach to an attribute that was never defined in a class
        class Plant:
            def __init__(self, name):
                self.name = name

        p1 = Plant("rose")
        print(p1.age)
    case _:
        print("no match")