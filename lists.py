# ordered, mutable, allows duplicates

my_list = ['banana', 'cherry', 'apple']

print(my_list)

my_list_2 = list()
print(my_list_2)

my_list_3 = [5, True, 'apple', 'apple']
print(my_list_3)

item = my_list_3[-1]
assert item == 'apple'

for i, e in enumerate(my_list_3):
    print(i, e)

if 'banana' in my_list_3:
    print('yes')
else:
    print('no')

print('banana' in my_list_3)

print(len(my_list_3))
my_list_3.append('lemon')
my_list_3.insert(1, 'blueberry')
print(my_list_3)
first = my_list_3.pop()
print(first)
print(my_list_3)
my_list_3.remove('apple')
print(my_list_3)
my_list_3.clear()
print(my_list_3)
my_list_3 = [5, True, 'apple', 'apple']
my_list_3.reverse()
print(my_list_3)
my_list.sort()
print(my_list)
# sort() does in place
# sorted(list) does not do it in place
my_list = ['banana', 'cherry', 'apple']
sortlist = sorted(my_list)
print(sortlist)
print(my_list)



l = [0] * 5
print(l)
l2 = [1,2,3]
l3 = l + l2
print(l3)

l = [1,2,3,4,5,6,7]
a = l[2:6]
print(a)
b = l[2:6:2]
print(b)
l.reverse()
print(l)
print(l[::-1])

# points to same
list_org = [1,2,3,4,5]
list_copy = list_org

# new copy
list_copy2 = list_org.copy()
list_copy3 = list(list_org)
list_copy4 = list_org[:]



## list comprehension
a = [1,2,3,4,5,6]
sqr = [i * i for i in a]
print(sqr)