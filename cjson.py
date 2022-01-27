import json

with open('jdata.json') as data:

    jd = json.load(data)
    print(jd['friends'])

print(jd)

s = json.dumps(jd)
print(s)

with open('new_file.json', 'w') as file:
    # file.write(s)
    json.dump(jd, file, indent=4)


class Foo(object):
    def __init__(self):
        self.x = 1
        self.y = 2

foo = Foo()
# s = json.dumps(foo) # raises TypeError with "is not JSON serializable"

s = json.dumps(foo.__dict__) # s set to: {"x":1, "y":2}
print(s)
s2 = json.dumps(vars(foo))
print(s2)

# can create custom json formatting function, where you'd return a dictionary with the keys you want
# then call json.dumps(object, default=method you defined)
# or create a class that extends JSONEncoder, and call json.dums(object, cls=class you made)
# class must have a def default(self, o) method that returns a dict

# look up video again for how to decode