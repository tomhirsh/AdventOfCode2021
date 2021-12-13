from utils import read_data_file
import numpy as np

lines = read_data_file(13, False)
foldings = [] # a list of tuples (axis, val), where axis:['x','y'] and val is int

num_foldings = -1

max_x, max_y = 0, 0
for i, line in enumerate(lines):
    if line == '\n':
        line_start_folding = i
        break
    coords = line.strip().split(',')
    max_x = max(max_x, int(coords[0]))
    max_y = max(max_y, int(coords[1]))

grid = np.zeros((max_x+1, max_y+1))

for line in lines[:i]:
    coords = line.strip().split(',')
    grid[int(coords[0]), int(coords[1])] = 1


for i in range(line_start_folding+1, len(lines)):
    line_params = lines[i].strip().split(' ')[-1].split('=')
    foldings.append((line_params[0], int(line_params[1])))

print(grid)
print(foldings)
if num_foldings != -1:
    foldings = foldings[:num_foldings]

for fold in foldings:
    if fold[0] == 'y':
        shape_y = max(fold[1], grid.shape[1] - (fold[1]+1))
        new_grid = grid[:,:shape_y]
        new_grid[:, new_grid.shape[1] - (grid.shape[1] - fold[1]-1):] += np.flip(grid[:,fold[1]+1:], 1)
        
    else: # 'x'
        shape_x = max(fold[1],grid.shape[0] - (fold[1]+1))
        new_grid = grid[:shape_x,:]
        new_grid[new_grid.shape[0] - (grid.shape[0] - fold[1]-1):, :] += np.flip(grid[fold[1]+1:,:], 0)

    grid = new_grid

grid[np.where(grid!=0)] = 1
print(np.where(grid!=0)[0].shape[0])

# pretty print
for i in range(grid.shape[1]):
    print(''.join(['|' if x==1 else '.' for x in grid[:,i]]))
