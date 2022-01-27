# anonymous arguments
from functools import reduce

add10 = lambda x: x + 10

print(add10(99))

mult = lambda x,y: x * y

print(mult(7, 9))

points = [(1,2), (13, 7), (5, 8)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)

m = map(lambda x: x * 2, [1,2,3])
print(m)
print(list(m))

r = reduce(lambda x, y: x + y, [1,2,3], 3)
print(r)