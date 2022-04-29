tower_A = [] 
tower_B = []
tower_C = []
'''Build the three tower we will use later, in the program later. 1 means towerA, 2 means towerB, 3 means towerC.'''

def start_Part3():
    '''get start the whole program'''

    good = False
    while(good == False):
        try:
            num = int(input("Type in the number of disks you want to move: "))

            if (type(num) == int and num > 0):
                good = True
                # stop the loop
                print("We will put", str(num), "disks in the left most tower and begin.")
                print("We will use numbers to represent disks, larger numbner represent larger disks.")
                set_up_beginning(num,tower_A)
                # setup disks
                hanoi(num,1,3)
                # start recursion
            else:
                print("You need to enter a int bigger than 0")

        except:
                print("You need to enter a int bigger than 0")
                continue

    


def hanoi (num,start,end):
    if (num == 1):
        move(start,end)
    else:
        other = 6 - (start + end)
        # since 1 + 2 + 3 = 6, so 6 -(other two) = the number of one left tower
        hanoi(num - 1,start , other)
        move(start,end)
        hanoi(num - 1 , other, end)

def move(start, end):
    '''move a disk from a tower to another tower'''

    print("move the top plate from " ,start ,"to",end)
    disk = 0
    if(start == 1):
        disk = tower_A.pop(0)
    elif(start == 2):
        disk = tower_B.pop(0)
    elif(start == 3):
        disk = tower_C.pop(0)
    else:
        print("Something wrong")
    
    if(end == 1):
        tower_A.insert(0,disk)
    elif(end == 2):
        tower_B.insert(0,disk)
    elif(end == 3):
        tower_C.insert(0,disk)
    else:
        print("Something wrong") 

    show_tower(tower_A)
    show_tower(tower_B)
    show_tower(tower_C)
     




def set_up_beginning(num,tower):
    '''put all disks in to the left most tower'''

    for i in range(1,num+1):
        tower.append(i)
    return

def show_tower(tower):
    '''print the current situation of a tower'''

    num = len(tower)

    if(tower == tower_A):
        print("Tower A(the left one) has", num ,"disks on it and currently look like this")
        if(num == 0):
            print("Currently empty")
            return
        for i in tower:
            print(str(i))
    elif(tower == tower_B):
        print("Tower B(the mid one) has", num ,"disks on it and currently look like this")
        if(num == 0):
            print("Currently empty")
            return
        for i in tower:
            print(str(i))
    elif(tower == tower_C):
        print("Tower C(the right one) has", num ,"disks on it and currently look like this")
        if(num == 0):
            print("Currently empty")
            return
        for i in tower:
            print(str(i))
        

# set_up_beginning(5,tower_A)
# show_tower(tower_A)
start_Part3()


