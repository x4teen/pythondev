name = input("Please enter your name : ")
age = int(input("How old are you, {0}?".format(name)))
print("{1} at the age of {0}, ".format(age, name))

if age >= 21:
    print("you can both vote and drink.")
elif age >= 18:
    print("you are old enough to vote but not old enough to drink.")
else:
    print("you can vote in {0} years and drink in {1} years.".format(18-age, 21-age))

if (age > 18) and (age < 65):
    print("You are of working age.")
elif (age < 18) and (age > 5):
    print("You should be in school")
else:
    print("You are at home today.")

