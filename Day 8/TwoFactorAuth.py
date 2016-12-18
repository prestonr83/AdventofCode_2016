import os
import re
from collections import deque


PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(PATH)
INPUT = "{}/input.txt".format(DIR_PATH)

class SimpleLCD(object):
    def __init__(self, input):
        self.SCREEN = None
        self.INPUT = INPUT
        self.LINES = None
        self.DATA_POS = 0
        
    def setup_screen(self, row, col):
        self.SCREEN = deque([])
        for i in range(col):
            self.SCREEN.append(deque(0 for i in range(row)))

    def load_input(self):
        lines = []
        with open(self.INPUT, mode="r") as data:
            for line in data.readlines():
                lines.append(line.strip("\n"))
        self.LINES = lines

    def process_input(self):
        for line in self.LINES:
            self.DATA_POS += 1
            num_1, num_2 = map(int, re.findall(r'[0-9]+', line))
            if 'rect' in line:
                self.draw_rect(num_1, num_2)
            if 'row' in line:
                self.rotate_row(num_1, num_2)
            if 'column' in line:
                self.rotate_col(num_1, num_2)

    def rotate_row(self, pos, pxl):
        self.SCREEN[pos].rotate(pxl)

    def rotate_col(self, pos, pxl):
        col = deque([i[pos] for i in self.SCREEN])
        col.rotate(pxl)
        for i in range(len(col)):
            self.SCREEN[i][pos] = col[i]

    def draw_rect(self, row ,col):
        for i in range(col):
            for j in range(row):
                self.SCREEN[i][j] = 1

    @property
    def pixel_count(self):
        pixels = len([ x for y in self.SCREEN for x in y if x == 1])
        return pixels

    @property
    def display(self):
        output = None
        for row in self.SCREEN:
            if output:
                output += '\n'
            else:
                output = ''
            for col in row:
                if col == 0:
                    output += ' '
                elif col == 1:
                    output += '█'
        return output


if __name__ == '__main__':
    try:
        screen = SimpleLCD(INPUT)
        print("Initializing screen...")
        screen.setup_screen(50,6)
        print("Loading input data...")    
        screen.load_input()
        print("Processing input...")
        screen.process_input()
        pixels = screen.pixel_count
        print("There are {} pixels lit up").format(pixels)
        print(screen.display)
    except Exception as ERROR:
        print("ERROR processing data on line {}").format(screen.DATA_POS)
        print(ERROR)
