import pytest

from advanced.main import (
    is_even,
    count_vowels,
    celsius_to_fahrenheit,
    reverse_text,
    larger_number,
    average_two,
    can_afford,
    repeat_text,
    contains_word,
    calculate_tip,
    make_initials,
    percent_score,
    is_between,
    all_different,
    average_three,
    describe_temperature,
)


# --------------------------------------------------
# is_even()
# --------------------------------------------------

@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-7, False),
    ],
)
def test_is_even(number, expected):
    assert is_even(number) is expected


# --------------------------------------------------
# count_vowels()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
        ("Programming is fun", 5),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


# --------------------------------------------------
# celsius_to_fahrenheit()
# --------------------------------------------------

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (20, 68.0),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


# --------------------------------------------------
# reverse_text()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("robot", "tobor"),
        ("hello world", "dlrow olleh"),
        ("A", "A"),
        ("12345", "54321"),
        ("", ""),
    ],
)
def test_reverse_text(text, expected):
    assert reverse_text(text) == expected


# --------------------------------------------------
# larger_number()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 5, 10),
        (5, 10, 10),
        (-5, -10, -5),
        (7, 7, 7),
        (0, -1, 0),
    ],
)
def test_larger_number(first, second, expected):
    assert larger_number(first, second) == expected


# --------------------------------------------------
# average_two()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 20, 15.0),
        (0, 0, 0.0),
        (-10, 10, 0.0),
        (5, 6, 5.5),
        (100, 50, 75.0),
    ],
)
def test_average_two(first, second, expected):
    assert average_two(first, second) == pytest.approx(expected)


# --------------------------------------------------
# can_afford()
# --------------------------------------------------

@pytest.mark.parametrize(
    "balance, cost, expected",
    [
        (100.0, 50.0, True),
        (50.0, 50.0, True),
        (49.99, 50.0, False),
        (0.0, 0.0, True),
        (10.0, 10.01, False),
    ],
)
def test_can_afford(balance, cost, expected):
    assert can_afford(balance, cost) is expected


# --------------------------------------------------
# repeat_text()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, times, expected",
    [
        ("Go!", 3, "Go!Go!Go!"),
        ("A", 1, "A"),
        ("Hi", 0, ""),
        ("", 5, ""),
        ("ab", 4, "abababab"),
    ],
)
def test_repeat_text(text, times, expected):
    assert repeat_text(text, times) == expected


# --------------------------------------------------
# contains_word()
# --------------------------------------------------

@pytest.mark.parametrize(
    "sentence, word, expected",
    [
        ("The robot is ready", "robot", True),
        ("hello world", "world", True),
        ("hello world", "mars", False),
        ("banana", "nan", True),
        ("Python", "python", False),
    ],
)
def test_contains_word(sentence, word, expected):
    assert contains_word(sentence, word) is expected


# --------------------------------------------------
# calculate_tip()
# --------------------------------------------------

@pytest.mark.parametrize(
    "cost, percent, expected",
    [
        (20.0, 15, 3.0),
        (100.0, 20, 20.0),
        (50.0, 10, 5.0),
        (0.0, 18, 0.0),
        (25.5, 20, 5.1),
    ],
)
def test_calculate_tip(cost, percent, expected):
    assert calculate_tip(cost, percent) == pytest.approx(expected)


# --------------------------------------------------
# make_initials()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first_name, last_name, expected",
    [
        ("Ada", "Lovelace", "AL"),
        ("alan", "turing", "AT"),
        ("Grace", "Hopper", "GH"),
        ("john", "SMITH", "JS"),
        ("x", "y", "XY"),
    ],
)
def test_make_initials(first_name, last_name, expected):
    assert make_initials(first_name, last_name) == expected


# --------------------------------------------------
# percent_score()
# --------------------------------------------------

@pytest.mark.parametrize(
    "points, possible, expected",
    [
        (18, 20, 90.0),
        (50, 100, 50.0),
        (1, 4, 25.0),
        (0, 10, 0.0),
        (7, 8, 87.5),
    ],
)
def test_percent_score(points, possible, expected):
    assert percent_score(points, possible) == pytest.approx(expected)


# --------------------------------------------------
# is_between()
# --------------------------------------------------

@pytest.mark.parametrize(
    "number, minimum, maximum, expected",
    [
        (5, 1, 10, True),
        (1, 1, 10, True),
        (10, 1, 10, True),
        (0, 1, 10, False),
        (15, 1, 10, False),
    ],
)
def test_is_between(number, minimum, maximum, expected):
    assert is_between(number, minimum, maximum) is expected


# --------------------------------------------------
# all_different()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, third, expected",
    [
        ("red", "green", "blue", True),
        ("red", "red", "blue", False),
        ("red", "green", "red", False),
        ("same", "same", "same", False),
        ("A", "a", "B", True),
    ],
)
def test_all_different(first, second, third, expected):
    assert all_different(first, second, third) is expected


# --------------------------------------------------
# average_three()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, third, expected",
    [
        (3, 6, 9, 6.0),
        (1, 2, 2, 5 / 3),
        (-10, 0, 10, 0.0),
        (0, 0, 0, 0.0),
        (10, 20, 25, 55 / 3),
    ],
)
def test_average_three(first, second, third, expected):
    assert average_three(first, second, third) == pytest.approx(expected)


# --------------------------------------------------
# describe_temperature()
# --------------------------------------------------

@pytest.mark.parametrize(
    "temperature, cold_limit, hot_limit, expected",
    [
        (5.0, 10.0, 25.0, "cold"),
        (30.0, 10.0, 25.0, "hot"),
        (20.0, 10.0, 25.0, "comfortable"),
        (10.0, 10.0, 25.0, "comfortable"),
        (25.0, 10.0, 25.0, "comfortable"),
    ],
)
def test_describe_temperature(
    temperature,
    cold_limit,
    hot_limit,
    expected,
):
    assert describe_temperature(
        temperature,
        cold_limit,
        hot_limit,
    ) == expected