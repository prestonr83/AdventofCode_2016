import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
INPUT = "{}/input.txt".format(dir_path)

SCREEN = []

def setup_screen(x,y):
    pass

def load_input():
    lines = []
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines.append(line.strip("\n"))
    return lines