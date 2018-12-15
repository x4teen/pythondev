import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

print(type(imelda))
even = range(0, 20, 2)
odd = range(1, 20, 2)
x = 2998302

with open("imelda", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(x, pickle_file)

with open("imelda", "rb") as pickle_file:
    imelda_data = pickle.load(pickle_file)
    list_01 = pickle.load(pickle_file)
    list_02 = pickle.load(pickle_file)
    num_01 = pickle.load(pickle_file)

print(imelda_data)
print(type(imelda_data))
print()

print("=" * 50)
album, artist, year, tracks = imelda_data
print("Artist:\t{0}\nAlbum:\t{1}\nYear:\t{2}\nTracks:".format(artist, album, year))

for songs in tracks:
    print("{0}.\t{1}".format(songs[0], songs[1]))
print("=" * 50)
print()

print("=" * 50)
print("{0:^50}".format("Other Data"))
print("=" * 50)

print("Even List : ", end="")
for i in list_01:
    print(i, end=" ")
print()

print("Odd List : {0}".format(list_02))
print("Number : {0:,}".format(num_01))

