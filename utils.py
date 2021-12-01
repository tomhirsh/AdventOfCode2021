import os

def read_data_file(day_num, example=False):
    path = os.path.join('inputs',f'day{day_num}')
    
    if example:
        path += '_ex'
    path += '.in'

    with open(path, 'r') as f:
        lines = f.readlines()
    return lines
    