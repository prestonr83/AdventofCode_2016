import itertools
import os

INPUT = "{}/input.txt".format(os.getcwd())

def valid_tri(numbers):
    combos = get_combos(numbers)
    results = []
    for combo in combos:
        tempnumbers = list(numbers)
        sum_len = combo[0] + combo[1]
        for i in combo:
            del tempnumbers[tempnumbers.index(i)]
        if sum_len > tempnumbers[0]:
            results.append(True)
            continue
        results.append(False)
    return all(result for result in results)

def parse_input():
    lines = 0
    tri_dict = {}
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            numbers = [int(i) for i in line.split()]
            tri_dict[lines] = numbers
            lines += 1
    return tri_dict

def col_check(triangles, item, valid_items=0, index=0):
    try:
        triangles[index]
    except KeyError:
        return valid_items
    numbers = []
    for i in range(3):
        numbers.append(triangles[index][item])
        index += 1
    valid = valid_tri(numbers)
    if valid:
        valid_items += 1
    return col_check(triangles, item, valid_items=valid_items, index=index)

def line_check(triangles, direction):
    total_items = len(list(triangles.keys()))
    valid_items = 0
    if direction == "row":
        for key in triangles.keys():
            valid = valid_tri(triangles[key])
            if valid:
                valid_items += 1
    if direction == "col":
        for i in range(3):
            valid_items += col_check(triangles, i)
    return(valid_items, total_items)

def get_combos(numbers):
    combos = []
    for combo in itertools.combinations(numbers, 2):
        combos.append(combo)
    return combos

if __name__ == "__main__":
    ITEMS = parse_input()
    R_CNT = line_check(ITEMS, "row")
    C_CNT = line_check(ITEMS, "col")
    print("{} of {} triangles are possible by row".format(R_CNT[0], R_CNT[1]))
    print("{} of {} triangles are possible by column".format(C_CNT[0], C_CNT[1]))
