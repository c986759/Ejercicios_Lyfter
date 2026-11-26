# We create the function to find uppercase and lowercase letters.
def find_uppercase_lowercase_letters(my_string):
    total_uppercase = 0
    total_lowercase = 0

    # We iterate through the sentence to find uppercase and lowercase letters.
    for char in my_string:
        if char.isupper():
            total_uppercase += 1
        elif char.islower():
            total_lowercase += 1

    print(f"There’s {total_uppercase} upper cases and {total_lowercase} lower cases ")


# main_block
def main():
    # We declare the text variable and call the function.
    my_string = "I love Nación Sushi"
    find_uppercase_lowercase_letters(my_string)


main()
