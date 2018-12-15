even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

list_01 = list(range(0, 5, 2))
list_02 = list(range(0, 6, 2))

print(list_01)
print(list_02)
print(list_01 == list_02)

r = range(0, 101)
print(r)

print("*" * 30)

for i in r[::-5]:
    print(i)

myString = "Python is a very powerful language"
backString = myString[::-1]

print(myString)
print(backString)

