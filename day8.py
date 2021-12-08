from utils import read_data_file
import os
import numpy as np

# part 1
digits_numbers_unique = {2:0, 4:0, 3:0, 7:0}

lines = read_data_file(8, False)
for line in lines:
    line_splitted = line.strip().split('| ')[-1].split(' ')
    for digit_pattern in line_splitted:
        if len(digit_pattern) in digits_numbers_unique.keys():
            digits_numbers_unique[len(digit_pattern)] += 1

sum1 = sum(digits_numbers_unique.values())
print(sum1)


def sort_str(pattern):
    return ''.join(sorted(pattern))

# part 2
digits_numbers_unique = {2:1, 4:4, 3:7, 7:8}
sum_entries = 0
for line in lines:
    encode = {'a':'','b':'', 'c':'', 'd':'','e':'','f':'','g':''}

    digits_numbers = {5:[], 6:[]}
    encode_numbers_unique = {1:'', 4:'', 7:'', 8:''}
    encode_numbers = {0:'', 2:'', 3:'', 5:'', 6:'', 9:''}
    decode_patterns = {}
    

    out_digits = line.strip().split('| ')[-1].split(' ')
    signal_digits = line.strip().split(' |')[0].split(' ')
    # find the unique digit lengths
    for pattern in signal_digits:
        if len(pattern) in digits_numbers_unique.keys():
            encode_numbers_unique[digits_numbers_unique[len(pattern)]] = pattern
            decode_patterns[sort_str(pattern)] = digits_numbers_unique[len(pattern)]
        else:
            digits_numbers[len(pattern)].append(pattern)

    # 7-1 gives us 'a'
    for dig in encode_numbers_unique[7]:
        if dig not in encode_numbers_unique[1]:
            encode['a'] = dig
            break

    # 6 doesn't contain one of 'c', 'f' and is the only one so with 6 digits - this will encode 'c'
    for pattern in digits_numbers[6]:
        if not (encode_numbers_unique[1][0] in pattern and encode_numbers_unique[1][1] in pattern):
            encode_numbers[6] = pattern
            decode_patterns[sort_str(pattern)] = 6
            break

    # find 'c' - in 8 but not in 6
    for p in encode_numbers_unique[8]:
        if p not in encode_numbers[6]:
            encode['c'] = p
            break

    # find 'f' - in one and not 'c'
    for p in encode_numbers_unique[1]:
        if p != encode['c']:
            encode['f'] = p

    # find 5 - the only 5 chars that doesn't contain 'c' and 2 doesn't contain 'f'
    for pattern in digits_numbers[5]:
        if encode['c'] not in pattern:
            encode_numbers[5] = pattern
            decode_patterns[sort_str(pattern)] = 5
        elif encode['f'] not in pattern:
            encode_numbers[2] = pattern
            decode_patterns[sort_str(pattern)] = 2
        else:
            encode_numbers[3] = pattern
            decode_patterns[sort_str(pattern)] = 3

    digits_of_9 = encode_numbers_unique[4] + encode_numbers[3]
    for pattern in digits_numbers[6]:
        if sort_str(pattern) != sort_str(encode_numbers[6]):
            for p in pattern:
                if p not in digits_of_9:
                    encode_numbers[0] = pattern
                    decode_patterns[sort_str(pattern)] = 0
                    break

    for pattern in digits_numbers[6]:
        if sort_str(pattern) != sort_str(encode_numbers[6]) and sort_str(pattern)!= sort_str(encode_numbers[0]):
            encode_numbers[9] = pattern
            decode_patterns[sort_str(pattern)] = 9

    entry = [decode_patterns[sort_str(x)] for x in out_digits]
    val_entry = 0
    for e,i in zip(entry, range(len(entry)-1, -1, -1)):
        val_entry += (10**i) * e
    sum_entries += val_entry

print(sum_entries)

