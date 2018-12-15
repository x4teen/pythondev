even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 9, 16, 25, 36)
squares = set(squares_tuple)
print(sorted(squares))

# symmetric_difference function picks the
print("Two set difference is ", end=": ")
print(sorted(even.difference(squares)))
print("Symmetric difference is ", end=": ")
print(even.symmetric_difference(squares))

# remove an item from a set
# remove method raises an error if item is not found
squares.remove(9)
print(squares)
# The following line will raise an error
try:
    squares.remove(9)
except KeyError:
    print("The item was not found.")

# discard method raises an error if item is not found
squares.discard(4)
print(squares)
squares.discard(4)      # does not raise an error
print(sorted(squares))

# update method can add multiple items to a set
squares.update({4, 9})
print(sorted(squares))

# issubset or issuperset checks value of super and subsets
print()
print("Square = {0}".format(sorted(squares)))
print("Even = {0}".format(sorted(even)))
sub_test = "is" if squares.issubset(even) else "is not"
super_test = "is" if even.issuperset(squares) else "is not"
print("Square {0} a subset of Even. Even {1} a superset of Square"
      .format(sub_test, super_test))

# try again after removing 4 and 9 from Square
squares -= {9, 25}
print()
print("Square = {0}".format(sorted(squares)))
print("Even = {0}".format(sorted(even)))
sub_test = "is" if squares.issubset(even) else "is not"
super_test = "is" if even.issuperset(squares) else "is not"
print("Square {0} a subset of Even. Even {1} a superset of Square"
      .format(sub_test, super_test))





