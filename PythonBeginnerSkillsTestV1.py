# Test name: Python Skills Test for Beginners

# Test instructions:
# This test consists of 5 questions. 
# For each question, you will be given a task to perform using Python code. 
# You should write a function that completes the task as described, and then return the result. 
# You should not use any external libraries or modules to complete the tasks. 
# You should not define any global variables. 
# You may define additional helper functions if necessary.

# Test questions:

# Question 1:
# Write a function that takes an integer as an argument and returns the absolute value of the integer.
# Example: 
# input: -5
# output: 5
def absolute_value(n):
    # your code here
    def get_absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

# Testing the function
input_num = -5
absolute_value = get_absolute_value(input_num)
print("Absolute value:", absolute_value)


# Question 2:
# Write a function that takes a string as an argument and returns the string with the first and last characters removed.
# Example:
# input: "hello"
# output: "ell"
def remove_first_last(string):
    # your code here
def remove_first_last_characters(input_string):
    if len(input_string) <= 2:
        return ""
    else:
        return input_string[1:-1]

# Testing the function
input_string = "Hello, World!"
modified_string = remove_first_last_characters(input_string)
print("Modified string:", modified_string)

# Question 3:
# Write a function that takes a list of integers as an argument and returns the sum of all odd numbers in the list.
# Example:
# input: [1, 2, 3, 4]
# output: 4
def sum_odds(numbers):
    # your code here
    def sum_odd_numbers(numbers):
    odd_sum = 0
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

# Testing the function
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_odds = sum_odd_numbers(input_numbers)
print("Sum of odd numbers:", sum_of_odds)


# Question 4:
# Write a function that takes a list of strings as an argument and returns a new list with all strings that have length 4 or less.
# Example:
# input: ["cat", "dog", "bird", "elephant"]
# output: ["cat", "dog"]
def filter_short_strings(strings):
    # your code here
def filter_short_strings(strings):
    filtered_list = []
    for string in strings:
        if len(string) <= 4:
            filtered_list.append(string)
    return filtered_list

# Testing the function
input_strings = ["apple", "cat", "hello", "dog", "python", "car"]
filtered_strings = filter_short_strings(input_strings)
print("Filtered strings:", filtered_strings)

# Question 5:
# Write a function that takes a dictionary as an argument and returns a new dictionary with all key-value pairs where the key is a string.
# Example:
# input: { "a": 1, "b": 2, "c": 3, 5: "d" }
# output: { "a": 1, "b": 2, "c": 3 }
def filter_string_keys(dictionary):
    # your code here
def filter_string_keys(dictionary):
    filtered_dict = {}
    for key, value in dictionary.items():
        if isinstance(key, str):
            filtered_dict[key] = value
    return filtered_dict

# Testing the function
input_dict = {1: 'one', '2': 'two', 3: 'three', '4': 'four', 'five': 5}
filtered_dict = filter_string_keys(input_dict)
print("Filtered dictionary:", filtered_dict)

















    
