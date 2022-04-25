b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyx0123456789+/"

b64 = "aG9nZWhvZ2U=" # hogehoge
b64_bin = ""

origin = ""

b64 = b64.replace("=", "") # padding削除

for s in b64:
    index = b64map.find(s)
    b64_bin += str('{:06b}'.format(index))

for i in range(0, len(b64_bin), 8):
    origin += chr(int(b64_bin[i:i+8], 2))

print(origin)