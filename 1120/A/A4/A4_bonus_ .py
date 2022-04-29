# 1)
def matrixMinMax(input):
    '''matrix -> tuple has two num
        get the max num and min num in a 2d matrix.
        assume the martix is not empty'''

    length = len(input)
    new_big =[]
    new_small =[]
    # print("len",length)
    for i in range (0,length):
        # print(i)
        big = max(input[i])
        small = min(input[i])

        new_big.append(big)
        new_small.append(small)
    an =[]
    an.append(max(new_big))
    an.append(min(new_big))

    return an

# AAA = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrixMinMax(AAA))
# BBB = [[1,2,-3],[4,5,65],[7,8,9]]
# print(matrixMinMax(BBB))

# 2)
'''grid + num + num + num -> bool
    a game of suduko, return True if good, False otherwise'''
def verifValid(grid,row,col,num):
    if(grid[row][col] != 0):
        print("Not Empty")
        return False
    elif(row != 0 and row != 9 and col != 0 and col != 9):
        if(grid[row+1][col] != num and grid[row-1][col] != num and grid[row][col+1] != num and grid[row][col-1] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 0 and col == 0):
        if(grid[0][1] != num and grid[1][0] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 9 and col == 0):
        if(grid[9][1] != num and grid[8][0] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 0 and col == 9):
        if(grid[1][9] != num and grid[0][8] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 9 and col == 9):
        if(grid[9][8] != num and grid[8][9] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 0):
        if(grid[row+1][col] != num and grid[row][col+1] != num and grid[row][col-1] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(row == 9):
        if(grid[row-1][col] != num and grid[row][col+1] != num and grid[row][col-1] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(col ==0):
        if(grid[row+1][col] != num and grid[row-1][col] != num and grid[row][col+1] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    elif(col == 9):
        if(grid[row+1][col] != num and grid[row-1][col] != num and grid[row][col-1] != num):
            grid[row][col] = num
            return True
        else:
            print("same number on other line")
            return False
    else:
        print("something is wrong")
        return False

# grid = [[5,3,8,6,9,10,4,7],
#         [7,4,6,0,3,2,8,1,9],
#         [1,9,2,0,8,4,3,5,6],
#         [8,7,1,2,6,3,4,9,5],
#         [3,2,9,4,5,7,1,6,8],
#         [4,6,5,9,1,8,7,2,3],
#         [0,0,4,3,7,9,5,8,2],
#         [9,8,3,1,0,5,6,7,4],
#         [2,5,0,8,4,6,9,3,1]]