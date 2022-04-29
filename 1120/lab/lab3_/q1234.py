# Q1
def pay(hourly_wage , number_of_hours):
    if(number_of_hours > 40 and number_of_hours <= 60 and hourly_wage >0):
        s = 40*hourly_wage + (number_of_hours - 40)*hourly_wage*1.5
        return s
    elif(number_of_hours > 60 and hourly_wage >0):
        s = 40*hourly_wage + (20)*hourly_wage*1.5 + (number_of_hours - 60)*hourly_wage*2
        return s 
    elif(number_of_hours>0 and number_of_hours <= 40 and hourly_wage >0):
        s = number_of_hours * hourly_wage
        return s
    else:
        s = "None in range"
        return s
# test
# print(pay(10,35))
# print(pay(10,45))
# print(pay(10,60))
# print(pay(10,61))

# Q2
def rps(P1 , P2):
    if (P1 != "R" and P1 != "P" and P1 !="S" and P2 != "R" and P2 != "P" and P2 !="S"):
        s = "input is wrong"
        return s
    if (P1 == P2):
        return 0

    elif(P1 == "R" and P2 == "S"):
        return -1
    elif(P1 == "S" and P2 == "P"):
        return -1
    elif(P1 == "P" and P2 == "R"):
        return -1

    elif(P2 == "R" and P1 == "S"):
        return 1
    elif(P2 == "S" and P1 == "P"):
        return 1
    elif(P2 == "P" and P1 == "R"):
        return 1
# test
# print(rps('R', 'P'))
# print(rps('R', 'S'))
# print(rps('S', 'S'))

# Q3a
def is_divisible(n,m):
    n = int(n)
    m = int(m)
    if (n % m ==0):
        return True
    else :
        return False

AAA = input("Enter 1st integer: ")
BBB = input("Enter 1st integer: ")

if (is_divisible(AAA,BBB) == True):
    print(AAA + " is divisble by " + BBB)
else:
    print(AAA + " is not divisble by " + BBB)

# Q3b
def  is_divisible23n8(AAA):
    if((is_divisible(AAA,2) == True or is_divisible(AAA,3)) == True and is_divisible(AAA,8) == False):
        return True
    else: 
        return False

AAA = input("Enter an integer: ")
if(is_divisible23n8(AAA) == True):
    print(AAA + " is divisible by 2 or 3 but not 8")
else:
    print("It is not true that "+ AAA + " is divisible by 2 or 3 but not 8")
