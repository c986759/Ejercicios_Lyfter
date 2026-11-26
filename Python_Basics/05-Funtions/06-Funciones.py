def sort_string(input_string):
    # Split the string manually character by character
    # We create the list where we store each word found.
    word_list = []
    # variable to store each word found
    current_word = ""

    # we iterate through the string letter by letter
    for char in input_string:
        if char == "-":
            # If we find a hyphen, the current word is complete
            word_list.append(current_word)
            current_word = ""  # Reset for the next word
        else:
            # Accumulate characters to build the word
            current_word += char

    # Add the last word after the final loop iteration
    if current_word != "":
        word_list.append(current_word)

    # Sort the list manually checking the first letter
    # We create the new list where items will be stored in order.
    sorted_list = []

    # Loop until we have processed all words from the original list
    while len(word_list) > 0:
        # We save the first word; it will serve as a starting point for comparison with the others.
        smallest_word = word_list[0]
        # This variable points to the index of that word; it will be used to remove that item
        # from the list once the smallest word has been identified in each complete iteration.
        smallest_index = 0

        # Iterate through the rest of the list to find the actual smallest word
        for index in range(1, len(word_list)):
            # Compare the first letter of each word
            if word_list[index][0] < smallest_word[0]:
                # if it is smaller, we store its value for the next comparison
                smallest_word = word_list[index]
                # We note its index in order to remove it from the original list.
                smallest_index = index

        # Add the smallest word found to our new sorted list
        sorted_list.append(smallest_word)

        # Remove it from the original list, so as not to compare it again
        word_list.pop(smallest_index)

    # Join the words into a single string
    result_string = ""

    for index in range(len(sorted_list)):
        result_string += sorted_list[index]
        # Append a hyphen after every word except the last one
        if index < len(sorted_list) - 1:
            result_string += "-"

    # we return the list sorted alphabetically, with hyphens between words
    return result_string


# Main block
def main():
    sample_string = "python-variable-funcion-computadora-monitor"

    # Call the function and store the result
    result = sort_string(sample_string)

    # Print the output
    print(f"Original: {sample_string}")
    print(f"Sorted:   {result}")


main()
