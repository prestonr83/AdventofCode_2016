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

def decomp_len(line):
    length = i = 0
    while i < len(line):
        if line[i] == '(':
            markerEnd = line.find(')', i)
            (chars, repeat) = [int(x) for x in line[i + 1:markerEnd].split('x')]
            length += decomp_len(line[markerEnd + 1:markerEnd + chars + 1]) * repeat
            i = markerEnd + chars
        else:
            length += 1
        i += 1
    return length

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
    return len(output)


if __name__ == '__main__':
    data = load_input()
    expanded = decomp(data)
    print("Version 1 length is {}".format(expanded))
    fully_expanded = decomp_len(data)
    print("Version 2 length is {}".format(fully_expanded))