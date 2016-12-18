import os
import re
from collections import deque


PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(PATH)
INPUT = "{}/input.txt".format(DIR_PATH)

def load_input():
        lines = []
        with open(INPUT, mode="r") as data:
            for line in data.readlines():
                lines.append(line.strip("\n"))
        return lines

def decomp_len(lines):
  output = ''
  for line in lines:
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
    length = decomp_len(data)
    print(length)