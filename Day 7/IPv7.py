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
    addr_list = re.findall(r'\[?[a-z]+\]?', addr)
    return addr_list

def chk_address(raw_addr):
    addr_list = parse_address(raw_addr)
    tls_break = False
    tls = False
    ssl = ssl_chk(raw_addr)
    for addr in addr_list:
        if addr[0] == "[":
            hnet = tls_chk(addr.strip("[]"))
            if hnet:
                tls = False
                break
        else:
            if not tls_break:
                status = tls_chk(addr)
                if status:
                    tls = True
    return (tls, ssl)

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

def ssl_chk(raw_addr):
    addr_list = parse_address(raw_addr)
    bab_list = []
    aba_list = []
    for addr in addr_list:
        addr_size = len(addr.strip("[]"))
        if addr[0] == "[":
            hnet = addr.strip("[]")
            for i in range(0,addr_size):
                if i+3 > addr_size:
                    break
                if hnet[i] == hnet[i+2]:
                    bab_list.append(hnet[i:i+3])
        else:
            for i in range(0,addr_size):
                if i+3 > addr_size:
                    break
                if addr[i] == addr[i+2]:
                    aba_list.append(addr[i:i+3])
    for aba in aba_list:
        bab = "{0}{1}{0}".format(aba[1],aba[0])
        if bab in bab_list:
            return True
    return False



def main():
    tls = {
        'enabled' : 0,
        'disabled' : 0
        }
    ssl = {
        'enabled' : 0,
        'disabled' : 0
        }
    addr_list = load_input()
    for raw_addr in addr_list:
        if chk_address(raw_addr)[0]:
            tls['enabled'] += 1
        else:
            tls['disabled'] += 1
        if chk_address(raw_addr)[1]:
            ssl['enabled'] += 1
        else:
            ssl['disabled'] += 1
    output = ("     ADDRESS REPORT\n"
              "------------------------\n"
              "TLS Enabled     : {}\n"
              "TLS Disalbed    : {}\n"
              "SSL Enabled     : {}\n"
              "SSL Disalbed    : {}\n"
              "Total Addresses : {}".format(tls['enabled'],
                                            tls['disabled'],
                                            ssl['enabled'],
                                            ssl['disabled'],
                                            len(addr_list)))
    return output

if __name__ == "__main__":
    print(main())

