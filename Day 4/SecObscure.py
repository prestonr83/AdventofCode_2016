import os
import string

INPUT = "{}/input.txt".format(os.getcwd())


def load_alphabet():
    alphabet = {}
    for index, ltr in enumerate(string.lowercase, 1):
        alphabet[index] = ltr
        alphabet[ltr] = index
    return alphabet

def load_input():
    lines = []
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines.append(line.strip("\n"))
    return lines

test = 'aaaaa-bbb-z-y-x-123[abxyz]'

def parse_line(line):
    rm_list = line.strip("]").replace("[", "-").split("-")
    enc_room = rm_list[:-2]
    sector = int(rm_list[-2])
    chksum = rm_list[-1]
    return (enc_room, sector, chksum)

def get_chksum(enc_room):
    enc_room = "".join(enc_room)
    unq_chars = set(enc_room)
    room_chars = list(enc_room)
    tmp = {}
    chksum = ''
    for char in unq_chars:
        try:
            key = tmp[room_chars.count(char)]
        except KeyError:
            tmp[room_chars.count(char)] = []
            key = tmp[room_chars.count(char)]
        key.append(char)
    cnt = [i for i in tmp.keys()]
    cnt.sort()
    cnt.reverse()
    for i in cnt:
        chars = tmp[i]
        chars.sort()
        chksum += "".join(chars)
    return chksum

def decode(enc_room, sector):
    room_name = ""
    for word in enc_room:
        for ltr in word:
            ltr_pos = ALPHABET[ltr]
            mod = sector % 26
            result = ltr_pos + mod
            if result > 26:
                pos = result - 26
                room_name += ALPHABET[pos]
                continue
            room_name += ALPHABET[result]
        room_name += " "
    return room_name.strip()


ALPHABET = load_alphabet()


def main():
    id_sum = 0
    data = load_input()
    for item in data:
        enc_room, sector, chksum = parse_line(item)
        result = get_chksum(enc_room)
        if result.startswith(chksum):
            id_sum += sector
            room_name = decode(enc_room, sector)
            keywords = ['northpole', 'storage', 'object']
            chk = [True if i in room_name.split() else False for i in keywords]
            if all(chk):
                storage = [room_name, sector]
    return (id_sum, storage[0], storage[1])

if __name__ == "__main__":
    ID_SUM, NAME, SECTOR = main()
    print("The sum of the sector IDs of real rooms is {}".format(ID_SUM))
    print("The room where North Pole objects are stored is called '{}' with a"
          " sector ID of {}".format(NAME, SECTOR))
