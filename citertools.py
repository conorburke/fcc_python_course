# itertools: product, permuations, combinations, accumulate, groupby, and infinite iterators

from itertools import accumulate, groupby, product, permutations, combinations, count, cycle, repeat
import operator

a = [1,2,3,4]
b = [4,5,6,7]
# cartesian product of lists
prod = product(a,b)
print(list(prod))

perm = permutations(a)
print(list(perm))

comb = combinations(a, 2)
print(list(comb))

accu = accumulate(a, func=operator.mul)
print(list(accu))

gb = groupby(a, key=lambda x: x % 3 == 0)
# print(list(gb))
for k, v in gb:
    print(k)
    print(list(v))

d = [{'name': 'alice', 'age': 25}, {'name': 'bob', 'age': 27},{'name': 'charlie', 'age': 25}]
# groupby required the groupby key to be sorted
d = sorted(d, key=lambda x: x['age'])
gb2 = groupby(d, key=lambda x: x['age'])
for k, v in gb2:
    print(k)
    print(list(v))

# start at a num, keep going indefinitely
# for i in count(10):

# infinitely cycle through a sequence
# for i in cycle([1,2,3])

# infinitely loop over a num:
# for i in repeat(1)
# stop after a certain time
# for i in repeat(100, 5)

