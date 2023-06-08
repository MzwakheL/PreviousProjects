class Album:
    def __init__(self, albumName, albumArtist, numberOfSongs):
        self.albumName = albumName
        self.albumArtist = albumArtist
        self.numberOfSongs = numberOfSongs

    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"


albums1 = [
    Album("Album1", "Artist1", 10),
    Album("Album2", "Artist2", 5),
    Album("Album3", "Artist3", 8),
    Album("Album4", "Artist4", 12),
    Album("Album5", "Artist5", 7)
]
for album in albums1:
    print(album)
print()

albums1.sort(key=lambda album: album.numberOfSongs)
for album in albums1:
    print(album)
print()

albums1[1], albums1[2] = albums1[2], albums1[1]
for album in albums1:
    print(album)
print()

albums2 = [
    Album("Album6", "Artist6", 15),
    Album("Album7", "Artist7", 9),
    Album("Album8", "Artist8", 11),
    Album("Album9", "Artist9", 6),
    Album("Album10", "Artist10", 14)
]
for album in albums2:
    print(album)
print()

albums2.extend(albums1)
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))
for album in albums2:
    print(album)
print()

albums2.sort(key=lambda album: album.albumName)
for album in albums2:
    print(album)
print()

dark_side_index = next((i for i, album in enumerate(albums2) if album.albumName == "Dark Side of the Moon"), None)
if dark_side_index is not None:
    print(f"The index of 'Dark Side of the Moon' is {dark_side_index}")
else:
    print("'Dark Side of the Moon' was not found in the list")




#reference - https://www.programiz.com/python-programming/methods/list/sort