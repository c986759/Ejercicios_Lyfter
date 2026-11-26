def calculator_menu(current_number, options_menu):
    while True:
        print("\nWelcome to the Calculator")
        print(
            f"Enter the option you wish to apply using the calculator with the actual number: {current_number}"
        )
        for i, item_menu in enumerate(options_menu):
            print(f"{i+1}. {item_menu}")

        try:
            option_selected = int(
                input(
                    f"Enter the option you wish to apply using the calculator (1-{len(options_menu)}): "
                )
            )

            # Explicitly validate the range to prevent 0 or negative numbers from indexing the list
            if 1 <= option_selected <= len(options_menu):
                print(f"The selected option was: {options_menu[option_selected - 1]}")
                return option_selected
            else:
                print(
                    f"Error: Please enter only an integer between 1 and {len(options_menu)}."
                )
                print("-" * 30)  # dividing line
                input("Press Enter to continue...")

        except ValueError:
            print(
                f"Error: Please enter only an integer between 1 and {len(options_menu)}."
            )
            print("-" * 30)  # dividing line
            input("Press Enter to continue...")


def ask_for_second_number(current_number):
    while True:
        print(f"\nThe current number is: {current_number}")
        try:
            # Using float allows both integers and decimals without crashing
            second_number = float(input("Please enter the second number: "))
            return second_number
        except ValueError:
            print("Error: You must enter a valid number.")
            print("-" * 30)  # dividing line
            input("Press Enter to continue...")


def calculator_operation(option, number_1, number_2):
    # We perform the operation using the local variables passed in as parameters.
    match option:
        case 1:
            return number_1 + number_2
        case 2:
            return number_1 - number_2
        case 3:
            return number_1 * number_2
        case 4:
            try:
                return number_1 / number_2
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
                return number_1  # If the division fails, we keep the original number intact.
        case _:
            return number_1


def main():
    # Local state variables living strictly inside main()
    current_number = 0
    options_menu_calculator = [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Clear result",
        "Exit",
    ]

    # The while True loop keeps the calculator running indefinitely.
    while True:
        # 1. We ask for the menu option first, passing current state as arguments.
        calculator_option_selected = calculator_menu(
            current_number, options_menu_calculator
        )

        # If the user chooses option 6 (Exit), we break the loop and close the program
        if calculator_option_selected == 6:
            print("Thank you for using the calculator. Goodbye!")
            break

        # If the user chooses option 5 (Clear result), we reset current_number to 0
        if calculator_option_selected == 5:
            current_number = 0
            print("\nResult has been cleared.")
            print("-" * 40)
            print(f"The new current number is now: {current_number}")
            print("-" * 40)
            input("Press Enter to continue...")
            continue

        # 2. We ask for the second number
        second_number = ask_for_second_number(current_number)

        # This variable was added because the final result message was incorrect.
        previous_number = current_number

        # 3. We calculate the new result and assign it directly to current_number
        current_number = calculator_operation(
            calculator_option_selected, current_number, second_number
        )

        # We display the result of the selected operation.
        print(
            f"\nThe result of the operation: {previous_number} {options_menu_calculator[calculator_option_selected-1]} {second_number} is: {current_number}"
        )
        print("-" * 40)  # A dividing line to separate operations
        print(f"The new current number is now: {current_number}")
        print("-" * 40)  # A dividing line to separate operations
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
