# ex1
def m(i):
     '''int->number'''
     if i == 1:
          return 1/3
     else:
          return m(i-1)+i * 1/(2*i+1)

# print(m(1))
# print(m(2))
# print(m(5))

# ex2
def count_digits(n):
    """int -> int"""
    s = str(n)
    an = len(s)

    return an
# print(count_digits(5))
# print(count_digits(55))
# print(count_digits(555))

# ex3
def is_palindrome(input):
    '''string->boolean'''
    l = len(input)
    if (l) < 2:
        return True
    l2 = int(l/2)
    for i in range(0,l2):
        if input[i].lower() != input[2*i-1].lower():
            return False
    return True


# print(is_palindrome("anna"))
# print(is_palindrome("anAAAna"))
# print(is_palindrome("alkgniolasgnliasdgnlsdng"))

# ex4
def is_palindrome_v2(input):
    """string -> bool"""
    l = len(input)
    if (l <= 2):
        return True
    
    if not input[0].isalpha():
        return is_palindrome_v2(input[1:])
    if not input[-1].isalpha():
        return is_palindrome_v2(input[:-1])
    if input[0].casefold() != input[-1].casefold():
        return False
    
    return is_palindrome_v2(input[1:-1])

# print(is_palindrome_v2("A man, a plan, a canal -- Panama!"))

# ex5

def gcd(a,b):
    """int, int -> int """
    if b == 0:
        return a
    return gcd(b, a % b)

# print(gcd(36,20))