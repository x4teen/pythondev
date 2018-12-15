import shelve

# with shelve.open('dataCity') as cities:
cities = shelve.open("dataCity")
cities["New York"] = 9000000
cities["London"] = 4000000
cities["Tokyo"] = 38140000
cities["Mumbai"] = 21357000
cities["Beijing"] = 21500000
cities["Istanbul"] = 14000000
cities["Shanghai"] = 24000000

for city, population in cities.items():
    print("{0:15}\t{1:>15,}".format(city, population))

print(type(cities))
print(cities)
print()

cities.close()

print("=" * 50)
cities = shelve.open("dataCity", 'a')
cities["Sydney"] = 7000000
cities["New York"] = 12000000

for city in cities:
    print("{0:15}\t{1:>15,}".format(city, cities[city]))

print(type(cities))
print(cities)
print()


while True:
    city_requested = input("Enter a city name or type quit to close the program : ")
    if city_requested == "quit":
        break
    elif cities.get(city_requested) is None:
        print("We don't have any data on {}. Try another".format(city_requested))
    else:
        population = cities.get(city_requested)
        print("{0:15}\t{1:>15,}".format(city_requested, population))

cities.close()







