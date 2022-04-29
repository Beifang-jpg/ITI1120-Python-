# exercises 1
def repeater(s1,s2,n):
    count = 0
    AAA = s1 + s2
    AAA = AAA*n
    underscore = "_"
    BBB = underscore + AAA + underscore

    return BBB


# check 
# print (repeater("AA", "ss", 7))

# exercises 2
def roots(a,b,c):
    # assume a is not 0
    R1 = (-b + (b*b - (4*a*c))**0.5)/(2*a)
    R2 = (-b - (b**2 - (4*a*c))**0.5)/(2*a)
        
    print ("The ...with a = " + str(a) + " b = " +str(b) +" c = "+ str(c))
    print ("has root: " + str(R1) + " and " + str(R2))

# check
# roots(1,2,1)

def real_roots(a,b,c):
    d = b*b - (4*a*c)
    return (d >=0)
# check
# print (real_roots(1,2,1))
# print (real_roots(1,1,1))   

def reverse(x):
    # assume x is two digit positive integer
    AAA = x//10
    BBB = x%10

    CCC = BBB*10 + AAA

    return CCC

# check
print (reverse(27))
print (reverse(19))