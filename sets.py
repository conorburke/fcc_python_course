# sets: unordered, mutable, no dups

s = {1, 2, 3, 4, 4, 5}
print(s)
s2 = set([4,4,4,5,6,7,7,8])
print(s2)
# check how many unique characters in word
ss = set('order')
print(ss)

s.add(6)
print(s)
s.discard(3)
print(s)
# returns and removes arbitrary value
a = s.pop()
print(a)
s.clear()
print(s)
s = {1, 2, 3, 4, 4, 5}
print(s)
s2 = set([4,4,4,5,6,7,7,8])

union = s.union(s2)
print(union)

inter = s.intersection(s2)
print(inter)

diff = s.difference(s2)
print(diff)
diff2 = s2.difference(s)
print(diff2)
# same as symmetric difference
print(s.difference(s2).union(s2.difference(s)))
print(s.symmetric_difference(s2))

# use update(), intersection_update(), differene_update(), or symmetric_difference to do inplace update

print(s.issubset(s2))
print(s.isdisjoint(s2))

#copying is same rules as other collection types

# frozen set. is immutable
fs = frozenset([1,2,3,3,4])
print(fs)

