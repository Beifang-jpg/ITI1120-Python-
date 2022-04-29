l =[]
l2 = []
check = None
sameChoise = 0
men = []
women = []

def getMenList():
    
    if len(l) == 0:
        for i in men.values():#get men's list
            l.append(i)

        for j in range(len(l)): # extract men's first prefer
            l2.append(l[j][0])

def checkDuplicate():
    
    global check,sameChoise
    
    l3 = list(set(l2))

    if len(l2) > len(l3):
        check = True
        for x in l2:
            if l2.count(x) > 1:
                sameChoise = x
    else:
        check = False

def stableMarriage():

    getMenList()
    checkDuplicate()
    
    if check == True:
        times = l2.count(sameChoise)
        position = -1
        menList = []
        womenPrefer = []
            
        for k in range(times):
            position = l2.index(sameChoise, position+1 ,len(l2))
            menList.append(position)
            
        for rawRank in menList: 
            womenPrefer.append(women['Woman '+str(sameChoise)].index(rawRank+1)+1)
        
        finalChoiseRank = min(womenPrefer)
        finalChoise = women['Woman '+str(sameChoise)][finalChoiseRank-1]
        menList.remove(finalChoise-1) 

        for m in menList:
            for n in range(len(womenPrefer)):
                l2.insert(m,men['Man '+str(m+1)][n])
                l2.pop(m+1)

        checkDuplicate()
        if check == False:
            output()
        else:
            stableMarriage()

def output():

    print("The following is a stable marriage solution for this input:")
    print()
    for i in range(len(l2)):
        print("Man "+ str(i+1)+" and Woman " + str(l2[i]))
        print()

def getDict(filename):

    lines = open(filename,'r', encoding='utf-16').read().splitlines()
    people = []
    value = []
    key = []
    key2 = []
    key3 = []
    global men
    global women

    for line in lines:
        people.append(line.split(': '))

    for va in range(len(people)):
        value.append(people[va][0])
        if len(people[va][0]) == 0:
            value.remove('')
            break
        else:
            key.append(people[va][1])

    #print(key)

    for x in key:
        x = list(x)
        for y in x:
            if y == ' ':
                x.remove(' ')
        key2.append(x)

    #print(key2)

    for d in key2:
        key3.append(list(map(int,d)))
    
    #print(key3)

    men = dict(zip(value,key3))

    print(men)


    value = []
    key = []
    key2 = []
    key3 = []

    for va in range(va+1,len(people)):
        value.append(people[va][0])
        if len(people[va][0]) == 0:
            value.remove('')
            break
        else:
            key.append(people[va][1])    
    

    for x in key:
        x = list(x)
        for y in x:
            if y == ' ':
                x.remove(' ')
        key2.append(x)

    #print(key2)

    for d in key2:
        key3.append(list(map(int,d)))
    
    print(key3)

    women = dict(zip(value,key3))  

    print(women)  

getDict('part1_input.txt')
#men = {"1":[4,1,2,3],"2":[2,3,1,4],"3":[2,4,3,1],"4":[3,1,4,2]}
#women = {"1":[4,1,3,2],"2":[1,3,2,4],"3":[1,2,3,4],"4":[4,1,3,2]}
#men = {"1":[1,3,2,4],"2":[4,1,3,2],"3":[1,2,3,4],"4":[1,4,3,2]}
#women = {"1":[2,1,4,3],"2":[3,1,2,4],"3":[4,1,3,2],"4":[1,2,3,4]}
stableMarriage()