# tuples: ordered, immutable, allows dups
import sys
import timeit

tup = ('name', 31, 'thing')
print(tup)
# parentheses are optional
tup = 1, 2, 3
print(tup)
print(type(tup))

# tuples need a comma or they won't be a tuple if one element
not_tup = ('thing')
print(not_tup)
print(type(not_tup))

yes_tup = 'thing',
print(yes_tup, type(yes_tup))

tup2 = tuple(['obj', 'or'])
print(tup2)

# can't change items in tuple
# tup[2] = 'new'

# can iterate like with lists

tup3 = ('a','p', 'p', 'l', 'e')
print(len(tup3))
print(tup3.count('p'))
print(tup3.index('p'))

l = list(tup3)
print(l)
l.append('s')
print(tuple(l))

#unpacking
tup4 = 'a', 27, 'c', 'd'

first, *middle, last = tup4
print(first, middle, last)

# tuples usually more performant
l = [1,2,3,4,5]
t = 1,2,3,4,5
print(sys.getsizeof(l))
print(sys.getsizeof(t))
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="0,1,2,3,4,5", number=1000000))