number = '1234567890'
for digit in number:
    print(digit)

my_iterator = iter(number)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


print("""

***** CHALLENGE 01 *****

""")

name = "Yasmeen Khan"
my_iterator = iter(name)

for i in range(len(name)):
    print(next(my_iterator), end=' ')
