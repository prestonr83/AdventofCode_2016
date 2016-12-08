

INPUT = "input.txt"


def parse_input():
    valid_items = 0
    lines = 0
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines += 1
            numbers = line.split()
            position = 0
            for num in numbers:

    return (valid_items, lines)


if __name__ == "__main__":
    valid = parse_input()
    print("{} of {} triangles are possible".format(valid[0], valid[1]))
