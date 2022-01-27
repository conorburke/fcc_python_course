import random
import secrets
import numpy as np

# sudo random; seem random but are reproducable

# flot 0 to 1
r = random.random()
print(r)

# float to range
r2 = random.uniform(1, 10)
print(r2)

# range inclusive
ri = random.randint(1, 10)
# range exclusive on end
rni = random.randrange(1, 3)
print(rni)

# normal/gause mean of 0, std of 1
rnormal = random.normalvariate(0, 1)
print(rnormal)

l = [5,6,7]
# pick a random value from list
rl = random.choice(l)
# pick sample without replacement
rs = random.sample(l, 2)
print(rl)
print(rs)
# pick sample with replacement
rk = random.choices(l, k=2)
print(rk)
random.shuffle(l)
print(l)

# make results reproduceable
random.seed(1)
print(random.random())


# secrets module is actually random not pseudo
s = secrets.randbits(32)
print(s)
s = secrets.randbelow(100)
print(s)
s = secrets.token_bytes(32)
print(s)
s = secrets.token_hex(32)
print(s)
s = secrets.choice(l)
print(s)

# numpy
n = np.random.rand(3)
print(n)
n = np.random.rand()
print(n)
n = np.random.rand(3, 3)
print(n)
n = np.random.randint(5)
print(n)
n = np.random.randint(5, 10, 3)
print(n)
n = np.random.normal(1, 1)
print(n)