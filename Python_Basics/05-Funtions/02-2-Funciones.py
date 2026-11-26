# We define the variable in the global scope.
my_global_variable = 10


def change_without_global():
    # We try to change the value.
    # Python interprets this as the creation of a NEW local variable.
    # with the same name, instead of modifying the global one.
    my_global_variable = 99
    print(f"Inside the function (without global): {my_global_variable}")


def change_with_global():
    # Le indicamos explícitamente a Python que use la variable del ámbito global
    global my_global_variable
    my_global_variable = 99
    print(f"Inside the function (using global): {my_global_variable}")


# We print before calling the function.
print(f"Before the function (non-global) {my_global_variable}")

# We call the function
change_without_global()

# We print after calling the function.
print(f"After the function (non-global): {my_global_variable}")

# We print before calling the function.
print(f"Before the function (with global) {my_global_variable}")

# We call the function with global
change_with_global()

# We print after calling the Global function.
print(f"After the function (with global) {my_global_variable}")

"""
OBSERVATION (Case without 'global'):
1. 'Before' shows 10 (the original global value).
2. 'Inside' shows 99 because a local variable was created that "hides" the global one.
3. 'After' shows 10 again. The global variable NEVER changed.
"""
"""
OBSERVATION (Case involving 'global'):
1. 'Before' shows 10.
2. 'Inside' shows 99 because we are modifying the global variable directly.
3. 'After' now shows 99. The global variable WAS indeed permanently modified
"""
