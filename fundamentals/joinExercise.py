myList = ["New York", "Chicago", "Los Angeles", "Las Vegas", "Philadelphia"]

newList = " == ".join(myList)

print(myList)
print(newList)

locations = {0: "Computer",
             1: "Brick Building at End of Road",
             2: "Top of Hill",
             3: "Well House for Stream",
             4: "Valley by Stream",
             5: "Forest"}

doors = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableDoors = ""
    availableDoors = ", ".join(doors[loc].keys())
    print("You are in {0}".format(locations[loc]))

    if loc == 0:
        break

    direction = input("Choose from the following available doors : {} "
                      .format(availableDoors.upper()))
    print()

    if direction in doors[loc]:
        loc = doors[loc][direction]
    else:
        print("Choice not available. Please make another choice.")
    





