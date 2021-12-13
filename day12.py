from utils import read_data_file

def count_paths(cur_path, nodes, lower_nodes, twice=False):
    if cur_path[-1] == 'end':
        return 1
        
    res = 0

    for adjacent in nodes[cur_path[-1]]:
        if adjacent not in cur_path or adjacent not in lower_nodes:
            res += count_paths(cur_path+[adjacent], nodes, lower_nodes, twice)
        elif twice:
            res += count_paths(cur_path+[adjacent], nodes, lower_nodes, False)

    return res
    

lines = read_data_file(12, False)
nodes = {'start':[]}
lower_nodes = ['start']

for line in lines:
    cur_nodes = line.strip().split('-')
    
    if 'start' == cur_nodes[0]:
        nodes['start'].append(cur_nodes[1])
    elif 'start' == cur_nodes[1]:
        nodes['start'].append(cur_nodes[0])
    else:
        for i in [0,1]:
            cur_node = cur_nodes[i]
            if cur_node in nodes:
                nodes[cur_node].append(cur_nodes[1-i])
            else:
                nodes[cur_node] = [cur_nodes[1-i]]
                if cur_node.islower():
                    lower_nodes.append(cur_node)

res = count_paths(['start'], nodes, lower_nodes)
print(res)

res = count_paths(['start'], nodes, lower_nodes, True)
print(res)