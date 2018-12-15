t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))


welcome = "Welcome to my Nightmare", "Alice Cooper", 1975, (
    (1, "Welcome to My Nightmare", 5.19), (2, "Devil's Food", 3.38),
    (3, "Some Folks", 4.19), (4, "Only Women Bleed", 5.49)
)
title, artist, year, tracks = welcome

print("-"*40)
print(" " * 10, title)
print("-" * 40)
print("Artist: {0}\tReleased: {1}".format(artist, year))
print("Tracks : ")
for track in tracks:
    for item in track:
        print("\t", item, end="\t")
    print()

