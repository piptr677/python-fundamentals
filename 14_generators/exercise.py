# fill in this function
def fib():
    x, y = 1, 1
    while True:
        yield y
        x, y = y, x + y

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break