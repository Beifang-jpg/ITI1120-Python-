# Q1

def skate(ice , aveTemp):
    if(ice >=30 and aveTemp <= -10):
        return True
    else:
        return False
# test
# print(skate(30, -10))
# print(skate(25.4, -15))
# print(skate(33, -15))
# print(skate(33, -5))

# Q2
def alphaNote(input):
    letterMark = " "
    if(input>=90):
        letterMark = "A+"
    elif(input>=85):
        letterMark = "A"
    elif(input>=80):
        letterMark = "A-"
    elif(input>=75):
        letterMark = "B+"
    elif(input>=70):
        letterMark = "B"
    elif(input>=65):
        letterMark = "C+"
    elif(input>=60):
        letterMark = "C"
    elif(input>=55):
        letterMark = "D+"
    elif(input>=50):
        letterMark = "D"
    elif(input>=40):
        letterMark = "E"
    elif(input>=0):
        letterMark = "F"
    return letterMark
# test
# print(alphaNote(100))
# print(alphaNote(89))
# print(alphaNote(56))
# print(alphaNote(30))

# Q3
def alphaNoteVerif():
    nextStep = False
    while(nextStep == False):
        grade = float(input("Please input the final mark (from 0 to 100): "))
        if(grade <= 100 and grade >=0):
            nextStep = True
        else:
            pass
    if(grade >= 50):
        re = "Passed"
    else:
        re = "Failed"
    letter = alphaNote(grade)
    print(letter)
    print(re)

# test
# alphaNoteVerif()

# Q4
def loops(input):
    oneToN = ""
    nToOne = ""
    for i in range(1,input+1,2):
        i = str(i)
        oneToN = oneToN + i + " "
    for i in range(input,0,-2):
        i = str(i)
        nToOne = nToOne + i + " "

    print(oneToN)
    print(nToOne)

# test
# loops(10)
# loops(13)

# Q5

def tester():
    # none -> none
    password = str(input("Enter your password: "))
    test_password(password)

def test_password(password):
    # str -> none
    # @,-, #, $, or % &
    length = len(password)
    hasLower = False
    hasUpper = False
    hasSpecial = False
    hasNum = False
    if(length < 8 or length >16):
        print("Try again, your password does not meet all requirements")
        return
    else:
        for i in password:
            if(i.islower()):
                hasLower = True
                # print("low")
            elif(i.isupper()):
                hasUpper = True
                # print("up")
            elif(i.isnumeric()):
                hasNum = True
                # print("num")
            elif(i == "&" or i == "@" or i == "-" or i == "#" or i == "$" or i == "%"):
                hasSpecial = True
                # print("spe")
        if (hasLower == True and hasUpper == True and hasSpecial == True and hasNum == True):
            print("Great, your password meets all requirements")
        else:
            print("Try again, your password does not meet all requirements")
            print(hasLower)
            print(hasUpper)
            print(hasNum)
            print(hasSpecial)

# test
# tester()
