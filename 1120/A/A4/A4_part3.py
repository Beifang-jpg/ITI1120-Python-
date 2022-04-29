
# 3)
def overlap(set1, list1):
    '''set+list -> set
        return a set contains same element in inputset and input list'''
    re_set = {0}
    len_set1 = len(set1)
    len_list1 = len(list1)

    for i in range(0,len_set1):
        num = set1.pop()
        for j in range(0,len_list1):
            if (num == list1[j]):
                re_set.add(num)
            else:
                pass
    re_set.pop()
    if(len(re_set == 0)):
        return 
    else:

        return re_set

# test

# set1 = {1,2,3,4,5}
# list1 = [9,8,7,6,5,4,12,13]
AAA = overlap(set(), [0, 19, 2, 4, 5, 9, 10, 11] )
print(AAA)
# print(overlap(set1, list1))


def reverse(input):
    '''map -> map
        give a map's reverse and combain same string and location together'''
    an = {}
    for k, v in input.items():
        an[v] = an.get(v, []) + [k]

    return an

# test

# map = {42:"mar",81:"sue",17:"edd",31:"daev",3:"mar",19:"sue"}
# print(reverse(map))


def digit_sum(input):
    '''num -> num
        calculate a numbers every digit add together equals what'''
    str_input = str(input)
    length = len(str_input)
    sum = 0

    for i in range(0,length):
        sum = sum + int(str_input[i])

    return sum

def digit_root(input):
    '''num -> num
        calculate a numbers every digit add together until digit is one'''
    re = digit_sum(input)

    while(re > 10):
        re = digit_root(re)    
      
    return re


# test
# print(digit_root(158))
# print(digit_root(1969))

