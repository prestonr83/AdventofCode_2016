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

def decomp_len(line, type):
    output = 0
    temp = line
    marker_dict = {}
    calc_dict = {}
    markers = re.findall(r'(\([0-9]+x[0-9]+\))', temp)
    base_len = len(temp)
    for marker in markers:
        base_len -= len(marker)
        mkr_pos = re.search(marker, temp)
        mkr_select , mkr_repeat = mkr_pos.group().split('x') 
        marker_dict[mkr_pos.start() - 1] = [int(mkr_select), int(mkr_repeat), len(marker)]
        print "ok"
    while True:
        count = 0
        for key in marker_dict.keys():
            if key in calc_dict.keys():
                continue
            chk_lst = range(marker_dict[key][2]+key,key+marker_dict[key][0]+marker_dict[key][2])
            last_marker = key
            while True:
                for i in chk_lst:
                    if i in marker_dict.keys() and len(marker_dict[i]) == 3: 
                        chk_lst = range(marker_dict[i][2]+i,i+marker_dict[i][0]+marker_dict[i][2])
                        last_marker = i
                        count += 1
                        continue
                    if len(marker_dict[i]) == 4:
                        marker_dict[last_marker][0] += marker_dict
                if len(marker_dict[last_marker]) == 3:    
                    marker_dict[last_marker][0] += marker_dict[last_marker][0]+last_marker+marker_dict[last_marker][2]
                    marker_dict[last_marker].append(True)
                break
        if count == 0:
            break

def decomp(line):
    output = ''
    temp = line
    total_len = len(re.sub(r'\([0-9]+x[0-9]+\)', '', line))
    marker_dict = {}
    while True:
        reg = re.search(r'\(([0-9]+)x([0-9]+)\)', temp)
        if not reg:
            break
        


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
<<<<<<< HEAD
    decomp_len(data, "test")
=======
    while True:
        compressed = re.search(r'\(([0-9]+)x([0-9]+)\)', expanded)
        round = 0
        if compressed:
            round += 1
            sys.stdout.write("Round {} = {}\n".format(round, len(expanded)))
            sys.stdout.flush()
            expanded = decomp(expanded)
        else:
            break
>>>>>>> 8f61400f74ec4331bfbd9b5cc97eaa6f7df8813e
    v2len = len(expanded)
    print("Version 2 length is {}".format(v2len))
