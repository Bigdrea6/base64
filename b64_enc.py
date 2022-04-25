b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx0123456789+/"

origin = "hogehoge" # aG9nZWhvZ2U=
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