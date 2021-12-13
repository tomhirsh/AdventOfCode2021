from utils import read_data_file
import numpy as np


lines = read_data_file(11, True)
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
grid_size = 10
num_steps = 10000

def add_to_adjacent_poses(grid, poses):
    for i in range(poses[0].shape[0]):
        for direction in directions:
            new_pos = (poses[0][i]+direction[0], poses[1][i]+direction[1])
            if new_pos[0]>=0 and new_pos[0]<grid_size and new_pos[1]>=0 and new_pos[1]<grid_size:
                grid[new_pos] += 1
    return grid

grid = np.array([[int(x) for x in line.strip()] for line in lines])
exploded = 0
for step in range(num_steps):
    grid = grid + 1 # increase all octopuses in 1
    octopuses_poses = np.where(grid == 10)
    while octopuses_poses[0].shape[0] > 0:
        grid[octopuses_poses] = -999
        adjacent_poses = add_to_adjacent_poses(grid, octopuses_poses)
        exploded += octopuses_poses[0].shape[0]

        octopuses_poses = np.where(grid > 9)
    grid[np.where(grid<0)] = 0

    if np.all(grid == np.zeros((grid_size, grid_size))):
            print(f'first simultaneously: {step+1}')
            break
print(grid)
print(exploded)
        
