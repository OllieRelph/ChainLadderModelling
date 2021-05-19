import pandas as pd
import chainladder as cl
import numpy as np
# read in csv with triangle of data, final row has 1 known value
triangle = pd.read_csv('triangle_test.csv')

# convert Nan values to None
triangle = triangle.where(pd.notnull(triangle), None)



# convert to 2D list
triangle_list = triangle.values.tolist()

#  set row limit/height for sum_right and sum_left
limit = 6

def CLM_Calc(x,y,limit):
    sum_right = 0
    sum_left = 0
    for i in range(1,limit+1):
        # sum rows above in current column, and last column, up to limit amount of rows
        sum_right += triangle_list[y-i][x]
        sum_left += triangle_list[y-i][x-1]
        # CLM Calculation
        triangle_list[y][x] = triangle_list[y][x-1] * (sum_right/sum_left)

# go through 2D array left to right, up to down
for y in range(0,len(triangle_list)):
    for x in range(0,len(triangle_list[0])):
        # if value is None
        if triangle_list[y][x] == None :
            # if the value to the left of None is 0 then the new value is 0
            if x!=0 and triangle_list[y][x-1] == 0:
                triangle_list[y][x] = 0
                
            # set dynamic limit if our row doesnt have 'limit' amount of rows above
            elif y < limit:
                CLM_Calc(x, y, y)
            # if we do have 'limit' amount of rows above
            else:
                CLM_Calc(x, y, limit)
                
                
np.savetxt('triangle_test_clm.csv', triangle_list,delimiter = ", ")
                
                                      


