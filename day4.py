from numpy.testing._private.utils import break_cycles
from utils import read_data_file
import numpy as np
import re


class BingoTable:
    def __init__(self, table_lines, size=5):
        self.table = np.zeros((size, size), dtype=int)
        for id_line, line in enumerate(table_lines):
            line_stripped_splitted = re.sub("\s+", ",", line.strip()).split(',')
            self.table[id_line] = np.array([int(x) for x in line_stripped_splitted])
        
        # marked is a table that contains 1 where a number was drawn, else 0
        self.marked = np.zeros_like(self.table, dtype=int)

    def play(self, number):
        if number in self.table:
            self.marked[np.where(self.table == number)] = 1

    def is_winner(self):
        if ((True in np.all(self.marked == 1, axis=0)) or 
            (True in np.all(self.marked == 1, axis=1))):
            return True
        return False
    
    def calc_score(self, number):
        unmarked_places = np.where(self.marked == 0)
        sum_unmarked = self.table[unmarked_places].sum()
        return sum_unmarked * number


def play_game(drawings, bingo_tables):
    for draw in drawings:
        for table in bingo_tables:
            table.play(draw)
            if table.is_winner():
                score = table.calc_score(draw)
                return score
    return -1


def play_game_let_squid_win(drawings, bingo_tables):
    have_not_win_yet_tables = list(range(len(bingo_tables)))

    for draw in drawings:
        for idx, table in enumerate(bingo_tables):
            table.play(draw)
            if table.is_winner():
                if len(have_not_win_yet_tables) == 1 and idx in have_not_win_yet_tables:
                    score = table.calc_score(draw)
                    return score
                else:
                    if idx in have_not_win_yet_tables:
                        have_not_win_yet_tables.remove(idx)
    return -1


lines = read_data_file(4)
drawings = [int(x) for x in lines[0].strip().split(',')]
bingo_tables = []

for i in range(int(len(lines[2:])/6)):
    cur_table = BingoTable(lines[5*i+2+i:5*i+7+i])
    bingo_tables.append(cur_table)

# part A
score = play_game(drawings, bingo_tables)
print(score)

# part B
score = play_game_let_squid_win(drawings, bingo_tables)
print(score)


