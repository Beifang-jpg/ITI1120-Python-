# task 1
s1 = 'good'
s2 = 'bad'
s3 = 'silly'

# a
def checkll(s):
    ll = "ll"
    if (s.find(ll) != -1):
        return True
    else:
        return False
# Testing
# print(checkll(s1))
# print(checkll(s3))

# b
def checkEmpty(s):
    check = " "
    if (s.find(check) != -1):
        return True
    else:
        return False

# Testing
# print(checkEmpty(s1))

# c
print(s1 + s2 + s3)

# d
big = s1 + s2 + s3
checkEmpty(big)

# e
print(s3 * 10)

# f
big = s1 + s2 + s3
num = len(big)
print(num)

# task 2
aha = "abcdefgh"

# a
print(aha[0:4])

# b
print(aha[3:6])

# c
print(aha[-1])

# d
print(aha[5:7])

# e
print(aha[3:-1])

# f
print(aha[5:8])

# g
print(aha[0]+aha[3]+aha[6])

# h
print(aha[1]+aha[4])

# task 3

# a=
s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...'''
print(s)
# a
newS = s.replace('.', ' ')
newS = newS.replace(',', ' ')
newS = newS.replace(';', ' ')
newS = newS.replace('\n', ' ')
print(newS)
# b
# there is nothing leading and trailing blank

# c
newS = newS.lower()

print(newS)

# d
print(newS.count('it was'))

# f
newS = newS.replace('was', 'is')

print(newS)