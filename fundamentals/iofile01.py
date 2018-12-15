jabber = open('sample.txt', 'r')

# A file is a stream object that has lines
# we can read one line at a time
for line in jabber:
    if 'time' in line.lower():
        print(line, end='')

jabber.close()
print()

print("=" * 80)
with open('sample.txt') as jabber:
    for line in jabber:
        if 'age' in line.lower():
            print(line, end='')


# We can also read all lines together and get
# a list object after reading the lines
print()
print("=" * 80)
with open('sample.txt') as jabber:
    lines = jabber.readlines()
    print(lines)
    print()

with open('results.txt', 'a') as results_file:
    for line in lines:
        if 'time' in line.lower():
            print("Line {0:3}:\t{1}".format(lines.index(line), line),
                  file=results_file, flush=True)
