# ex2
def min_or_max_index(lst, b):
    if (b == True):
        return get_min(lst)
    else:
        return get_max(lst)

def get_max(input):
    max = input[0]
    index = 0
    for i in range(len(input)):
        if (input[i] > max):
            max = input[i]
            index = i
    return (max, index)

def get_min(input):
    min = input[0]
    index = 0
    for i in range(len(input)):
        if (input[i] < min):
            min = input[i]
            index = i
    return (min, index)

# ex3
def first_one(input):
    index = len(input) - 1
    mid = index //2
    one = -1

    while(input[mid] != 1 and mid < index):
        if(mid == (index-1)):
            mid = mid+1
        
        rest = index - mid
        mid = mid + (rest // 2)


    
    
    if(input[mid] == 1):
        one = mid
    else:
        one = -1
    return one
# print(first_one( [0,0,0,0,0,0,1,1] ))
# print(first_one( [1,1] ))
# print(first_one( [0,0,0] ))

def last_zero(input):
    '''if zero not exist, it will return -1'''
    one = first_one(input)
    if(one == (-1)):
        zero = 0
    else:
        zero = one-1
    return zero
# print(last_zero( [0,0,0,0,0,0,1,1] ))
# print(last_zero( [1,1] ))
# print(last_zero( [0,0,0] ))
