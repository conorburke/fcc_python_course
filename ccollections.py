# collections: counter, namedtuple, ordereddict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = 'aaaabbbbccc'

# create a dict with counts as values for unique keys
c = Counter(a)
print(c)
# list of tuples with most common
print(c.most_common(2)[0][0])
print(list(c.elements()))

Point = namedtuple('Point', 'x, y')
pt = Point(2,3)
print(type(pt))

# since 3.7, dicts are ordered but older versions use OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)

# defaultdict has default value if key not set
dd = defaultdict(int)
dd['a']
dd['b']
print(dd['c'])

# deque
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.appendleft(4)
dq.popleft()
print(dq)