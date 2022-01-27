from random import randint

try:
    b = '1' + 2
except TypeError as ex:
    print(ex)
# can use else clause if no exceptions caught
# can use finally clause to execute no matter what

# raise an error

x = randint(1, 10)

if x < 5:
    raise ValueError("too small")
if x < 8:
    raise Exception("other ex")

# class MyCustomError(Exception):
    pass