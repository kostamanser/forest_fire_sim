# Rules:

# Burning Trees:
# If a tree (1) has a burning neighbour (2) (not diagonal neighbours), it catches fire and becomes a burning tree (2) 
#   in the next step.
# Burned Trees:
# A burning tree (2) will turn into an empty cell (0) in the next step (it burns down).
# Tree Growth:
# Empty cells (0) randomly turn into trees (1) with a small 
#   probability at each step, simulating regrowth.

import numpy as np
import matplotlib.pyplot as plt
from random import randint
from matplotlib.colors import ListedColormap

# Adjust size of grid and number of iterations (frames)
rows = 40
columns = 40
frames = 100

# Start grid with random 0s, 1s, 2s
game_grid = np.zeros([rows+2,columns+2])


for x in range(2,rows+1):
    for y in range(2,columns+1):
        # Generate random integer
        chance = randint(0,100)
        # percent chance square is burning state
        if chance<10:
            game_grid[x,y] = 2
        # percent chance square is living tree
        elif chance > 50: 
            game_grid[x,y] = 1
            
# Set up the plot
fig, ax = plt.subplots()
cmap = ListedColormap(['#836b4d', '#7fae8b', '#c76363'])

im = ax.imshow(game_grid, cmap=cmap, interpolation='nearest')

# Small chance of creating new tree at each location
def create_new_trees(grid, x, y):
    chance = randint(0,100)
    if chance<10:
        grid[x,y]= 1
    return grid

# Handle when a tree should sart burning
def burn_trees(grid, x, y):
    if (grid[x+1,y] == 2 or grid[x-1,y] == 2 or grid[x,y+1] == 2 or grid[x,y-1] == 2) and grid[x,y] == 1:
        grid[x,y] = 2
    return grid

# Find trees already burning
def burned_trees(grid):
    burned = np.argwhere(grid ==2.)
    return burned
    
        

# Simulation loop
for frame in range(frames):
    burning = burned_trees(game_grid)
    for x in range(2,rows+1):
        for y in range(2,columns+1):
            game_grid = create_new_trees(game_grid,x,y)
            game_grid = burn_trees(game_grid,x,y)

    game_grid[burning[:, 0], burning[:, 1]] = 0

    # Display simulation
    im.set_data(game_grid)  
    plt.draw()  
    plt.pause(0.2) 

# Keep the plot open after the simulation finishes
plt.show()
