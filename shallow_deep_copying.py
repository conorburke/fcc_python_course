from copy import copy, deepcopy


org = 5
# variable with same reference. but immutable, so changs won't reflect
cpy = org

cpy += 1
print(org)
print(cpy)

oa = [1, 2, 3]
ca = oa

ca[1] = 9
print(oa)

# shallow copy: one level deep, only references of nested child objects
# depe copy: full independent copy

# shallow

o = [1, 2, 3]
c = copy(o)
# same things
# c = list(o)
# c = o.copy()
o[0] = 99
print(o)
print(c)

# original will be affected when shallwo copy
o = [[1,2,3], [4,5,6]]
sc = copy(o)
sc[0][1] = -10
print(sc)
print(o)

# original will NOT be affected when shallwo copy
o = [[1,2,3], [4,5,6]]
sc = deepcopy(o)
sc[0][1] = -10
print(sc)
print(o)