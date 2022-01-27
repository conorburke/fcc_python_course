#dictionary: kv paris, unordered, mutable

d = {'name': 'Conor', 'h': 'i', 1: 2}
print(d)
print(d[1])

d2 = dict(name='C', age=32)
print(d2)

del d['h']
print(d)
d.pop(1)
print(d)
# remove last inserted item
d.popitem()
print(d)

d = {'name': 'Conor', 'h': 'i', 1: 2}
if 'name' in d:
    print('yes')
try:
    print(d['namee'])

except:
    print('error')

#iteration
for key in d:
    print(key)
for k, v in d.items():
    print(k, v)

#shallow
dc = d
dc2 = d.copy()
dc2['new'] = 'chaos'
print(dc2)
print(d)
print(dc)

d4 = {'x': 2, 'h': 5}
d.update(d4)
print(d)

# keys must me immutable types
dt = {(1,2,3): 4 }
print(dt)