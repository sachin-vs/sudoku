def check_square(num_list,i,j):
    square_list=[]
    
    for z in range(0,len(grid),2):
        for m in range(0,len(grid[z]),2):
            sub_square=[]
            sub_square.append(grid[z][m])
            sub_square.append(grid[z][m+1])
            sub_square.append(grid[z+1][m])
            sub_square.append(grid[z+1][m+1])
            square_list.append(sub_square)

    if i<=1 and j<=1:
        for num in square_list[0]:
            num_list.append(num)
    elif i <=1 and j>1:
        for num in square_list[1]:
            num_list.append(num)
    elif i>1 and j<=1:
        for num in square_list[2]:
            num_list.append(num)
    else:
        for num in square_list[3]:
            num_list.append(num)
    return set(num_list)
def check_rows(num_list,i,j):
    for z in range(0,len(grid[i])):
        num_list.append(grid[i][z])
    return check_square(num_list,i,j)
def check_columns(i,j,grid):
    num_list=[]
    for k in range(0,len(grid)):
        num_list.append(grid[k][j])
    return check_rows(num_list,i,j)


import numpy as np
grid=np.array([[2,0,0,1],[0,0,3,0],[0,0,0,0],[3,0,0,0]])
print('Input Sudoku')
print(grid)
num={0,1,2,3,4}
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] ==0:
            new= check_columns(i,j,grid)
            li=list(num-new)

            grid[i][j]=li[0]
print('Output Sudoku')
print(grid)