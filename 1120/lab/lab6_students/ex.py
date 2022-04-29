# ex2
def exerciseTwo():
    # nothing -> nothing
    out = False
    
    while(out == False ):
        one = input("Enter the first number: ")
        two = input("Enter the second number: ")


        one = int(one)
        two = int(two)

        display = one + two
        print(display)

        AAA = input("Enter yes if you want to do that again: ")
        if (AAA == "yes"):
            out = False
        else:
            out = True

# exerciseTwo()
# ex3
def first_neg(input):
    # list -> number
    i = 0
    r = len(input)
    while(i < r):
        print(i)
        if(input[i] < 0):
            break
        else:
            i = i+1

        
# first_neg([2, 3, -1, 4, -2])
# first_neg([2, 3, 1, 4, 2])
# first_neg([])

# ex4
def sum_5_consecutive_for(input):
    # list -> bool

    l = len(input)

    if(l < 5):
        return False

    for i in range((l)-4):
        if input[i]+input[i+1]+input[i+2]+input[i+3]+input[i+4] == 0 :
            return True

    else:
        return False

def sum_5_consecutive_while(input):
    # list -> bool

    l = len(input)

    if(l < 5):
        return False
    i = 0
    while (i < (l-4)):
        if input[i]+input[i+1]+input[i+2]+input[i+3]+input[i+4] == 0 :
            return True
        i = i+1

    return False  

# print(sum_5_consecutive_for([2, 3, -3, 2, 4,-6]))
# print(sum_5_consecutive_for ([-10, 1, 1, 4, 2, 10, 13]))
# print(sum_5_consecutive_for([2, 1, -3, -3, -3, 2, 7, 4, -6]))
# print(sum_5_consecutive_for ([]))
# print(sum_5_consecutive_for ([1, -1,0]))

# print(sum_5_consecutive_while([2, 3, -3, 2, 4,-6]))
# print(sum_5_consecutive_while ([-10, 1, 1, 4, 2, 10, 13]))
# print(sum_5_consecutive_while([2, 1, -3, -3, -3, 2, 7, 4, -6]))
# print(sum_5_consecutive_while ([]))
# print(sum_5_consecutive_while ([1, -1,0]))



# ex5

# in other file

# ex6
def fib(n):
    a=[1]*n  

    i=2
    while (i<n):
        a[i]=a[i-1]+a[i-2]  
        i=i+1
    print(a)

fib(7)
fib(8)