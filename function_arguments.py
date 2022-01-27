# arguments vs parameters
# positional arguments must be before keyword arguments

def foo(a, b, *args, **kwargs):
    for a in args:
        print(a)
    
    for k,v in kwargs.items():
        print(k, v)


foo(1, 2, 7, 8, 9, thing1='a', thing2='b')

# a signature like these requires c and d to be keyword arguments
# def foo2(a, b, *, c, d)
def foo3(*, c, d):
    pass

foo3(c=2, d=3)


def arrintake(a, b, c):
    pass

arrintake(*[1,2,3])

def dictintake(a, b):
    pass

dictintake(**{'a': 1, 'b': 2})