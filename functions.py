# no caps or dashes - underscores & all lower case

def hello_world():
    print("Hello world!")

hello_world()

def sum(num1, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return    # will return none if any of the variables passed in are not ints & will skip the following line of code
    return num1 + num2

total = sum(2, 3)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    # kwargs = key word arguments
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave", last="Gray")
