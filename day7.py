import numpy as np
import os
from scipy.optimize import minimize

def fun(x, crabs_x_poses):
    return np.linalg.norm(crabs_x_poses - x, 1)

def fun2(x, crabs_x_poses):
    total = 0
    xs = np.ones_like(crabs_x_poses) * x
    lower_upper = np.sort(np.vstack([crabs_x_poses, xs]), axis=0)
    for crab in lower_upper.T:
        total += np.abs((crab[1] - crab[0]+1) * (crab[1]-crab[0]) / 2) # sum of sequence
    return total

with open(os.path.join('inputs', 'day7.in'), 'r') as f:
    crabs_horizontal = [int(x) for x in f.readline().strip().split(',')]

crabs_horizontal = np.array(crabs_horizontal)

# part 1 - using scipy minimize
x0 = 0
res = minimize(fun, x0, crabs_horizontal)
print(res)

# part 2 - iterating for minimization
x0 = 0
res = np.inf
for i in range(100000):
    cur_res = fun2(x0, crabs_horizontal)
    if cur_res < res:
        x0 += 1
        res = cur_res
    else:
        break
print(int(res))
