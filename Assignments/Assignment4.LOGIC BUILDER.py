'''Assignment (17/02/2026)
Assignment Name : Logic Builder
Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions.'''
# Function to print numbers with Fizz/Buzz logic
def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif num % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(num)

    return fizz_count, buzz_count, fizzbuzz_count


# Calling the function
fizz, buzz, fizzbuzz = fizz_buzz()

# Display counts
print("\n--- Count Summary ---")
print("Fizz count:", fizz)
print("Buzz count:", buzz)
print("FizzBuzz count:", fizzbuzz)