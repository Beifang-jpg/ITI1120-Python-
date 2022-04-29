# ex 1 is_eligible
def ageEnough(age):
    if(age >= 18):
        return True
    else:
        return False
def canada(where):
    if(where == "Canadian" or where == "Canada" or where == "canadian" or where == "canada"):
        return True
    else:
        return False
def crime(c):
    if(c == "NO" or c == "no"):
        return False
    else:
        return True
def is_eligible(age, citizenship, prison):
    if (ageEnough(age) == True and canada(citizenship) == True and crime(prison) == False):
        return True
    else:
        return False
name =input("What is your name? ")
age = int(input("How old are you? "))
citizen = input("What is your citizenship? ")
prison = input("Are you live in prison convicted for a criminal offence? ")

if(is_eligible(age, citizen , prison) == True):
    print(name, ", you are eligible to vote")
else:
    print(name, ", you are not eligible to vote")



# ex 2 rstvwxyz
def mess(input):
    for i in input:
        if(i == "r" or i =="s" or i =="t" or i =="v" or i =="w" or i =="x" or i =="y" or i =="z"):
            input = input.replace(i,i.upper())
        elif(i == " "):
            input = input.replace(i,"-")
    return input
# Testing
# print(mess('Random access memory  '))
# print(mess('central processing unit.'))

# ex 3 in other file

# ex 4

def printOne(integer , character):
    s = character
    if (integer < 0):
        print("Can't be negative.")
        return
    else:
        for i in range (0,integer):
            print (s)
            s = s +character


def pirmaid(integer , character):
    s = character
    e = " "
    level = 1
    mid = 1
    if (integer < 0):
        print("Can't be negative or one level")
        return
    else:
        for i in range (0,integer):
            eachOne = e*(integer - level) + s*(mid) + e*(integer - level)
            print (eachOne)
            level = level+1
            mid = mid+2


number = int(input("Please input a positive integer: "))
character = input("Please input a character: ")
printOne(number,character)


number2 = int(input("Please input a positive integer: "))
character2 = input("Please input a character: ")
pirmaid(number2,character2)

# ex5
def divisors(num):
    if (num < 0):
        print("Can't be negative.")
        return
    else:
        for i in range(1,num+1):
            if ((num % i)== 0):
                print(i)

num = int(input("please input a positive int: "))
divisors (num)

def prime(num):

    if (num < 0):
        print("Can't be negative.")
        return
    elif(num == 1):
        print("Two is the smallest prime number, should bigger than two.")
    else:
        for i in range(2,num):
            if ((num % i)== 0):
                print("It is not prime")
                return False
        print(num + " is prime")
        return True
        
num = int(input("please input a positive int: "))
prime (num)

def prime_bouns(num):
    if (num < 0):
        print("Can't be negative.")
        return
    elif(num == 1):
        print("Two is the smallest prime number, should bigger than two.")
    else:
        for i in range (2,num):
            prime = True
            for j in range(2,i):
                if ((i % j) == 0):
                    prime = False
                    break
            if(prime == True):
                print(i)
            

num = int(input("please input a positive int: "))
prime_bouns (num)