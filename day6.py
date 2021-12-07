import numpy as np
import os

num_days = 256
cycle = 7
len_fishes = cycle + 2
# using a histogram of fishes, for each day count how many fishes alive
fishes_histogram = np.zeros(len_fishes)

with open(os.path.join('inputs','day6.in')) as f:
    for fish in f.readline().strip().split(','):
        fishes_histogram[int(fish)] += 1

for i in range(num_days):
    # create more fishes in the relevant day
    fishes_histogram[(i + cycle) % len_fishes] += fishes_histogram[i % len_fishes]

print(int(fishes_histogram.sum()))


# brute-force
# num_days = 16

# with open(os.path.join('inputs','day6_ex.in')) as f:
#     lanternfish_list = [int(x) for x in f.readline().strip().split(',')]

# for i in range(num_days):
#     for i_list in range(len(lanternfish_list)):
#         if lanternfish_list[i_list] == 0:
#             lanternfish_list[i_list] = 6
#             lanternfish_list += [8]
#         else:
#             lanternfish_list[i_list] -= 1

# print(len(lanternfish_list))