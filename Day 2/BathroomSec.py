
INSTRUCTIONS = "instructions.txt"

KEYPAD = {
          0 : [1,2,3],
          1 : [4,5,6],
          2 : [7,8,9],
         }

RULES = {
        'U' : [-1, 0],
        'D' : [1, 0],
        'L' : [0, -1],
        'R' : [0, 1]
        }

DIAMONDPAD = {0: [None, None, 1, None, None],
              1: [None, 2, 3, 4, None],
              2: [5,6,7,8,9],
              3: [None, "A", "B", "C", None],
              4: [None, None, 'D', None, None]
             }

CODE = None

def read_instructions(k_pad, row, col):
    global CODE
    CODE = []
    with open(INSTRUCTIONS, mode='r') as instruct:
        for line in instruct.readlines():
            CODE.append(decode_line(line.strip("\n"), k_pad, row, col))
    return CODE

def decode_line(line, k_pad, row, col):
    row = row
    col = col
    for ltr in line:
        change = RULES[ltr]
        temprow = row + change[0]
        tempcol = col + change[1]
        if temprow > -1 and tempcol > -1:
            try:
                if k_pad[temprow][tempcol]:
                    col = tempcol
                    row = temprow
            except (KeyError, IndexError):
                pass
    return k_pad[row][col]

if __name__ == "__main__":
    read_instructions(KEYPAD, 1, 1)
    print("The bathroom code is {}".format("".join(map(str, CODE))))
    read_instructions(DIAMONDPAD, 2, 0)
    print("The actual bathroom code is {}".format("".join(map(str, CODE))))