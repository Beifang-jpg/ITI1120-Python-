def stableMarriage():
    l = []
    l2 = []
    
    for i in men.values():#get men's values
        l.append(i)

    for j in range(len(l)): # extract men's first prefer
        l2.append(l[j][0])

    ifSame = False
    counter = 0

    for k in range(len(l2)):
        times = l2.count(l2[k])
        if times != 1 and ifSame == True:
            l2[k] = men[str(k+1)][counter+1]
            counter +=1
            if l2.count(l2[k]) != 1:
                l2[k] = men[str(k+1)][counter+1]
                counter = 0


        if times != 1 and ifSame == False:
            ifSame = True
            
            
        
    print("The following is a stable marriage solution for this input:\n")
    for i in range(len(l2)):
        print("Man "+ str(i+1)+" and Woman " + str(l2[i]))
        print()
    

men = {"1":[4,1,2,3],"2":[2,3,1,4],"3":[2,4,3,1],"4":[3,1,2,4]}
women = {"1":[4,1,3,2],"2":[1,3,2,4],"3":[1,2,3,4],"4":[4,1,3,2]}
stableMarriage()