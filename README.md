# Function Gauntlet

## Basic Premise

Complete a series of **16 small function challenges**.

Your starter file contains 16 functions that have already been named and given their required parameters. Each function also contains a docstring explaining exactly what it should do.

Your job is to replace each `pass` with code that makes the function behave as described.

Each function should focus on **one clear task**. The functions use a mixture of strings, integers, floats, and Booleans as parameters and return values.

## Basic File Structure

```text
basic/
└── main.py
```

Your provided `main.py` will be filled with function stubs that have a descriptive docstring. For each function, your job will be:

* Add type hints for each parameter.
* Describe the parameter in the docstring.
* Add a return type hint.
* Describe the return value in the docstring.
* Program the function so that it works as described.

> ***Remember**: Each function in this assignment will work as an input - output machine! Your job is just to program the input - output machine to work as intended!*

## Basic Requirements

* [ ] Complete all **16 provided function stubs**.
* [ ] Do not change the provided function names or parameters.
* [ ] Each function must use the values received through its parameters rather than relying on fixed values written inside the function.
* [ ] Each function must return the datatype and result described in its docstring.
* [ ] Keep each function focused only on the task described in its docstring.
* [ ] Add function calls underneath the provided functions to test that they work with different values.

> Fully completing the Basic Requirements earns **16/20 marks, or 80%**.

## Basic Assessment — 16 Marks

| Function | Criteria | Marks |
|---|---|---:|
| `is_even()` | Correctly returns whether a number is even. | 1 |
| `count_vowels()` | Correctly counts vowels in a string. | 1 |
| `celsius_to_fahrenheit()` | Correctly converts Celsius to Fahrenheit. | 1 |
| `reverse_text()` | Correctly returns the text in reverse order. | 1 |
| `larger_number()` | Correctly returns the larger integer. | 1 |
| `average_two()` | Correctly calculates the average of two integers. | 1 |
| `can_afford()` | Correctly returns whether the balance can cover the cost. | 1 |
| `repeat_text()` | Correctly repeats the supplied text. | 1 |
| `contains_word()` | Correctly determines whether the word appears in the sentence. | 1 |
| `calculate_tip()` | Correctly calculates the requested tip amount. | 1 |
| `make_initials()` | Correctly creates uppercase initials. | 1 |
| `percent_score()` | Correctly calculates the percentage earned. | 1 |
| `is_between()` | Correctly determines whether the number is within the inclusive range. | 1 |
| `all_different()` | Correctly determines whether all three strings are different. | 1 |
| `average_three()` | Correctly calculates the average of three integers. | 1 |
| `describe_temperature()` | Correctly returns `cold`, `comfortable`, or `hot`. | 1 |
|  | **Total** | **16** |

<details><summary> </summary>


</details>

## Advanced Premise

Add **four new functions** to your completed Function Gauntlet.

Unlike the Basic functions, these functions are **not provided as stubs**. You will need to create each function yourself based on its description.

Each challenge requires several steps rather than one simple calculation or comparison.

## Advanced File Structure

```text
advanced/
└── main.py
```

Begin by copying your completed Basic `main.py` into the Advanced folder.

## Advanced Requirements

* [ ] Create `temperature_in_safe_range(celsius, minimum_f, maximum_f)`. Convert the Celsius temperature to Fahrenheit and return `True` if the converted temperature is between the supplied Fahrenheit limits, including the limits. Otherwise return `False`.
* [ ] Create `can_afford_with_tip(balance, cost, tip_percent)`. Calculate the tip, add it to the original cost, and return `True` if the supplied balance can pay the complete total. Otherwise return `False`.
* [ ] Create `meets_average(score1, score2, score3, required_average)`. Calculate the average of the three scores and return `True` if it is greater than or equal to the required average. Otherwise return `False`.
* [ ] Create `initials_match(first_name, last_name, expected_initials)`. Determine the initials of the supplied first and last names and return `True` if they match `expected_initials`. Capitalization should not affect the result.
* [ ] Add test calls for all four Advanced functions using more than one set of values.
* [ ] When testing the Advanced functions with user-entered values, validate numeric input and handle incorrect numeric entries without allowing the program to crash.

## Advanced Assessment — 4 Marks

| Assessment Item | Criteria | Marks |
|---|---|---:|
| Temperature Challenge | Correctly converts the temperature and determines whether it falls inside the supplied safe range. | 1 |
| Purchase Challenge | Correctly includes the calculated tip when determining whether the purchase can be afforded. | 1 |
| Average Challenge | Correctly calculates the three-score average and compares it with the required average. | 1 |
| Initials Challenge | Correctly creates and compares initials without capitalization affecting the result. | 1 |
|  | **Total** | **4** |
