# Chapter 4: Lists - Character Picture Grid
# Author: Paul Jr Fernandez
# Changelog:
# 18 Jan 2018 v1.0: Initial release
#

# Function to interchange rows and columns
def gridTranspose(mirrorGrid):
    maxLength = 0 # Store length of inner list with the most items
    noOfLists = len(mirrorGrid) # No of inner lists present in grid AKA length of grid

    for i in range(noOfLists): # Find inner list with the most items
        if maxLength < len(mirrorGrid[i]):
            maxLength = len(mirrorGrid[i])

    for i in range(maxLength): # Transpose Grid
        for j in range(noOfLists):
            print(mirrorGrid[j][i], end=' ')
        print()
        

# Main
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
gridTranspose(grid)
