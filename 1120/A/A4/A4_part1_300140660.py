# a)
def largest_34(a):
    '''list -> num
        return sum of 3rd and 4th largest num in a list
        big o is (n) '''
    sort_a = sorted(a)
    length = len(sort_a)
    new_list = []
    for i in range (0,length):
        if(i == (length-1)):
            new_list.append(sort_a[i])
        elif (sort_a[i] == sort_a[i+1]):
            pass
        else:
            new_list.append(sort_a[i])
    length2 = len(new_list)
    an = 0
    an = new_list[length2 - 3] + new_list[length2 -4]
    return an

# a = [1000,1,100,2,99,200,100]
# print(largest_34(a))

# b)
def largest_3rd(a):
    '''compute the len(a)//3 largest elements in a 
        big o is (n*log(n))'''
    sort_a = sorted(a)
    length = len(sort_a)
    new_list = []
    for i in range (0,length):
        if(i == (length-1)):
            new_list.append(sort_a[i])
        elif (sort_a[i] == sort_a[i+1]):
            pass
        else:
            new_list.append(sort_a[i])
    length2 = len(new_list)
    an = 0

    third = len(a)//3
    # print(third)
    # print(new_list)
    for i in range(0,third):
        an = an + new_list[length2-1-i]

    return an
# a = [1000,1,100,2,99,200,100]
# a2 = [1000,1,100,2,99,200,100,300,400]

# print(largest_3rd(a))
# print(largest_3rd(a2))

# c)
def third_at_least(a):
    '''list -> num/none
        return a value in a appear at least len(a)//3 + 1 times
        big O is (n)'''
    enough = len(a)//3 + 1
    count = 0
    sort_a = sorted(a)
    length = len(sort_a)
    for i in range (0,length):
        if(i == (length-1)):
            if (count >= enough):
                return sort_a[i]
        elif (sort_a[i] == sort_a[i+1]):
            count = count + 1
        else:
            if (count >= enough):
                return sort_a[i]
    return None

# b = [5,5,5,5,5,5,5,5]
# a = [1000,1,100,2,99,200,100]

# print(third_at_least(a))
# print(third_at_least(b))

# d)
def sum_tri(a,x):
    '''list+num -> bool
        return true if three num is list add together == x
        big o is n**3'''
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            for k in range(j,len(a)):
                if(a[i] + a[j] + a[k] == x):
                    return True
                else:
                    pass
    return False
# c = [1,5,8,2,6,55,90]
# print(sum_tri(c,103))
# print(sum_tri(c,999))



