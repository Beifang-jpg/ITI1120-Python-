# Q1

from xml.etree.ElementTree import tostring


def travelTime(distance , speed):
    # number -> number
    # Assume two variable are real numbers.
    timeInHour = distance / speed

    timeInMin = timeInHour * 60

    return timeInMin


# Q2
def finalMark(a,b,c,d,e):
    # number,number,number,number,number -> number
    # Assume five input are bwteen 0-100
    W1 = a* 0.10
    W2 = b* 0.24
    W3 = c* 0.08
    W4 = d* 0.23
    W5 = e* 0.35
    f = W1 + W2 + W3 + W4 + W5

    return f

# Q3
def bibformat(a,b,c,d,e):
    # string,string,string,string,number -> string
    # Assume five input are strings
    f = "'" + a + "(" + str(e) +"). " + b + ". " + c + ": " + d + "'"

    return f

# check
# print (bibformat("Antonnie", "le pe" , "Parise", "Jese", "1943"))

# Q4
def bibformatPrint():
    # none -> none
    Author =  input("Enter the name of the author: ")
    title = input("Enter the titel of the book: ")
    city = input("In what city the headquarters of the publisher? ")
    publisher = input("Enter the name of the publisher: ")
    year = input("What year was the book published? ")
    f = bibformat(Author,title,city,publisher,year)
    print(f)


# check
# bibformatPrint()

# Q5
def in_out(x,y,c):
    # number,number,number -> none
    # Assume c is >=0
    point1 = input("Please enter the x for query point: ")
    point2 = input("Please enter the y for query point: ")
    point1 = float(point1)
    point2 = float(point2)

    if (point1 >= x and point1 <= (x+c)):
        if (point2 >= y and point2 <= (y+c)):
            print("True")
            # return True
        else:
            print("False")
            # return False
    else:
        print("Flase")
        # return False

# Q6 part1
def cad_cashier(price,payment):
    # number,number -> none
    # Asssume price and payment are both positive real number
    # Also they are both two digits
    if (payment < price):
        print("The money you give is not enough. ")
    else:
        change = payment - price
        change = round(change,2)
        # print(change)

        fiveCents = round((change*100) / (0.05*100))
        # print(fiveCents)
        # The way python store number make me to do this
        real_change = round(fiveCents * 0.05,2)
        print (real_change)
# check
# cad_cashier(10.58,11)
# cad_cashier(10.58,15)
# cad_cashier(10.55,15)
# cad_cashier(10.50,15)
# cad_cashier(10.52,15)
# cad_cashier(98.87,100)

# Q6 part2
def min_CAD_coins(price,payment):
    # number,number -> number,number,number,number,number
    # Asssume price and payment are both positive real number
    # Also they are both two digits
    if (payment < price):
        print("The money you give is not enough. ")
    else:
        change = payment - price
        change = round(change,2)
        # print(change)

        fiveCents = round((change*100) / (0.05*100))
        # The way python store number make me to do this
        tonnies = fiveCents // 40
        tonnies = int(tonnies)
        fiveCents = fiveCents % 40

        lonnies = fiveCents // 20
        lonnies = int(lonnies)
        fiveCents = fiveCents % 20

        quarters = fiveCents // 5
        quarters = int(quarters)
        fiveCents = fiveCents % 5

        dimes = fiveCents // 2
        dimes = int(dimes)
        fiveCents = fiveCents % 2

        nickels = fiveCents
        nickels = int(nickels)

        # print(tonnies, lonnies , quarters , dimes, nickels)
        return(tonnies, lonnies , quarters , dimes, nickels)

# check
# min_CAD_coins(10.58,11)
# min_CAD_coins(10.58,15)
# min_CAD_coins(10.52,15)

