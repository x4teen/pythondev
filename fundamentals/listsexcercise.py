print("====== LIST EXERCISE 02 =====")
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
result_set = [even, odd]
result_list = even + odd

print(" Set : {0}".format(result_set))
print(" List : {0}".format(result_list))

for set_item in result_set:
    print(set_item)
    for value in set_item:
        print(value)

print()
print("====== LIST EXERCISE 02 =====")
menu = []
menu.append(['spam', 'ham', 'sausage', 'pancakes', 'bacon', 'eggs', 'potato'])
menu.append(['ham', 'sausage', 'pancakes', 'bacon', 'eggs', 'potato'])
menu.append(['spam', 'ham', 'sausage', 'pancakes', 'eggs', 'potato'])
menu.append(['sausage', 'pancakes', 'bacon', 'eggs', 'potato'])
menu.append(['spam', 'ham', 'bacon', 'eggs'])
menu.append(['spam', 'ham', 'sausage', 'pancakes', 'potato'])
menu.append(['spam', 'pancakes', 'bacon', 'eggs', 'potato'])
menu.append(['ham', 'sausage', 'pancakes', 'bacon', 'eggs'])

for meal in menu:
    if not 'spam' in meal:
        for food in meal:
            print(food)

trees = ["Larch", "Birch"]
my_garden = trees
trees.append("Chestnut")
print(my_garden)
