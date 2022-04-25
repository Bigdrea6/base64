def b64_enc(b64map):
    origin = input("strings >> ")
    origin_bin = ""

    b64 = ""

    for s in origin:
        origin_bin += str('{:08b}'.format(ord(s)))

    if len(origin_bin) % 6 != 0:
        padding = 6 - (len(origin_bin) % 6)
        origin_bin += "0" * padding

    for i in range(0, len(origin_bin), 6):
        b64 += b64map[int(origin_bin[i:i+6], 2)]

    if len(b64) % 4 != 0:
        padding = 4 - (len(b64) % 4)
        b64 += "=" * padding

    print(b64)

def b64_dec(b64map):
    b64 = input("base64 strings >> ")
    b64_bin = ""

    origin = ""

    b64 = b64.replace("=", "")

    for s in b64:
        index = b64map.find(s)
        b64_bin += str('{:06b}'.format(index))

    for i in range(0, len(b64_bin), 8):
        origin += chr(int(b64_bin[i:i+8], 2))

    print(origin)

if __name__ == "__main__":
    b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx0123456789+/"

    judge = input("Is b64map normal? (y or n) >> ")
    if judge != "y":
        b64map = input("map >> ")
    
    mode = input("mode (e or d) >> ")
    if mode == "e":
        b64_enc(b64map)
    elif mode == "d":
        b64_dec(b64map)