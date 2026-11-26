# function to store the names in the list in a random order
def read_file_by_lines(path):
    # global songs_list
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for number, line in enumerate(lines):
            # We use strip() to remove line breaks and clean up spaces.
            # songs_list.append(line.strip())
            print(f"Line {number+1}: {line.strip()}")
    # return songs_list


# function to store the names in the list in a random order
def store_song_titles(path):
    # We create the global lists.
    songs_list = []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for number, line in enumerate(lines):
            # We use strip() to remove line breaks and clean up spaces.
            songs_list.append(line.strip())

    return songs_list


def sort_list(song_list):
    n = len(song_list)
    # We iterate through the list, comparing complete words
    for i in range(n):
        for j in range(0, n - i - 1):
            # We perform comparisons in lowercase to avoid errors related to uppercase letters.
            if song_list[j].lower() > song_list[j + 1].lower():
                # We swapped the positions of the words.
                song_list[j], song_list[j + 1] = (
                    song_list[j + 1],
                    song_list[j],
                )

    return song_list


def write_new_file(path, songs):
    with open(path, "w", encoding="utf-8") as file:
        for i in range(len(songs)):
            if i == 0:
                file.write(songs[i])
            else:
                file.write("\n" + songs[i])


# Main block
def main():
    # We create the variable to store the unordered list.
    unsorted_titles = []
    # We create the list where the titles will be arranged.
    new_song_list = []
    # print the original txt file
    print(
        "This is the songs_titles.txt file containing the list of songs in no particular order."
    )

    # We read the file and save it to the first list.
    read_file_by_lines("songs_titles.txt")
    # We store the titles in a temporary list, to be sorted later.
    unsorted_titles = store_song_titles("songs_titles.txt")
    # We arrange the names in the list alphabetically.
    new_song_list = sort_list(unsorted_titles)
    # We create the new text file and insert the ordered list.
    write_new_file("organized_songs_titles.txt", new_song_list)
    # print the new, sorted .txt file
    print(
        "This is the file organized_songs_titles.txt, containing the list of songs in order."
    )
    read_file_by_lines("organized_songs_titles.txt")


main()
