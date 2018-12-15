# Set can be created by using braces around primitive types
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)
print(type(farm_animals))

for animal in farm_animals:
    print(animal)
print("=" * 40)

# Set can be created by using the set function on a list
wild_animals = ["lion", "tiger", "panther", "elephant", "hare"]
print(type(wild_animals))
print(wild_animals)

wild_animals = set(wild_animals)
print(type(wild_animals))
print(wild_animals)

for animal in wild_animals:
    print(animal)

# New items can added to a set by using the add method
farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

# Empty sets must be created with the set function. Empty braces
# create a empty dictionary.
empty_set = set()
empty_braces = {}
print(" set() creates {0}.".format(type(empty_set)))
print(" {{}} creates {0}".format(type(empty_braces)))


# Example of Union functions for sets.
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))


# Intersection Function in Sets can be used by using
# either the intersection function or '&" symbol
print("=" * 40)
print(even.intersection(squares))
print(even & squares)
print(sorted(even - squares))

# Python a set can not contain duplicate value
two_even = [2, 2, 4, 6, 6, 8, 8, 10, 10, 10, 12, 12, 12, 12, 14, 14]
print("A list {} can have duplicate value".format(two_even))
two_even = set(two_even)
print("The same list converted to a set {} only contains unique values."
      .format(two_even))


