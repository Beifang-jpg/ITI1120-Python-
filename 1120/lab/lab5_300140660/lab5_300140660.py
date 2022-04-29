# Ex1
t=[5, 1, -2, 10, 13, 8]
def ah(l,x,y):
    good = []
    count = 0
    l = len(t)

    for i in range (0,l):
        if (t[i] >= x and t[i] <= y):
            good.append(t[i])
            count = count + 1
        else:
            pass
    
    num = str(len(good))
    m = str(min(good))

    print("(" + num + ", " + m + ")")

# test
# ah(t,2,11)

# Ex2
def is_perfect(input):
    adding = 0

    for i in range(1,input):
        if((input % i) == 0):
            adding = adding + i
        else:
            pass
    
    if(adding == input):
        return True
    else:
        return False
# test
# print(is_perfect(6))
# print(is_perfect(28))

def print_less_than_10000():
    for i in range(1,10001):
        if (is_perfect(i)):
            print (i)
        else:
            pass
# test
# print_less_than_10000()

def print_less_than_35_000_000():
    for i in range(0,35000001):
        if (is_perfect(i)):
            print (i)
        else:
            pass

# test
# print_less_than_35_000_000()

# Ex3a
def arithmetic(input):
    dis = 0
    dis = input[1] - input[0]
    a = False
    l = len(input)

    for i in range(0,(l-1)):
        check = input[i+1] - input[i]
        if(dis != check):
            return a
        else:
            pass
    a = True
    return a
# Test
# print(arithmetic( [-5, -1, 3, 7, 11] ))
# print(arithmetic([0, -1, 3, 7, 11]))
# a = [5, 10, 15, 24, 29]
# print(arithmetic(a))
# print(arithmetic(a[:3]))
# print(arithmetic([1,2,3,5]))

# Ex3b
def is_sorted(input):
    a = False
    l = len(input)

    for i in range(0,(l-1)):
        check = (input[i+1] >= input[i])
        if(check == False):
            return a
        else:
            pass
    a = True
    return a
# test

print(is_sorted([1, 1, 1, 7, 7]))
print(is_sorted([-10, -1, 3, 7, 100]))
print(is_sorted([0, 3, 1, 7, 11]))
a = [5, -10, 15, 24, 29]
print(is_sorted(a))
print(is_sorted(a[1:4]))
