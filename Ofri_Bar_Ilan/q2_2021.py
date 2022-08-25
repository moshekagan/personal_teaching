# a = [{"name": "b", "age": 20}, {"name": "a", "age": 30}]
#
# s = sorted(a, key=lambda item: item["name"])
# print(s)

# Q2
song_list = [
    {
        "name": "song number 7",
        "artist": "Arik",
        "popularity": 9999999999,
        "release_date": "01_01_1973",
        "genres": ["israeli", "rock"]
    },
    {
        "name": "song number 6",
        "artist": "Arik",
        "popularity": 9999999999,
        "release_date": "01_01_1973",
        "genres": ["israeli", "pop"]
    },
]

# todo: create dict of genres - counter =>

genres_count = {
    "pop": 1,
    "israeli": 2,
    "rock": 1,
}

# todo: print the genres sorted =>

k = genres_count.keys()  # ["pop", "rock", "israeli"]
sorted_keys = sorted(k)  # ["israeli", "pop", "rock"]

for genre in sorted_keys:
    print(genre + " - " + str(genres_count[genre]))

