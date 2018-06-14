with open('littleschoolbus.bmp', 'rb') as f:
    data = f.read()
    bn = []
    for c in data:
        bn.append(str(ord(c)&1))

def bin2hex(b):
    x = hex(int(b, 2))[2:].replace('L', '')
    return '0' + x if len(x)%2 else x

for i in range(8):
    print bin2hex(''.join(bn) + '0'*i).decode('hex')
