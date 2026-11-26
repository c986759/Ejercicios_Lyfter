# We create the function that iterates through the list and stores the sum of the numbers in a variable.
def sum_items_of_list(number_list):
    total = 0
    for index, number in enumerate(number_list):
        total = total + number

    return total


# main_block
def main():
    number_list = [10, 20, 30, 40]
    # We call the function and display the result.
    print(
        f"The numbers on the list are as follows:: {number_list} and the sum of them is: {sum_items_of_list(number_list)}"
    )


main()
