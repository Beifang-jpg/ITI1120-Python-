from random import random, randrange


n=int(input("Enter a positive even integer for the size of the list?" ))

# 1
a = []
for i in range (0,n):
    a = a +[0]
print(a)

# 2
b = []
for i in range (0,n):
    r = randrange(1,100)
    b = b +[r]

print(b)

# 3
c = b
print(c)

# 4
AAA = len(b)
AAA = AAA/2
AAA = int(AAA)

for i in range(0,AAA):
    c[i] = 0

print(b)
print(c)

# 5
d = []
d = b

# 6
AAA = len(b)
# BBB = AAA/2
# BBB = int(BBB)
e = []
i = 0

while (i < AAA):
    add = b[i]
    e = e + [add]
    i = i +2

print(e)

