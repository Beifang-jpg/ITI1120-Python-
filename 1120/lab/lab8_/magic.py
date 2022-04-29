def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''

     # this tests the condition that is implied by the definition
     # i.e. that m has to be a square matrix
     if(not(is_square(m))): # if matrix is not square
          return False      # return False

     # YOUR CODE GOES HERE

     # TEST CONDITION 1
     box = []


     for i in range(0,len(m)):
          for j in range(0,len(m)):
               AAA = m[i][j]
               if AAA not in box:
                    box.append(AAA)
               else:
                    return False
     # test if there is any same number

     # TEST CONDITION 2
     row_one = 0
     col_one = 0
     for i in range(0,len(m)):
          row_one = row_one + m[0][i]
     for i in range(0,len(m)):
          col_one = col_one + m[i][0]
     
     for i in range(1,len(m)):
          total_thisRow = 0
          for j in range(0,len(m[i])):
               total_thisRow = total_thisRow + m[i][j]
          if (total_thisRow != row_one):
               return False
          else:
               pass

     for i in range(0,len(m)):
          total_thisCol = 0
          for j in range(0 ,len(m)):
               total_thisCol = total_thisCol + m[j][i]
          if (total_thisCol != col_one):
               return False
          else:
               pass
     
     return True




# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
