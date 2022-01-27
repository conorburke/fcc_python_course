# strings: ordered, immutable, text representation

# can use single or double quotes

from xml.etree.ElementTree import tostring


s = '''\
hello \
world\
'''
print(s)


s = 'my strings'
print(s.split())
print(s.split())
print(' '.join(s.split()))
print(','.join([str(x) for x in [1,2,3]]))
print(type(''.join([str(x) for x in [1,2,3]])))
print(s)
for i in s:
    print(ord(i))
    print(chr(ord(i)))

print(s.find('i'))
print(s.count('s'))
print(s.replace('my', 'mi'))

# string format
i = 10
s = 'the num is %f' % i
print(s)
print("the number is {}".format(i))
print(f'the n is {i}')