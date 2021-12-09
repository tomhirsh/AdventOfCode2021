import numpy as np
from numpy.core.defchararray import multiply
from utils import read_data_file

lines = read_data_file(9)
heightmap = np.array([[int(x) for x in line.strip()] for line in lines])

low_points = []
low_points_poses = []
for i in range(heightmap.shape[0]):
    for j in range(heightmap.shape[1]):
        if (((i>0 and heightmap[i,j] < heightmap[i-1,j]) or i==0) and
            ((j>0 and heightmap[i,j] < heightmap[i,j-1]) or j==0) and
            ((i<heightmap.shape[0]-1 and heightmap[i,j] < heightmap[i+1,j]) or i== heightmap.shape[0]-1) and
            ((j<heightmap.shape[1]-1 and heightmap[i,j] < heightmap[i,j+1]) or j==heightmap.shape[1]-1)):
            low_points.append(heightmap[i,j])
            low_points_poses.append((i,j))

print(sum(low_points)+len(low_points))

def tuple_add(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1])

def compute_valid_dirs(point, prev_point):
    valid_dirs = []
    if point == (0,0):
        valid_dirs = [(1,0), (0,1)]
    elif point == (heightmap.shape[0]-1, heightmap.shape[1]-1):
        valid_dirs = [(-1,0), (0,-1)]
    elif point[0] == 0 and point[1] == heightmap.shape[1]-1:
        valid_dirs = [(1,0), (0,-1)]
    elif point[0] == heightmap.shape[0]-1 and point[1] == 0:
        valid_dirs = [(-1,0), (0,1)]
    elif point[0] == 0:
        valid_dirs = [(1,0), (0,1), (0,-1)]
    elif point[1] == 0:
        valid_dirs = [(-1,0), (1,0), (0,1)]
    elif point[0] == heightmap.shape[0]-1:
        valid_dirs = [(-1,0), (0,1), (0,-1)]
    elif point[1] == heightmap.shape[1]-1:
        valid_dirs = [(-1,0), (1,0), (0,-1)]
    else:
        valid_dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    prev_dir = (prev_point[0]-point[0], prev_point[1]-point[1])
    if prev_dir in valid_dirs:
        valid_dirs.remove(prev_dir)
    
    return valid_dirs

def backtracking_basins(point, prev_point):
    if heightmap[point] == 9:
        return 0
    
    heightmap[point] = 9

    valid_dirs = compute_valid_dirs(point, prev_point)
    if len(valid_dirs) == 0:
        return 1
    
    return 1 + sum([backtracking_basins(tuple_add(point , dir), point) for dir in valid_dirs])


basins_sizes = []
for low_point_pos in low_points_poses:
    heightmap_copy = heightmap.copy()
    basin_size = backtracking_basins(low_point_pos, (np.inf, np.inf))
    heightmap = heightmap_copy
    basins_sizes.append(basin_size)

sizes_large = sorted(basins_sizes)[-3:]
large_basins = np.prod(sizes_large)
print(large_basins)
