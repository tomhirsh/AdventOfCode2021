from utils import read_data_file
from collections import Counter
from copy import deepcopy

lines = read_data_file(14, False)
template = lines[0].strip()

# part 1 - brute force
d_instructions = {}
for line in lines[2:]:
    instruction = line.strip().split(' -> ')
    d_instructions[instruction[0]] = instruction[1]

num_steps = 10

for step in range(num_steps):
    new_template = ''
    for s1, s2 in zip(template[:-1], template[1:]):
        new_template += s1 + d_instructions[s1+s2]
    
    template = new_template + template[-1]
    # print(f'{step}: {template}')

counter = Counter(template)
max_val = max(Counter(template).values())
min_val = min(Counter(template).values())
print(max_val-min_val)


# part 2 - use conditions of couples
num_steps = 40
d_instructions = {}
template = lines[0].strip()

for line in lines[2:]:
    instruction = line.strip().split(' -> ')
    d_instructions[instruction[0]] = [instruction[0][0]+instruction[1], instruction[1]+instruction[0][1], 0]

org_d_instructions = deepcopy(d_instructions)

for s1, s2 in zip(template[:-1], template[1:]):
    d_instructions[s1+s2][-1] += 1

for step in range(num_steps):
    new_d_instructions = deepcopy(org_d_instructions)
    for couple1, couple2, times in d_instructions.values():
        new_d_instructions[couple1][-1] += times
        new_d_instructions[couple2][-1] += times
    d_instructions = deepcopy(new_d_instructions)

sums = {}
for key in d_instructions:
    val = d_instructions[key][-1]
    if key[0] in sums:
        sums[key[0]] += val
    else:
        sums[key[0]] = val
    if key[1] in sums:
        sums[key[1]] += val
    else:
        sums[key[1]] = val

sums[template[0]] += 1
sums[template[-1]] += 1

max_val = max([value/2 for value in sums.values()])
min_val = min([value/2 for value in sums.values()])
print(int(max_val-min_val))
