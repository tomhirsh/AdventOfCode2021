from utils import read_data_file

def handle_forward(pos, num_steps):
    pos['horizontal'] += num_steps
    return pos

def handle_up_down(pos, num_steps):
    pos['depth'] += num_steps
    return pos

def handle_forward2(pos, num_steps):
    pos['horizontal'] += num_steps
    pos['depth'] += pos['aim'] * num_steps
    return pos

def handle_up_down2(pos, num_steps):
    pos['aim'] += num_steps
    return pos


def parse_command(line, pos, handle_forward, handle_up_down):
    command, x = line[:-1].split(' ')
    num_steps = int(x)
    if command == 'forward':
        return handle_forward(pos, num_steps)
    elif command == 'up':
        return handle_up_down(pos, -num_steps)
    return handle_up_down(pos, num_steps)

lines = read_data_file(2, False)

# first part
pos = {'horizontal':0, 'depth':0}

for line in lines:
    pos = parse_command(line, pos, handle_forward, handle_up_down)

print(pos['horizontal'] * pos['depth'])


#second part
pos = {'horizontal':0, 'depth':0, 'aim':0}

for line in lines:
    pos = parse_command(line, pos, handle_forward2, handle_up_down2)

print(pos['horizontal'] * pos['depth'])