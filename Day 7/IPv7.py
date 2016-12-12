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

def parse_address(addr):
    addr_list = re.split(r'(\[|\])', addr)
    return addr_list

def chk_address(addr_list):
    for i in range(len(addr_list)):
        if addr_list[i] == ']' or addr_list[i] =='[':
            continue
        if i > 0 and addr_list[i-1] == "[":
            hnet = tls_chk(addr_list[i])
            if hnet:
                return False
        else:
            status = tls_chk(addr_list[i])
            if status:
                return True
    return False

def tls_chk(addr_segment):

    for i in range(len(addr_segment)):
        ltr_set1 = list(addr_segment[i:i+2])
        ltr_set2 = list(addr_segment[i+2:i+4])
        if len(ltr_set2) < 2:
            break
        if ltr_set1 == ltr_set2:
            continue
        ltr_set2.reverse()
        if ltr_set1 == ltr_set2:
            return True
    return False

def main():
    tls = {
        'enabled' : 0,
        'disabled' : 0
        }
    addr_list = load_input()
    for raw_addr in addr_list:
        addr = parse_address(raw_addr)
        if chk_address(addr):
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

