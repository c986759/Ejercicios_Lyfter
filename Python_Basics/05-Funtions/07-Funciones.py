import math

# This function determines whether the number is prime or not.
def is_prime_number(number):
    # Numbers less than or equal to 1 are not prime.
    if number <= 1:
        return False
    
    # 2 is the only even prime number
    if number == 2:
        return True
    
    # is greater than 2 and is an even number, it is not prime.
    if number % 2 == 0:
        return False
    
    # If the previous conditions are met, we test only with odd numbers up to the square root of the number.    
    square_root = int(math.isqrt(number))
    for i in range(3, square_root + 1, 2):
        if number % i == 0:
            return False  # If it finds a divisor, it breaks and returns False.
            
    return True  # If it completes the loop, it is prime.

# iterate through the entire list and use the other function to determine whether it is prime or not (true / false)
# We add the found prime numbers to the new list.
def find_prime_numbers(number_list):
    list_of_primes_found = []  
    
    for number in number_list:
        # We call the first function to check the current number
        if is_prime_number(number):
            list_of_primes_found.append(number)  # If it is True, we add it to the new list
            
    return list_of_primes_found  # We return the new final list containing all the primes.

# Main block
number_list = [2, 3, 10, 5, 7, 20, 13, 18, 19, 24, 29, 30]

# We store the result in this variable; we pass the complete list as a parameter to the function.
result = find_prime_numbers(number_list)

print(f"List of numbers to evaluate:{number_list}")
print(f"Prime numbers found: {result}")
