# QUESTION 1

def element_uniqueness(L):
     '''(list)->bool
     Returns True if all the elements in the list are distinct,
     in other words, if there is no element in the list that appears more than once.
     Precondition: L is not empty

     >>> element_uniqueness([2, 2,2, 2, 8])
     False
     >>> element_uniqueness([1,-20,-1])
     True
     >>> element_uniqueness([3,2,4,0,3])
     False
     >>> element_uniqueness([10])
     True
     >>> element_uniqueness([10,10])
     False
     >>> element_uniqueness([10,-1])
     True
     '''

     for i in range(0,len(L)-1):
          for j in range(i+1,len(L)):
               if(L[i] == L[j]):
                    # print(i,"and",j)
                    return False
               else:
                    pass
     return True

# print(element_uniqueness([10,-1]))
# print(element_uniqueness([3,2,4,0,3]))
# print(element_uniqueness([1,-20,-1]))
# print(element_uniqueness([10,10]))



# QUESTION 2

def one_unique_at_least(L):
     '''(list)->bool
     Returns True if there exist at least one element in L that is unique,
     in other words, that appears exactlly once in the list
     Precondition: L is not empty
     >>> one_unique_at_least([2,2,2,2,8])
     True
     >>> one_unique_at_least([2,1,2])
     True
     >>> one_unique_at_least([1,-20,-1])
     True
     >>> one_unique_at_least([3,2,2,3,3])
     False
     >>> one_unique_at_least([10])
     True
     >>> one_unique_at_least([10,10])
     False
     >>> one_unique_at_least([10,-1])
     True
     '''
     new = sorted(L)

     lengh = len(new)

     if(new[0] != new[1]):
          return True
     elif(new[lengh -1] != new[lengh -2]):
          return True

     for i in range(1,len(new)-2):
          if (new[i] != new[i+1] and new[i] != new[i-1]):
               return True
          else:
               pass
     return False

# print(one_unique_at_least([2,2,2,2,8]))   
# print(one_unique_at_least([3,2,2,3,3]))
# print(one_unique_at_least([1,-20,-1]))
          
          

# QUESTION 3
     
def all_unique(L):
     ''' (list,int)->list
     Return a list of elements of L that appear exactlly once in L. 
     Precondition: L is not empty
    
     >>> all_unique([2, 2,2, 2, 8])
     [8]
     >>> all_unique([1,-20,-1])
     [-20,-1,,1]
     >>> all_unique([3,2,2,3,3])
     []
     >>> all_unique([10])
     [10]
     >>> all_unique([10,10])
     []
     >>> all_unique([10,-1])
     [-1,10]
     '''
     new = sorted(L)
     AAA =[]

     lengh = len(new)

     if(new[0] != new[1]):
          AAA.append(new[0])

     if(new[lengh -1] != new[lengh -2]):
          AAA.append(new[lengh -1])

     if(lengh == 3 and len(AAA)==2):
          AAA.append(new[1])

          
     for i in range(1,len(new)-2):
          if(new[i] != new[i+1] and new[i] != new[i-1]):
               AAA.append(new[i])

          else:
               pass
     return AAA
# print(all_unique([3,2,2,3,3]))
# print(all_unique([10,-1]))
# print(all_unique([2, 2,2, 2, 8]))
# print(all_unique([1,-20,-1]))
# print(all_unique([1,-80,-1]))

# QUESTION 1 again

def element_uniqueness_v2(L):
     # make now a 2nd solution to element_uniqueness
     # by making a call to all_unique
     new = all_unique(L)
     # print(len(new))
     if(len(new) == len(L)):
          return True
     else:
          return False
# print(element_uniqueness_v2([2,2,2,2,8]))   
# print(element_uniqueness_v2([3,2,2,3,3]))
# print(element_uniqueness_v2([1,-20,-1]))
 

# QUESTION 2 again

def one_unique_at_least_v2(L):
     # make now a 2nd solution to one_unique_at_least_v2
     # by making a call to all_unique
     new = all_unique(L)

     if(len(new) > 0):
          return True
     else:
          return False
# print(one_unique_at_least_v2([2,2,2,2,8]))   
# print(one_unique_at_least_v2([3,2,2,3,3]))
# print(one_unique_at_least_v2([1,-20,-1]))
# QUESTION 4

def count_unique(L):
     '''(list,int)->int
     Return the number of unique elements of L,
     i.e. the number of elements that appear exactlly once in L
     Precondition: L is not empty
    
     >>> count_unique([2, 2,2, 2, 8])
     1
     >>> count_unique([1,-20,-1])
     3
     >>> count_unique([3,2,2,3,3])
     0
     >>> count_unique([10])
     1
     >>> count_unique([10,10])
     0
     >>> count_unique([10,-1])
     2
     '''
     new = all_unique(L)
     an = len(new)
     return an
# print(count_unique([10,-1]))

# QUESTION 5                               

def duplicates(L):
     ''' (list)->int
     Returns True if the given list L has duplicates, in other,
     if it has at least one element that appears two or more times.
     Precondition: L is not empty

     >>> duplicates([2, 2,2, 2, 8])
     True
     >>> duplicates([1,-20,-1])
     False
     >>> duplicates([3,2,2,3,3])
     True
     >>> duplicates([10])
     False
     >>> duplicates([10,10])
     True
     >>> duplicates([10,-1])
     False
     '''
     new = all_unique(L)
     # print(len(new))
     if(len(new) != len(L)):
          return True
     else:
          return False

# QUESTION 6

def majority(L):
     '''(list)->
     An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
     This function returns the majority element of L if such an element exsits, otherwise it returns None
     >>> majority([2,1,2])
     2
     >>> majority([10,5,1,5,5])
     5
     >>> majority([5,5,1,1])
     
     >>> majority([3])
     3
     >>> majority([8,8,2,8])
     8
     '''
     more = 1
     max = 0
     num = 999
     new = sorted(L)
     for i in range (0,len(new)):

          if (i == len(new)-1):
               print("more",more)
               if(max < more):

                    max = more
                    num = new[i]
                    more = 1
          else:
               if(new[i] == new[i+1]):
                    more = more+1
               else:
                    if(max < more):

                         max = more
                         num = new[i]

                         more = 1

     # print(max)
     if(max > (len(new)//2)):
          return num
     else:
          return
print(majority([8,8,2,8]))
print(majority([10,5,1,5,5]))
 
