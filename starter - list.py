# topFiveSongs = []
# print("Enter your top 5 songs: ")

# for i in range(5):
#     songs = input()
#     topFiveSongs.append(songs)

# print(f"Your top 5 songs are {topFiveSongs}.")


playlistManager = []

def removeSong():
        print("Select a song to remove")
        print("Option 1")
        print(*playlistManager[0])
        print("Option 2")
        print(*playlistManager[1])
        print("Option 3")
        print(*playlistManager[2])
        print("Option 4")
        print(*playlistManager[3])
        print("Option 5")
        print(*playlistManager[4])

        removeinp = int(input("Which song would you like to remove. (state the option, e.g. '1') "))
        if removeinp == 1:
            playlistManager.remove(playlistManager[0])
        elif removeinp == 2:
            playlistManager.remove(playlistManager[1])
        elif removeinp == 3:
            playlistManager.remove(playlistManager[2])
        elif removeinp == 4:
            playlistManager.remove(playlistManager[3])
        elif removeinp == 5:
            playlistManager.remove(playlistManager[4])
        playlistManager.sort()
        print(f"Your new playlist is:",*playlistManager, "with 5 songs in the playlist.")

def addSong():
    song = input("Input song here to add to the playlist: ")
    playlistManager.append(song)

print("Enter 5 songs to add to the playlist: ")
for i in range(5):
    songs = input()
    playlistManager.append(songs)


playlistManager.sort()
print("Your top 5 songs are:",*playlistManager, "with 5 songs in the playlist")

add = input("Would you like to add a song? Y/N ").lower()

if add == "y":
    addSong()
else:
    print("Okay, closing program.")


remove = input("Would you like to remove a song? Y/N ").lower()

if remove == "y":
    removeSong()
else:
    print("Okay, closing program.")

print("Your playlist is now", *playlistManager)