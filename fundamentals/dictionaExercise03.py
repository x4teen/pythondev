cities = {"New York": 9000000,
          "London": 4000000,
          "Tokyo": 38140000,
          "Mumbai": 21357000,
          "Beijing": 21500000,
          "Istanbul": 14000000,
          "Shanghai": 24000000,
          "New York": 10000000,
          "Sydney": 5000000}

cities_Country = {"New York": "United States",
                  "London": "United Kingdom",
                  "Tokyo": "Japan",
                  "Mumbai": "India",
                  "Beijing": "China",
                  "Istanbul": "Turkey",
                  "Shanghai": "China",
                  "New York": "NY State",
                  "Sydney": "Australia"}

countries = ", ".join(cities_Country)
print(countries)
countries = list(cities_Country.keys())
print(countries)

cities.update(cities_Country)
print(cities.items())
