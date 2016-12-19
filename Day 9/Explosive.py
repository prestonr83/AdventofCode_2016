import os
import re
import sys
from collections import deque


PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(PATH)
INPUT = "{}/input.txt".format(DIR_PATH)

def load_input():
        lines = []
        with open(INPUT, mode="r") as data:
            for line in data.readlines():
                lines.append(line.strip("\n"))
        if len(lines) == 1:
            return lines[0]
        return lines

def decomp(line):
    output = ''
    temp = line
    while True:
        start = re.search(r'(^[a-zA-Z0-9]+)\(?', temp)
        reg = re.search(r'\(([0-9]+)x([0-9]+)\)', temp)
        if start:
            output += start.group(1)
        if not reg:
            break
        repeat = int(reg.group(2))
        start_pos = reg.start() + len(reg.group())
        end_pos = int(reg.group(1)) + start_pos
        for i in range(repeat):
            output += temp[start_pos:end_pos]
        temp = temp[end_pos:]
        sys.stdout.write("\rchars left to process {}".format(len(temp)))
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    return output

if __name__ == '__main__':
    data = load_input()
    expanded = decomp(data)
    length = len(expanded)
    print("Version 1 length is {}".format(length))
    while True:
        compressed = re.search(r'\(([0-9]+)x([0-9]+)\)', expanded)
        round = 0
        if compressed: 
            round += 1
            sys.stdout.write("Round {} = {}".format(round, len(expanded)))
            sys.stdout.flush()
            expanded = decomp(expanded)
        else:
            break
    v2len = len(expanded)
    print("Version 2 length is {}".format(v2len))
