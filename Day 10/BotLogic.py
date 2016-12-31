import os
import re


PATH = os.path.abspath(__file__)
DIR_PATH = os.path.dirname(PATH)
INPUT = "{}/input.txt".format(DIR_PATH)


def load_input():
    lines = []
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines.append(line.strip("\n"))
    return lines

def load_bot_dict(input):
    bot_dict = {}
    output_dict = {}
    for line in input:
        matches = re.findall(r'(bot|value|output) ([0-9]+)', line)
        if matches[0][1] == '66':
            pass
        if matches[0][0] == 'bot':
            bot_inst = None
            for index, (typ, bot) in enumerate(matches):
                if typ == 'output':
                    if bot not in output_dict.keys():
                        output_dict[bot] = []
                    bot = 'o' + bot
                if index == 0:
                    bot_inst = bot
                if index == 1:
                    bot_dict[bot_inst][1]['low'] = bot
                if index == 2:
                    bot_dict[bot_inst][1]['high'] = bot
                if bot not in bot_dict.keys() and typ != 'output':
                        bot_dict[bot] = [[], {'low' : None, 'high': None}]
        if matches[0][0] == 'value':
            if matches[1][1] not in bot_dict.keys():
                bot_dict[matches[1][1]] = [[], {'low' : None, 'high': None}]
            bot_dict[matches[1][1]][0].append(matches[0][1])
    return (bot_dict, output_dict)

def process_load(bot_dict, output_dict):
    part1 = None
    while True:
        for k, v in bot_dict.items():
            pop = [False, False]
            if len(v[0]) == 2:
                v[0]= [int(i) for i in v[0]]
                v[0].sort()
                if [17, 61] == v[0]:
                    part1 = k
                high = v[0][1]
                low = v[0][0]
                if v[1]['low'].startswith('o'):
                    output_dict[v[1]['low'].strip('o')].append(low)
                    pop[0] = True
                elif len(bot_dict[v[1]['low']][0]) != 2:
                    bot_dict[v[1]['low']][0].append(low)
                    pop[0] = True
                if v[1]['high'].startswith('o'):
                    output_dict[v[1]['high'].strip('o')].append(high)
                    pop[1] = True
                elif len(bot_dict[v[1]['high']][0]) != 2:
                    bot_dict[v[1]['high']][0].append(high)
                    pop[1] = True
                if pop[0]:
                    bot_dict[k][0].remove(low)
                if pop[1]:
                    bot_dict[k][0].remove(high)
        chip_qty = [True if len(v[0]) == 0 else False for v in bot_dict.values()]
        if all(chip_qty):
            return (part1, output_dict)




if __name__ == "__main__":
    bot_dict = load_bot_dict(load_input())
    output = process_load(*bot_dict)
    print("Bot {} compares chips 61 and 17").format(output[0])
    print("{} is the total of output 0 * output 1 * output 2".format(output[1]['0'][0]*output[1]['1'][0]*output[1]['2'][0]))