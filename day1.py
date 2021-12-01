from utils import read_data_file
import numpy as np

# read data
lines = read_data_file(1, False)

# first part
prev_depth = int(lines[0][:-1])
counter_increased = 0
for line in lines[1:]:
    cur_depth = int(line[:-1])
    if cur_depth > prev_depth:
        counter_increased += 1
    prev_depth = cur_depth
print(counter_increased)


# second part
three_windows = np.zeros((3,3))
cur_window_idx, cur_sum_depths, counter_increased = 0, 0, 0
prev_sum_depth = np.inf

for idx, line in enumerate(lines):
    cur_depth = int(line[:-1])
    if idx % 3 == cur_window_idx and idx >1:
        cur_sum_depths = three_windows[cur_window_idx].sum()
        if cur_sum_depths > prev_sum_depth:
            counter_increased += 1
        prev_sum_depth = cur_sum_depths
        cur_window_idx = (cur_window_idx + 1) % 3

    three_windows[0, idx % 3] = cur_depth
    three_windows[1, (idx+1) % 3] = cur_depth
    three_windows[2, (idx+2) % 3] = cur_depth

if three_windows[cur_window_idx].sum() > prev_sum_depth:
    counter_increased += 1

print(counter_increased)
