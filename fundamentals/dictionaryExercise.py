cities = {"New York": 9000000,
          "London": 4000000,
          "Tokyo": 38140000,
          "Mumbai": 21357000,
          "Beijing": 21500000,
          "Istanbul": 14000000,
          "Shanghai": 24000000,
          "New York": 10000000}
print(cities)
print("=" * 50)
for city in cities:
    print(city, "\t", cities[city])


cities["Sidney"] = 5000000
del cities["Istanbul"]
city_keys = list(cities.keys())
city_keys.sort()

print("=" * 50)
print("{0:20}\t{1:>15}".format("City", "Population"))
print("-" * 50)
for city in city_keys:
    print("{0:20}\t{1:>15,}".format(city, cities[city]))
print("=" * 50)
print()

while True:
    city = input("Please enter a city name:")
    if city == 'exit':
        break
    population = cities.get(city)
    if population is None:
        print("No data available for {0}.".format(city))
    else:
        print("The population of {0} is {1:,}".format(city, population))


