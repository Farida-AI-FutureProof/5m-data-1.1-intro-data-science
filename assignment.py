# Question 1
def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, 
    FizzBuzz if divisible by both 3 and 5, otherwise returns the number."""
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


# Question 2
def sum_of_squares(numbers):
    """Takes a list of numbers and returns the sum of the squares of all numbers."""
    total = 0
    for num in numbers:
        total += num ** 2
    return total


# Question 3
def count_repeats(numbers):
    """Takes a list (or string) and returns how many distinct items are repeated."""
    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1
    repeats = 0
    for v in counts.values():
        if v > 1:
            repeats += 1
    return repeats


# Question 4
def count_vowels(string):
    """Returns the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    return count


# --- Run doctests (this must be at the very bottom) ---
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
