import functools

def template_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return
    return wrapper


def mydecorator(func):
    # preserves name of wrapped function
    @functools.wraps(func)
    def wrapper():
        return 1 + func()
    return wrapper
    
# same as dosomething = mydecorator(dosomething)    
@mydecorator
def dosomething():
    return 1

# without functools.wrap(func), this will be wrapper and not dosomething
print(dosomething.__name__)
print(dosomething())


def decwithargs(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return wrapper

@decwithargs
def multiply(x, k=2):
    return x * k

print(multiply(5))
print(multiply(5, 3))


# decorators with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = ''
            for _ in range(num_times):
                result += func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
            

# greet = repeat(3)(greet)
# same as above assignment
@repeat(num_times=3)
def greet(name):
    return f'hello {name}'


print(greet('Conor'))

# can add multiple decorators. will be executed in order


# class decorators
# use if you need to keep track of some state

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    # need this specific call
    def __call__(self, *args, **kwargs):
        print('hi there')
        self.num_calls += 1
        print(f'this is executed {self.num_calls}')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()
# cc()

@CountCalls
def say_hello():
    print('hello')

say_hello()
say_hello()







    


