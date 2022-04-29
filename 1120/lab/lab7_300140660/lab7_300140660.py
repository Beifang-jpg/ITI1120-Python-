# 5.16
def indexes(s , c):
    '''str + char -> list'''
    an = []
    l = len(s)

    for i in range (0,l):
        if (s[i] == c):
            an.append(i)
        else:
            pass
    return an

# print(indexes("mississippi", "i"))
# print(indexes("mississippi", "s"))

# 5.17 
def double(input):
    '''list -> none'''
    l = len(input) 
    for i in range(1,l):
        if(input[i] == 2*(input[i-1])):
            print(input[i])
        else:
            pass
    return
# double([3,0,1,2,3,6,2,4,5,6,5])

# 5.18
def four_letter(input):
    '''list -> list'''
    an = []
    for i in range (len(input)):
        if (len(input[i]) == 4):
            an.append(input[i])
        else:
            pass
    return an
# print(four_letter(["AAA" , "AAAA", "BBBB"," dsfsdfds"]))

# 5.19
def inBoth(input_first,input_second):
    for i in range(len(input_first)):
        for j in range(len(input_second)):
            if (input_first[i] == input_second[j]):
                return True
    return False


# 5.20
def intersection(input_first,input_second):
    ''' list + list -> list'''
    an =[]
    for i in range(len(input_first)):
        for j in range(len(input_second)):
            if (input_first[i] == input_second[j]):
                an.append(input_first[i])
            else:
                pass
    return an
# print(intersection([1,2,3,4,5,6],[1,41,71,2,33,5,999,888]))

# 5.21
def pair(input_first,input_second,num):
    ''' list +list+ num -> none'''
    # an =[]
    for i in range(len(input_first)):
        for j in range(len(input_second)):
            if(input_first[i] + input_second[j] == num):
                AAA = [input_first[i],input_second[j]]
                print(AAA[0], " ", AAA[1])

            else:
                pass
    return
# print(pair([2,3,4,],[5,7,9,12],9))

# 5.22
def pairSum(input,num):
    ''' list + num -> none'''
    for i in range(len(input)):
        for j in range(i , len(input)):
            if(input[i] + input[j] == num ):
                print(i, " " , j)
            else:
                pass
    return
# pairSum([7,8,5,3,4,6],11)

# 5.29

def lastfirst(input):
    '''list -> list'''
    first = []
    last = []
    l = len(input)

    for i in range(len(input)):
        
        AAA = input[i].split(', ')
        print(len(AAA))

        last.append(AAA[0])
        first.append(AAA[1])

    return [first, last]


# print(lastfirst(["AAA , BBB","Ajioj, Bjoijo","Ajiodfj, Bkjfo"]))

# 5.31
def subsetSum(input, num):
    '''list + num -> bool'''
    for i in range(len(input)-2):
        for j in range(i+1, len(input)-1):
            for k in range(j+1, len(input)):
                if (input[i] + input[j] + input[k]) == num:
                    return True
    return False

# print(subsetSum([5,4,10,20,15,19],38))
# print(subsetSum([5,4,10,20,15,19],10))

# 5.33
def mystery(input):
    '''int -> int'''
    count = 0
    while (input > 1):
        input = input// 2
        count = count + 1
    return count
# print(mystery(4))
# print(mystery(11))
# print(mystery(25))

# 5.46
def inversions(s):
    '''str -> int'''
    count = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:
                count = count + 1
    return count
# print(inversions("ABCD"))

# 5.48
def sublist(input_first, input_second):
    count = 0
    for i in range(len(input_first)):
        for j in range(len(input_second)):
            if (input_first[i] == input_second[j]):
                count = count + 1
            else:
                pass
    if (count == (len(input_first))):
        return True
    else:
        return False
# print(sublist([15,1,100],[15,1000,555,777,1,233,100]))

# 5.37
def mssl(input):
    '''list -> int'''
    best = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)+1):
            count = 0
            for k in range(i, j):
                count = count + input[k]
            if (count > best):
                best = count
            else:
                pass
    return best
# print(mssl([3,4,5]))