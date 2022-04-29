

def stableMarriage():
    l = []
    l2 = []#[1,4,1,1] -> [1,4,2,1] -> [1,4,2,3]
    counter = 0

    for i in men.values():#get men's list
        l.append(i)

    for j in range(len(l)): # extract men's first prefer
        l2.append(l[j][0])

    ifSame = False
    

    for k in range(len(l2)):

        times = l2.count(l2[k])

        if times != 1 and ifSame == True:
            
            position = -1
            same = l2[k]
            mansort = []#[0,2,3]
            womenPrefer = []#[2,4,3]
            
            for k in range(times):# add value to mansort
                position = l2.index(same, position+1 ,len(l2))
                mansort.append(position)
            
            for rawRank in mansort: #get womanprefer
                womenPrefer.append(women[str(same)].index(rawRank+1)+1)
                
            
            finalChoiseRank = min(womenPrefer)
            finalChoise = women[str(same)][finalChoiseRank-1]

            mansort.remove(finalChoise-1) #[2,3]
            counter += 1
            for m in mansort:
                l2.insert(m,men[str(m+1)][counter])
                l2.pop(m+1)

        if times != 1 and ifSame == False: # trigger
            ifSame = True
            
            
        
    print("The following is a stable marriage solution for this input:\n")
    for i in range(len(l2)):
        print("Man "+ str(i+1)+" and Woman " + str(l2[i]))
        print()
    

# men = {"1":[1,3,2,4],"2":[4,1,3,2],"3":[1,2,3,4],"4":[1,4,3,2]}
# women = {"1":[2,1,4,3],"2":[3,1,2,4],"3":[4,1,3,2],"4":[1,2,3,4]}
men = {"1":[4,1,2,3],"2":[2,3,1,4],"3":[2,4,3,1],"4":[3,1,2,4]}
women = {"1":[4,1,3,2],"2":[1,3,2,4],"3":[1,2,3,4],"4":[4,1,3,2]}

stableMarriage()