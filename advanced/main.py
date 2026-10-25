def is_even(number):
    """ Return True if number is even and False if it is odd.

    :param number: the number to check if it is even.
    :return:
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text):
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text:
    :return:
    """
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius:
    :return:
    """
    return celsius * 1.8 + 32


def reverse_text(text):
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text:
    :return:
    """
    return text[::-1]


def larger_number(a, b):
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b


def average_two(a, b):
    """Calculate and return the average of two integers.

    :param a:
    :param b:
    :return:
    """
    return (a + b) / 2


def can_afford(balance, cost):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    return balance >= cost


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text:
    :param times:
    :return:
    """
    return text * times


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:
    :param word:
    :return:
    """
    return word in sentence


def calculate_tip(cost, percent):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:
    :param percent:
    :return:
    """
    return cost * (percent / 100)


def make_initials(first_name, last_name):
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name:
    :param last_name:
    :return:
    """
    return first_name[0].upper() + last_name[0].upper()


def percent_score(points, possible):
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points:
    :param possible:
    :return:
    """
    if possible < 1:
        return None
    return (points / possible) * 100


def is_between(number, minimum, maximum):
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number:
    :param minimum:
    :param maximum:
    :return:
    """
    return minimum <= number <= maximum


def all_different(a, b, c):
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a:
    :param b:
    :param c:
    :return:
    """
    return a != b and b != c and a != c


def average_three(a, b, c):
    """Calculate and return the average of three integers.

    :param a:
    :param b:
    :param c:
    :return:
    """
    return (a + b + c) / 3


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:
    :param cold_limit:
    :param hot_limit:
    :return:
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"

def temperature_in_safe_range(celsius, minimum_f, maximum_f):
    fahrenheit = (celsius * 9/5) + 32
    return minimum_f <= fahrenheit <= maximum_f

def can_afford_with_tip(balance, cost, tip_percent):
    total_cost = cost + (cost * (tip_percent / 100))
    return balance >= total_cost

def meets_average(score1, score2, score3, required_average):
    return (score1 + score2 + score3) / 3 >= required_average

def initials_match(first_name, last_name, expected_initials):
    actual = first_name[0].upper() + last_name[0].upper()
    return actual == expected_initials.upper()

if __name__ == "__main__":
    # testing temperature function
    print(describe_temperature(15, 20, 30)) # should be cold

    # testing average function
    print(average_three(10, 20, 30))  # should be 20

    # testing even function
    print(is_even(4))  # should be true

    # advanced function tests
    print("\n--- Advanced Multi-Value Tests ---")

    # temperature test
    print("Temperature Safe Range Tests:")
    print(temperature_in_safe_range(25, 68, 85))  # Test set 1 (Should be True)
    print(temperature_in_safe_range(10, 68, 85))  # Test set 2 (Should be False)

    # purchase test
    print("\nCan Afford With Tip Tests:")
    print(can_afford_with_tip(100.0, 50.0, 15.0))  # Test set 1 (Should be True)
    print(can_afford_with_tip(40.0, 50.0, 10.0))  # Test set 2 (Should be False)

    # average test
    print("\nMeets Average Tests:")
    print(meets_average(85, 90, 95, 85.0))  # Test set 1 (Should be True)
    print(meets_average(60, 70, 65, 75.0))  # Test set 2 (Should be False)

    # initials test
    print("\nInitials Match Tests:")
    print(initials_match("Ada", "Lovelace", "AL"))  # Test set 1 (Should be True)
    print(initials_match("john", "doe", "js"))  # Test set 2 (Should be False)

     # this validates and invalidates input without crashing
    print("\n--- Interactive User Input Test ---")
    try:
        # Prompting user for numeric values safely
        balance = float(input("Enter your account balance: "))
        cost = float(input("Enter the purchase cost: "))
        tip_pct = float(input("Enter tip percentage: "))

        can_buy = can_afford_with_tip(balance, cost, tip_pct)
        print(f"Can you afford this purchase? {can_buy}")

    except ValueError:
         print("Invalid entry! Please enter numbers only. (Crash prevented successfully!)")

