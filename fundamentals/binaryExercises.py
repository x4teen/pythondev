for i in range(256):
    print("{0:>4} in binary is {0:>08b}, in octal is {0:>08o} and in hexadecimal is {0:08x}".format(i))

x = 0x20
y = 0x0a

print("{0:>2x} + {1:>2x} = {2:3} or {2:3x} in Hex".format(x, y, x+y))
