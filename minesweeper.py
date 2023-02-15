# Lesson SE-T28
# Task 1


# minesweeper.py--returns the number of adjacent mines of a grid containing
#                   "#" (mines) and "-", where "-" is replaced with the number
#                   of mines adjacent.


# Define a function that receives input from a 2D list and assess the number
#   of mines surrounding the dashes.

def mine_Sweeper(mine_field):

    # Search every element for a "-" in the grid and replace with adj mines count.
   
    print("\n\t\t\t*** Number of adjacent Mines: ***\n")
    
    for row, line in enumerate(mine_field, 0):
        column = 0
        for col in line:
            mines = 0
            if col == "-":
        
                # North position
                if row -1 < 0:
                    if column < 0:
                        mines += 0
                elif mine_field[row -1][column] == "#":
                    mines += 1
        
                # North-west position
                if row -1 < 0 or column -1 < 0:
                    mines += 0
                elif mine_field[row -1][column -1] == "#":
                    mines +=1
        
                # West position
                if column -1 < 0:
                    if row < 0:
                        mines += 0
                elif mine_field[row][column -1] == "#":
                    mines += 1
                    mines += 0
                
                # South-west position
                if row +1 > len(mine_field) -1 or column -1 < 0: 
                    mines += 0
                elif mine_field[row +1][column -1] == "#":
                    mines += 1
        
        
                # South position
                if row +1 > len(mine_field) -1:
                    if column < 0:
                        mines += 0
                elif mine_field[row +1][column] == "#":
                    mines += 1
         
                # South-east position
                if column  +1  > len(line) -1 or row +1 > len(mine_field) -1:
                    mines += 0
                elif mine_field[row +1][column +1] == "#":
                    mines += 1
        
                # East position
                if column +1 > len(line) -1 :
                    if row < 0 :
                        mines += 0
                elif mine_field[row][column +1] == "#":
                    mines += 1
        
                # North-east position
                if column +1 > len(line) -1 or row -1 < 0:
                    mines += 0
                elif mine_field[row -1][column +1] == "#":
                    mines +=1
        
                mine_field[row][column] = str(mines) 
                column += 1
        
            elif col == "#":
                mine_field[row][column] = col 
                column += 1
        
        # Output of the function
        print("                       ", mine_field[row])

print()


# Create 2D list/grid.

mine_field = [ ['#', '-', '#', '-', '#', '#', '-', '-', '#', '-'],
               ['-', '-', '-', '#', '-', '-', '-', '#', '-', '#'],
               ['#', '-', '#', '-', '#', '-', '#', '#', '-', '-'],
               ['-', '#', '-', '-', '#', '-', '#', '-', '#', '-'],
               ['-', '-', '#', '-', '-', '-', '-', '-', '#', '-'],
               ['#', '-', '#', '-', '-', '-', '-', '#', '-', '-'],
               ['-', '-', '-', '#', '-', '-', '-', '#', '-', '#'],
               ['-', '-', '#', '-', '-', '#', '-', '-', '#', '-'],
               ['-', '#', '-', '#', '#', '-', '-', '#', '-', '#'],
               ['#', '-', '-', '#', '-', '-', '-', '#', '-', '#']]


# Call mine_Sweeper function with the list as input.

mine_Sweeper(mine_field)

print()

