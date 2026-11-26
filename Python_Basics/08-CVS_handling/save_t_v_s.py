import csv


# function to determine the number of games, while excluding blanks, letters, and negative values
def get_valid_amount():
    while True:
        try:
            amount = int(input("How many video games do you want to register? "))
            if amount <= 0:
                raise ValueError("The number must be greater than 0.")
            return amount
        except ValueError as error:
            print(f"Error: Invalid input ({error}). Please enter a positive integer.")


# function to prevent empty data entry (blank fields)
def get_non_empty_text(prompt_message):
    while True:
        try:
            user_input = input(prompt_message).strip()
            if not user_input:
                raise ValueError("This field cannot be left blank.")
            return user_input
        except ValueError as error:
            print(f"Error: {error}")


# Function to validate the ESRB rating, preventing empty values and enforcing valid categories
def get_valid_rating():
    valid_ratings = ("E", "E10+", "T", "M", "AO", "RP")

    while True:
        try:
            raw_input = input(f"ESRB Rating {valid_ratings}: ").strip().upper()

            if not raw_input:
                raise ValueError("Rating cannot be left blank.")

            if raw_input not in valid_ratings:
                raise ValueError(
                    f"Invalid category. Choose one of: {', '.join(valid_ratings)}."
                )

            return raw_input
        except ValueError as error:
            print(f"Error: {error} Try again.")


# Function to prompt the user for data to be entered; the data is stored in a list.
def get_video_games():
    games_list = []
    amount = get_valid_amount()

    for i in range(amount):
        print(f"\n--- Video Game #{i + 1} ---")
        name = get_non_empty_text("Name: ")
        genre = get_non_empty_text("Genre: ")
        developer = get_non_empty_text("Developer: ")
        rating = get_valid_rating()

        game_data = {
            "nombre": name,
            "genero": genre,
            "desarrollador": developer,
            "clasificacion": rating,
        }
        games_list.append(game_data)

    return games_list


# function to save data to a TSV (tab-separated) file
def save_video_games(file_path, data):
    if not data:
        print("No data to save.")
        return

    try:
        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
            writer.writeheader()
            writer.writerows(data)
        print(f"\nData successfully saved to '{file_path}'.")
    except PermissionError:
        print(
            f"\nError: Permission denied. Close '{file_path}' if it is open in Excel."
        )
    except OSError as error:
        print(f"\nError: Could not write to file. Details: {error}")


# function to read data from a TSV (tab-separated) file
def read_video_games(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter="\t")
            print("\n=== Registered Video Games ===")
            for game in reader:
                print(
                    f"Name: {game['nombre']} | "
                    f"Genre: {game['genero']} | "
                    f"Developer: {game['desarrollador']} | "
                    f"ESRB Rating: {game['clasificacion']}"
                )
    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
    except KeyError as error:
        print(f"\nError: Missing expected column in file: {error}")
    except OSError as error:
        print(f"\nError: Could not read file. Details: {error}")


def main():
    file_name = "video_games.tsv"
    try:
        video_games = get_video_games()
        save_video_games(file_name, video_games)
        read_video_games(file_name)
    except KeyboardInterrupt:
        print("\n\nProgram cancelled by the user.")


if __name__ == "__main__":
    main()
