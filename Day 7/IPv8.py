import re
import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
INPUT = "{}/input.txt".format(dir_path)

def load_input():
    lines = []
    with open(INPUT, mode="r") as data:
        for line in data.readlines():
            lines.append(line.strip("\n"))
    return lines

def tls_address(addr_list):
    hnet = False
    tls = False
    for i in range(len(addr_list)):
        if addr_list[i] == ']' or addr_list[i] =='[':
            hnet = not hnet
            continue
        if ']' in addr_list[i:i+4]:
            continue
        ltr_set1 = list(addr_list[i:i+2])
        ltr_set2 = list(addr_list[i+2:i+4])
        if len(ltr_set2) < 2:
            if tls:
                return True
            return False
        if ltr_set1 == ltr_set2:
            continue
        ltr_set2.reverse()
        if ltr_set1 == ltr_set2:
            if hnet:
                return False
            tls = True

def main():
    tls = {
        'enabled' : 0,
        'disabled' : 0
        }
    addr_list = load_input()
    for raw_addr in addr_list:
        if tls_address(raw_addr):
            tls['enabled'] += 1
        else:
            tls['disabled'] += 1
    output = ("   ADDRESS TLS REPORT\n"
              "------------------------\n"
              "TLS Enabled     : {}\n"
              "TLS Disalbed    : {}\n"
              "Total Addresses : {}".format(tls['enabled'],
                                            tls['disabled'],
                                            len(addr_list)))
    return output

if __name__ == "__main__":
    print(main())

