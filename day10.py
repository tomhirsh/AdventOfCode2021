from utils import read_data_file
import numpy as np

def is_corrupted(line, closers, openers):
    l_openers = []
    for c in line:
        if c in openers:
            l_openers.append(c)
        elif l_openers[-1] != closers[c][0]:
            return c
        elif l_openers[-1] == closers[c][0]:
            l_openers.pop()
        else:
            return 'incomplete'
    return 'incomplete'

def process_incomplete(line, closers, openers_vals):
    l_openers = []
    for c in line:
        if c in openers_vals.keys():
            l_openers.append(c)
        elif l_openers[-1] == closers[c][0]:
            l_openers.pop()
    
    score_line = 0
    for o in reversed(l_openers):
        score_line = 5*score_line + openers_vals[o]
    return score_line

lines = read_data_file(10, False)
openers = '([{<'
closers = {')':['(',3], ']':['[',57], '}':['{',1197], '>':['<',25137] }
openers_vals = {'(':1, '[':2, '{':3, '<':4}
score1 = 0
scores2 = []
for line in lines:
    line_stripped = line.strip()
    c = is_corrupted(line_stripped, closers, openers)
    if c in closers.keys():
        score1 += closers[c][1]
    else:
        score_line = process_incomplete(line_stripped, closers, openers_vals)
        scores2.append(score_line)

print(score1)
print(sorted(scores2)[int(len(scores2)/2)])
