# We created the function that iterates through the string in reverse.
def show_word_backwards(my_string):
    for index in range(len(my_string) - 1, -1, -1):
        print(my_string[index])


# main_block
def main():
    # We declare the text variable and call the function.
    my_string = "Parancutirimicuaro"
    show_word_backwards(my_string)


main()
