print(2 * 3)
print(2 ** 3)
zeros = [0, 1] * 5
print(zeros)
s = "ab" * 10
print (s)

def foo(a, *args, **kwargs):
    print(a)
    for a in args:
        print(a)
    for k,v in kwargs.items():
        print(k, v)

foo(1, 2, 3, 4, {'a': 1, 'b': 2})


# a signature like these requires c and d to be keyword arguments
# def foo2(a, b, *, c, d)
def foo3(*, c, d):
    pass

foo3(c=2, d=3)

def arrintake(a, b, c):
    print(a, b, c)

arrintake(*[1,2,3])

def dictintake(a, b, c=3):
    print(a, b, c)

dictintake(**{'a': 1, 'b': 2, 'c': 4})



numbers = [1, 2, 3, 4]
*beg, last = numbers
print(beg)
print(last)

tup = (1, 2, 3)
l = [4, 5, 6]
s = {7, 8, 9}

new_list = [*tup, *l, *s]
print(new_list)

d = {'a': 1, 'b': 2}
d2 = {'c': 3}

new_dict = {**d, **d2}
print(new_dict)

keys = {*d, *d2}
print(keys)