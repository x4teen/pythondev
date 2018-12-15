import shelve
blt = ["bacon", "lettuce", "tomato", "bread"]
toast = ["bread", "butter"]
omelette = ["eggs", "chives", "butter", "cheese"]
soup = ["potato", "chicken broth", "rosemary", "cream"]
pasta = ["pasta", "sausage", "basil", "pepper", "sun dried tomato"]

with shelve.open('recipes', writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["toast"] = toast
    recipes["omlette"] = omelette
    recipes["soup"] = soup
    recipes["pasta"] = pasta

    for recipe in recipes:
        print("{0} needs {1}".format(recipe, recipes[recipe]))

    recipes["blt"].append("cheese")
    recipes["pasta"].extend(["cheese", "grilled Chicken"])
    print()

    shopping_list = set()
    for recipe in recipes:
        shopping_list.update(set(recipes[recipe]))
        print("{0} needs the following {1} ingredients:\n\t{2}"
              .format(recipe, len(recipes[recipe]), recipes[recipe]))

    print()
    shopping_list = sorted(shopping_list)
    print("Shopping List:")
    count = 0
    for item in shopping_list:
        count += 1
        print("\t{0:2}.\t{1}".format(count,item))
