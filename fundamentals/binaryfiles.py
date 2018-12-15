# Reading and writing binary files.
# Data must be converted to bytes before writing to binary files.

# Converting binary data using byte method.
with open("binarydata", "bw") as bin_file:
    bin_file.write(bytes(range(17)))

# Reading binary data
with open("binarydata", "br") as bin_file:
    for num in bin_file:
        print(num)
print()


# ********* EXERCISE 02 **********
print("=" * 50)
print("{0:^50}".format("Binary Exercise 02"))
print("=" * 50)

a = 65534       #FF FE
b = 65535       #FF FF
c = 65536       #00 01 00 00
d = 2998302     #02 2D C0 1E

with open("binarydata02", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))


with open("binarydata02", "br") as bin_file:
    a = int.from_bytes(bin_file.read(2), 'big')
    print("a = {}".format(a))
    b = int.from_bytes(bin_file.read(2), 'big')
    print("b = {}".format(b))
    c = int.from_bytes(bin_file.read(4), 'big')
    print("c = {}".format(c))
    d = int.from_bytes(bin_file.read(4), 'big')
    print("d = {}".format(d))
    d2 = int.from_bytes(bin_file.read(4), 'little')
    print("d (little) = {}".format(d2))

print()
