import json


# Prompt the user for a non-empty string.
def get_non_empty_text(message):
    while True:
        try:
            text = input(message).strip()
            if text == "":
                raise ValueError("Input cannot be empty.")
            return text
        except ValueError as error:
            print("Invalid input:", error)


# Prompt the user for an optional string (empty input becomes None).
def define_optional_text(message):
    text = input(message).strip()
    if text == "":
        return None
    return text


# Prompt the user for an integer within a given range.
def define_int_in_range(message, min_value, max_value):
    while True:
        try:
            raw_value = input(message).strip()
            if raw_value == "":
                raise ValueError("Input cannot be empty.")
            number = int(raw_value)
            if number < 0:
                raise ValueError("Number cannot be negative.")
            if number < min_value or number > max_value:
                raise ValueError(f"Number must be between {min_value} and {max_value}.")
            return number
        except ValueError as error:
            print("Invalid input:", error)


# Prompt the user for a positive float number.
def define_positive_float(message, min_value, max_value):
    while True:
        try:
            raw_value = input(message).strip()
            if raw_value == "":
                raise ValueError("Input cannot be empty.")
            number = float(raw_value)
            if number < 0:
                raise ValueError("Number cannot be negative.")
            if number < min_value or number > max_value:
                raise ValueError(f"Number must be between {min_value} and {max_value}.")
            return number
        except ValueError as error:
            print("Invalid input:", error)


# Prompt the user for a boolean answer (yes/no).
def define_yes_no(message):
    while True:
        try:
            answer = input(message).strip().lower()
            if answer == "":
                raise ValueError("Input cannot be empty.")
            if answer == "yes" or answer == "y" or answer == "true":
                return True
            if answer == "no" or answer == "n" or answer == "false":
                return False
            raise ValueError("Answer must be yes/no or true/false.")
        except ValueError as error:
            print("Invalid input:", error)


# Prompt the user for a list of up to 4 skills manually.
def define_skills():
    skills = []
    count = define_int_in_range("How many skills (1 to 4): ", 1, 4)
    index = 0
    while index < count:
        skill_name = get_non_empty_text(f"Enter skill #{index + 1}: ")
        skills.append(skill_name)
        index = index + 1
    return skills


# Prompt the user for all stats manually.
def define_stats():
    stats = {}
    stats["hp"] = define_int_in_range("Enter HP (1 to 255): ", 1, 255)
    stats["attack"] = define_int_in_range("Enter Attack (1 to 255): ", 1, 255)
    stats["defense"] = define_int_in_range("Enter Defense (1 to 255): ", 1, 255)
    stats["sp_attack"] = define_int_in_range("Enter Sp. Attack (1 to 255): ", 1, 255)
    stats["sp_defense"] = define_int_in_range("Enter Sp. Defense (1 to 255): ", 1, 255)
    stats["speed"] = define_int_in_range("Enter Speed (1 to 255): ", 1, 255)
    return stats


# Read existing Pokemon list from a JSON file.
def load_pokemon_list(file_path):
    try:
        file_handle = open(file_path, "r", encoding="utf-8")
        data = json.load(file_handle)
        file_handle.close()
        if type(data) is not list:
            raise ValueError("JSON root must be a list.")
        return data
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("JSON file is corrupted. Aborting to prevent data loss.")
        return None
    except ValueError as error:
        print("Invalid JSON structure:", error)
        print("Aborting to prevent data loss.")
        return None


# Collect a single new Pokemon dictionary from user input.
def create_pokemon_record():
    pokemon = {}
    print("Enter the details for the new Pokémon")
    print(" -------------------------------")
    pokemon["name"] = get_non_empty_text("Enter Pokemon name: ")
    pokemon["type"] = get_non_empty_text("Enter Pokemon type: ")
    pokemon["level"] = define_int_in_range("Enter level (1 to 100): ", 1, 100)
    pokemon["weight_kg"] = define_positive_float(
        "Enter weight in kg (0.1 to 1000.0): ", 0.1, 1000.0
    )
    pokemon["is_shiny"] = define_yes_no("Is it shiny? (yes/no): ")
    pokemon["held_item"] = define_optional_text(
        "Enter held item (leave blank for none): "
    )
    pokemon["skills"] = define_skills()
    pokemon["stats"] = define_stats()
    return pokemon


# Save the updated Pokemon list to a JSON file.
def save_pokemon_list(file_path, pokemon_list):
    try:
        file_handle = open(file_path, "w", encoding="utf-8")
        json.dump(pokemon_list, file_handle, indent=2)
        file_handle.close()
        print("Pokemon saved successfully to", file_path)
    except OSError as error:
        print("Error writing to file:", error)


# Coordinate loading, creating, and saving a Pokemon.
def run_pokemon_manager(file_path):
    pokemon_list = load_pokemon_list(file_path)
    if pokemon_list is None:
        return

    print("These are the current Pokémon data in the pokemon.json file.")
    print(pokemon_list)
    new_pokemon = create_pokemon_record()
    pokemon_list.append(new_pokemon)
    save_pokemon_list(file_path, pokemon_list)
    pokemon_list = load_pokemon_list(file_path)
    print("These are the new Pokémon data in the pokemon.json file.")
    print(pokemon_list)


# Main block
def main():
    run_pokemon_manager("pokemon.json")


main()
