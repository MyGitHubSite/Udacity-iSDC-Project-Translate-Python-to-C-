#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
        
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = beliefs

    for i in range(len(beliefs)):     #row
        for j in range(len(beliefs[0])):    #col
            hit = (color == grid[i][j])
            new_beliefs[i][j] = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
                                                          
    return normalize(new_beliefs)

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)   #rows
    width = len(beliefs[0])   #cols
    new_G = [[0.0 for j in range(width)] for i in range(height)]
    
    for i, row in enumerate(beliefs):    #row
        for j, cell in enumerate(row):    #col
            new_i = (i + dx) % height
            new_j = (j + dy) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
            
    return blur(new_G, blurring)