# for i in range(1, 20):
#     print("The value of i is now {0}".format(i))

number = "912,23483,69589,669659"
cleanNumber = ''

for i in range(len(number)):
    if number[i] in ".0123456789":
        cleanNumber = cleanNumber + number[i]

finalNumber = int(cleanNumber)
print("The final result is {0}".format(finalNumber))

