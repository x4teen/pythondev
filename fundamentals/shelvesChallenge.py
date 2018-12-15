import shelve

books = shelve.open("books")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "toast": ["bread", "butter"],
                    "omelette": ["eggs", "chives", "butter", "cheese"],
                    "soup": ["potato", "chicken broth", "rosemary", "cream"],
                    "pasta": ["pasta", "sausage", "basil", "pepper", "sun dried tomato"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape", "glue"]}



print(books)
print()

print(books["recipes"]["pasta"])
print(books["recipes"]["omelette"])
print(books["maintenance"]["stuck"])