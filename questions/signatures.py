"""
Function signatures for all 57 questions.
Key: (day_number, question_order)
Value: dict with:
  - signature: the def line shown to student (read-only)
  - wrapper: code that calls the function with parsed inputs and returns result
             The wrapper receives variables from parsed input and calls the function.
             It must return a single value that gets compared to expected output.
"""

SIGNATURES = {
    # Day 1
    (1, 1): {
        "signature": "def sum_of_two(a, b):",
        "params": ["int", "int"],
        "wrapper": """
def _run(input_str):
    a, b = map(int, input_str.strip().split())
    result = sum_of_two(a, b)
    return str(result)
"""
    },
    (1, 2): {
        "signature": "def area_of_circle(r):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    import math
    r = int(input_str.strip())
    result = area_of_circle(r)
    return str(round(result, 2))
"""
    },
    # Day 2
    (2, 1): {
        "signature": "def largest_of_three(a, b, c):",
        "params": ["int", "int", "int"],
        "wrapper": """
def _run(input_str):
    a, b, c = map(int, input_str.strip().split())
    result = largest_of_three(a, b, c)
    return str(result)
"""
    },
    (2, 2): {
        "signature": "def is_leap_year(year):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    year = int(input_str.strip())
    result = is_leap_year(year)
    return str(result)
"""
    },
    (2, 3): {
        "signature": "def check_even_odd(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = check_even_odd(n)
    return str(result)
"""
    },
    # Day 3
    (3, 1): {
        "signature": "def multiplication_table(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = multiplication_table(n)
    if isinstance(result, list):
        return '\\n'.join(str(x) for x in result)
    return str(result).strip()
"""
    },
    (3, 2): {
        "signature": "def sum_to_n(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = sum_to_n(n)
    return str(result)
"""
    },
    (3, 3): {
        "signature": "def factorial(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = factorial(n)
    return str(result)
"""
    },
    # Day 4
    (4, 1): {
        "signature": "def square_pattern(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = square_pattern(n)
    if isinstance(result, list):
        return '\\n'.join(str(x) for x in result)
    return str(result).strip()
"""
    },
    (4, 2): {
        "signature": "def pyramid_pattern(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = pyramid_pattern(n)
    if isinstance(result, list):
        return '\\n'.join(str(x) for x in result)
    return str(result).strip()
"""
    },
    # Day 5
    (5, 1): {
        "signature": "def check_prime(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = check_prime(n)
    return str(result)
"""
    },
    (5, 2): {
        "signature": "def gcd(a, b):",
        "params": ["int", "int"],
        "wrapper": """
def _run(input_str):
    a, b = map(int, input_str.strip().split())
    result = gcd(a, b)
    return str(result)
"""
    },
    (5, 3): {
        "signature": "def power(base, exp):",
        "params": ["int", "int"],
        "wrapper": """
def _run(input_str):
    base, exp = map(int, input_str.strip().split())
    result = power(base, exp)
    return str(result)
"""
    },
    # Day 6
    (6, 1): {
        "signature": "def reverse_string(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = reverse_string(s)
    return str(result)
"""
    },
    (6, 2): {
        "signature": "def is_palindrome(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = is_palindrome(s)
    return str(result)
"""
    },
    (6, 3): {
        "signature": "def count_vowels(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = count_vowels(s)
    return str(result)
"""
    },
    # Day 7
    (7, 1): {
        "signature": "def find_largest(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = find_largest(arr)
    return str(result)
"""
    },
    (7, 2): {
        "signature": "def find_second_largest(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = find_second_largest(arr)
    return str(result)
"""
    },
    (7, 3): {
        "signature": "def count_frequency(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = count_frequency(arr)
    if isinstance(result, dict):
        return '\\n'.join(f"{k}: {v}" for k, v in sorted(result.items()))
    return str(result).strip()
"""
    },
    # Day 9
    (9, 1): {
        "signature": "def linear_search(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = linear_search(arr, target)
    return str(result)
"""
    },
    (9, 2): {
        "signature": "def find_maximum(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = find_maximum(arr)
    return str(result)
"""
    },
    # Day 10
    (10, 1): {
        "signature": "def reverse_array(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = reverse_array(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (10, 2): {
        "signature": "def rotate_array(arr, k):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    result = rotate_array(arr, k)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 11
    (11, 1): {
        "signature": "def move_zeroes(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = move_zeroes(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (11, 2): {
        "signature": "def remove_duplicates(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = remove_duplicates(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 12
    (12, 1): {
        "signature": "def bubble_sort(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = bubble_sort(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (12, 2): {
        "signature": "def selection_sort(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = selection_sort(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 13
    (13, 1): {
        "signature": "def insertion_sort(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = insertion_sort(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (13, 2): {
        "signature": "def is_sorted(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = is_sorted(arr)
    return str(result)
"""
    },
    # Day 15
    (15, 1): {
        "signature": "def char_frequency(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = char_frequency(s)
    if isinstance(result, dict):
        return '\\n'.join(f"{k}: {v}" for k, v in result.items())
    return str(result).strip()
"""
    },
    (15, 2): {
        "signature": "def first_non_repeating(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = first_non_repeating(s)
    return str(result)
"""
    },
    # Day 16
    (16, 1): {
        "signature": "def two_sum(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = two_sum(arr, target)
    if isinstance(result, (list, tuple)):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (16, 2): {
        "signature": "def has_duplicates(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = has_duplicates(arr)
    return str(result)
"""
    },
    # Day 17
    (17, 1): {
        "signature": "def binary_search_iterative(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = binary_search_iterative(arr, target)
    return str(result)
"""
    },
    (17, 2): {
        "signature": "def binary_search_recursive(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = binary_search_recursive(arr, target)
    return str(result)
"""
    },
    # Day 18
    (18, 1): {
        "signature": "def first_last_occurrence(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = first_last_occurrence(arr, target)
    if isinstance(result, (list, tuple)):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (18, 2): {
        "signature": "def floor_ceil(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = floor_ceil(arr, target)
    if isinstance(result, (list, tuple)):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 19
    (19, 1): {
        "signature": "def two_sum_sorted(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = two_sum_sorted(arr, target)
    if isinstance(result, (list, tuple)):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    (19, 2): {
        "signature": "def pair_with_sum(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = pair_with_sum(arr, target)
    return str(result)
"""
    },
    # Day 20
    (20, 1): {
        "signature": "def max_sum_subarray(arr, k):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    result = max_sum_subarray(arr, k)
    return str(result)
"""
    },
    (20, 2): {
        "signature": "def longest_subarray_sum_k(arr, k):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    result = longest_subarray_sum_k(arr, k)
    return str(result)
"""
    },
    # Day 22
    (22, 1): {
        "signature": "def stack_operations(operations):",
        "params": ["list[str]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    q = int(lines[0])
    operations = lines[1:q+1]
    result = stack_operations(operations)
    if isinstance(result, list):
        return '\\n'.join(str(x) for x in result)
    return str(result).strip()
"""
    },
    (22, 2): {
        "signature": "def is_valid_brackets(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = is_valid_brackets(s)
    return str(result)
"""
    },
    # Day 23
    (23, 1): {
        "signature": "def next_greater_element(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = next_greater_element(arr)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 24
    (24, 1): {
        "signature": "def queue_operations(operations):",
        "params": ["list[str]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    q = int(lines[0])
    operations = lines[1:q+1]
    result = queue_operations(operations)
    if isinstance(result, list):
        return '\\n'.join(str(x) for x in result)
    return str(result).strip()
"""
    },
    # Day 25
    (25, 1): {
        "signature": "def traverse_linked_list(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = traverse_linked_list(arr)
    return str(result)
"""
    },
    (25, 2): {
        "signature": "def search_linked_list(arr, target):",
        "params": ["list[int]", "int"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    target = int(lines[2])
    result = search_linked_list(arr, target)
    return str(result)
"""
    },
    # Day 26
    (26, 1): {
        "signature": "def reverse_linked_list(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = reverse_linked_list(arr)
    return str(result)
"""
    },
    (26, 2): {
        "signature": "def find_middle(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = find_middle(arr)
    return str(result)
"""
    },
    # Day 27
    (27, 1): {
        "signature": "def fibonacci(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = fibonacci(n)
    return str(result)
"""
    },
    (27, 2): {
        "signature": "def sum_recursive(n):",
        "params": ["int"],
        "wrapper": """
def _run(input_str):
    n = int(input_str.strip())
    result = sum_recursive(n)
    return str(result)
"""
    },
    # Day 28
    (28, 1): {
        "signature": "def is_palindrome_recursive(s):",
        "params": ["str"],
        "wrapper": """
def _run(input_str):
    s = input_str.strip()
    result = is_palindrome_recursive(s)
    return str(result)
"""
    },
    # Day 29
    (29, 1): {
        "signature": "def max_subarray_sum(arr):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr = list(map(int, lines[1].split()))
    result = max_subarray_sum(arr)
    return str(result)
"""
    },
    (29, 2): {
        "signature": "def max_profit(prices):",
        "params": ["list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    prices = list(map(int, lines[1].split()))
    result = max_profit(prices)
    return str(result)
"""
    },
    # Day 30
    (30, 1): {
        "signature": "def merge_sorted_arrays(arr1, arr2):",
        "params": ["list[int]", "list[int]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    arr1 = list(map(int, lines[1].split()))
    arr2 = list(map(int, lines[2].split()))
    result = merge_sorted_arrays(arr1, arr2)
    if isinstance(result, list):
        return ' '.join(map(str, result))
    return str(result).strip()
"""
    },
    # Day 33
    (33, 1): {
        "signature": "def are_anagrams(a, b):",
        "params": ["str", "str"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    a, b = lines[0].strip(), lines[1].strip()
    result = are_anagrams(a, b)
    return str(result)
"""
    },
    (33, 2): {
        "signature": "def longest_common_prefix(words):",
        "params": ["list[str]"],
        "wrapper": """
def _run(input_str):
    lines = input_str.strip().split('\\n')
    n = int(lines[0])
    words = [lines[i+1].strip() for i in range(n)]
    result = longest_common_prefix(words)
    return str(result) if result else ''
"""
    },
}
