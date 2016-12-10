import hashlib

DOOR_ID = 'ojvtpuvg'

def getMD5hash(string):
    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()

def crack_pwd(door_id, ordered=True):
    password = ''
    if not ordered:
        password = [0,0,0,0,0,0,0,0]
        positions = [0,1,2,3,4,5,6,7]
    index = 0
    while True:
        md5 = getMD5hash(door_id+str(index))
        index += 1
        if md5.startswith('00000'):
            if ordered:
                password += md5[5]
                print(password)
                if len(password) == 8:
                    return password
            else:
                try:
                    pos = int(md5[5])
                    if int(md5[5]) in positions:
                        password[int(md5[5])] = md5[6]
                        del positions[positions.index(int(md5[5]))]
                        print(password)
                except ValueError:
                    continue
                if len(positions) == 0:
                    return "".join(password)

if __name__ == "__main__":
    password = crack_pwd(DOOR_ID)
    cmp_password = crack_pwd(DOOR_ID, ordered=False)
    print("The password is {}".format(password))
    print("The complex password is {}".format(cmp_password))