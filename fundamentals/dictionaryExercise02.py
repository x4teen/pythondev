cities = {"New York": 9000000,
          "London": 4000000,
          "Tokyo": 38140000,
          "Mumbai": 21357000,
          "Beijing": 21500000,
          "Istanbul": 14000000,
          "Shanghai": 24000000,
          "New York": 10000000,
          "Sydney": 5000000}

print("=" * 50)
print("{0:20}\t{1:>15}".format("City", "Population"))
print("-" * 50)
cityCount = 0
populationTotal = 0

for city in cities:
    print("{0:20}\t{1:>15,}".format(city, cities[city]))
    cityCount += 1
    populationTotal += cities[city]
print("=" * 50)
print("Cities : {0:<11}\t{1:>15,}".format(cityCount, populationTotal))
print()

print(cities.items())
cityTuple = tuple(cities.items())
print(cityTuple)
print("=" * 50)

for city in cityTuple:
    cityName, cityPopulation = city
    print("{0:20}\t{1:>15,}".format(cityName, cityPopulation))




