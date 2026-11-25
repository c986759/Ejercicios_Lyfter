# define function #1
def create_variable():
    test_variable = "Test"
    return test_variable


# main_block
def main():

    # access variable
    # access_variable = create_variable()
    print(test_variable)
    # The program cannot access the variable: test_variable is not defined
    # NameError: name 'test_variable' is not defined. Did you mean: 'create_variable'?


main()
