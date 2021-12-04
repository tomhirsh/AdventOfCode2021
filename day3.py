from utils import read_data_file
import numpy as np


def is_common(is_most_common, lines_arr):
    common_bits = np.zeros(lines_arr.shape[1], dtype=int)
    out = 0
    for i in range(lines_arr.shape[1]):
        bit = 0
        sum_bit_all_lines = lines_arr[:,i].sum()
        if ((is_most_common and sum_bit_all_lines > lines_arr.shape[0]/2)
            or (not is_most_common and sum_bit_all_lines < lines_arr.shape[0]/2)):
            common_bits[i] = 1
            bit = 1

        out = (out << 1) | bit 
    return out, common_bits


def common_single_bit(arr, is_most_common):
    sum_bits = arr.sum()
    arr_half_size = len(arr) /2
    if ((is_most_common and sum_bits > arr_half_size) 
        or (not is_most_common and sum_bits < arr_half_size)
        or (is_most_common and sum_bits == arr_half_size)):
        return 1
    return 0

def life_support_rating(lines_arr, is_most_common):
    out = 0

    for i in range(lines_arr.shape[0]):
        bit = common_single_bit(lines_arr[:, i], is_most_common)
        is_equal_places = np.where(lines_arr[:, i] == bit)[0]
        lines_arr = lines_arr[is_equal_places, :]
        if len(lines_arr) == 1:
            break

    for bit in lines_arr[0]:
        out = (out << 1) | bit

    return out


lines = read_data_file(3, False)
lines = [[int(x) for x in line.strip()] for line in lines]
lines_arr = np.array(lines)

# part 1
gamma, _ = is_common(True, lines_arr)
epsilon, _ = is_common(False, lines_arr)
print(gamma * epsilon)

#part 2
oxygen = life_support_rating(lines_arr, is_most_common=True)
CO2 = life_support_rating(lines_arr, is_most_common=False)
print(CO2 * oxygen)
