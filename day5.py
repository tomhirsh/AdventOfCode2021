import numpy as np
from utils import read_data_file


def create_start_end_points(points):
    points = [points[0].split(','), points[1].split(',')]
    for i, p in enumerate(points):
        points[i] = tuple(int(x) for x in p)
    cur_max_x = max(points[0][0], points[1][0])
    cur_max_y = max(points[0][1], points[1][1])
    return points, cur_max_x, cur_max_y



lines = read_data_file(5, False)
# list of tuples of tuples,
# each tuple is a tuple of start,end points (tuples)
segments_coords = [] 
max_x, max_y = 0, 0
# parse and init coords list
for line in lines:
    points = line.strip().split('->')
    tuple_points, cur_max_x, cur_max_y = create_start_end_points(points)
    segments_coords.append(tuple_points)
    max_x = max(cur_max_x, max_x)
    max_y = max(cur_max_y, max_y)


# part A

board = np.zeros((max_x+1, max_y+1), dtype=int)

for segment_coord in segments_coords:
    if segment_coord[0][0] == segment_coord[1][0]: # same x
        cur_max_y = max(segment_coord[0][1], segment_coord[1][1])
        cur_min_y = min(segment_coord[0][1], segment_coord[1][1])
        board[cur_min_y:cur_max_y+1, segment_coord[0][0]] += 1
    if segment_coord[0][1] == segment_coord[1][1]: # same y
        cur_max_x = max(segment_coord[0][0], segment_coord[1][0])
        cur_min_x = min(segment_coord[0][0], segment_coord[1][0])
        board[segment_coord[0][1], cur_min_x:cur_max_x+1] += 1
    
res = len(np.where(board >= 2)[0])
print(res)
    

# part B

board = np.zeros((max_x+1, max_y+1), dtype=int)

for segment_coord in segments_coords:
    if segment_coord[0][0] == segment_coord[1][0]: # same x
        cur_max_y = max(segment_coord[0][1], segment_coord[1][1])
        cur_min_y = min(segment_coord[0][1], segment_coord[1][1])
        board[cur_min_y:cur_max_y+1, segment_coord[0][0]] += 1
    elif segment_coord[0][1] == segment_coord[1][1]: # same y
        cur_max_x = max(segment_coord[0][0], segment_coord[1][0])
        cur_min_x = min(segment_coord[0][0], segment_coord[1][0])
        board[segment_coord[0][1], cur_min_x:cur_max_x+1] += 1
    else: #diagonal
        delta_x, delta_y = 1, 1
        if segment_coord[0][0] > segment_coord[1][0]:
            delta_x = -1
        if segment_coord[0][1] > segment_coord[1][1]:
            delta_y = -1

        for i in range(abs(segment_coord[0][0]-segment_coord[1][0])+1):
            board[segment_coord[0][1] + i*delta_y, segment_coord[0][0] + i*delta_x] += 1

res = len(np.where(board >= 2)[0])
print(res)