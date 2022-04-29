# Q1
def triples(input):
    # str -> bool
    l = len(input)

    for i in range(0,(l-2)):
        # print(input[i])
        if(input[i] == input[i+1] == input[i+2]):
            return True
        else:
            pass
    return False

# print(triples("abc"))
# print(triples("abbbcdeeggggg"))
# print(triples("abc2eee"))

# Q2
def momo(input):
    # str -> str
    l = len(input)
    an = ""
    i = 0
    count = 1

    while(i < l):
        if(i == (l-1)):
            an = an + str(input[i]) + str(count)
            i = i + 1           
        elif(input[i] == input[i+1]):
            count = count +1
            i = i + 1
        else:
            an = an + str(input[i]) + str(count)
            i = i + 1
            count = 1


    # print(an)
    return an


# momo("abcccd")
# momo("a")
# momo("aabbbccccx")
# momo("aaa1111")
    
# Q3
def sum_odd_divisors(n):
    # int -> int or none
    an = 0
    if (n == 0):
        return
    else:
        if(n < 0):
            n = n * (-1)

        for i in range(1,(n+1)):
            if(n % i == 0 and i % 2 == 1):
                an = an + i
    # print(an)
    return an

# sum_odd_divisors(-9)
# sum_odd_divisors(1)
# sum_odd_divisors(2)
# sum_odd_divisors(3)
# sum_odd_divisors(7)
# sum_odd_divisors(-2001)