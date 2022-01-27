import sys

def mygen():
    yield 1
    yield 2
    yield 3

g = mygen()
print(g)

# for i in g:
#     print(i)

# v1 = next(g)
# print(v1)
# v2 = next(g)
# print(v2)

# can use with anything that takes iterable
print(sum(g))

def countdown(start):
    print('starting')
    while start > 0:
        yield start
        start -= 1

cd = countdown(4)
v = next(cd)
print(v)
v = next(cd)
print(v)
v = next(cd)
print(v)
v = next(cd)
print(v)


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

l = firstn(10000)
print(sys.getsizeof(l))
print(sum(l))

# save lots of memory
def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(g))
g = firstn_gen(10000)
print(sum(g))

def fibonacci(limit):
    first = 0
    second = 1
    while first <= limit:
        yield first
        first, second = second, first + second

fib = fibonacci(30)
for i in fib:
    print(i)

# print(sum(fibonacci(5)))

# shorthand syntax
mygen = (i for i in range(10) if i % 2 == 0)
# for i in mygen:
#     print(i)
print(list(mygen))