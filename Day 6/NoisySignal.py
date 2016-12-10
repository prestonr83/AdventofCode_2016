import itertools
import os

INPUT = "{}/input.txt".format(os.getcwd())

def load_input():
    lines = []
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines.append(line.strip("\n"))
    return lines


def parse_input():
    input_dict = {}
    for enum, line in enumerate(load_input()):
        ln_list = [i for i in line]
        input_dict[enum] = ln_list
    return input_dict

def  get_freq_ltr(ltr_list, freq):
    unq_ltr = set(ltr_list)
    tmp = {}
    for ltr in unq_ltr:
        try:
            key = tmp[ltr_list.count(ltr)]
        except KeyError:
            tmp[ltr_list.count(ltr)] = []
            key = tmp[ltr_list.count(ltr)]
        key.append(ltr)
    cnt = [i for i in tmp.keys()]
    cnt.sort()
    if freq:
        cnt.reverse()
    tmp[cnt[0]].sort()
    return tmp[cnt[0]][0]

def decode_msg(input_dict, freq=True):
    msg = ''
    for i in range(len(input_dict[0])):
        col_list = []
        for j in range(len(input_dict.keys())):
            col_list.append(input_dict[j][i])
        msg += get_freq_ltr(col_list, freq)
    return msg

def main():
    print(decode_msg(parse_input()))

if __name__ == "__main__":
   pt1_msg = decode_msg(parse_input())
   pt2_msg = decode_msg(parse_input(), freq=False)
   print("Part 1 decoded message is '{}'".format(pt1_msg))
   print("Part 2 decoded message is '{}'".format(pt2_msg))