"""
Run this once after migrations to load all 57 DSA questions with test cases.
Usage: python manage.py shell < load_questions.py
  OR:  python load_questions.py (from project root with Django configured)
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dsaplatform.settings')
django.setup()

from questions.models import Day, Question, TestCase

# Clear existing data
TestCase.objects.all().delete()
Question.objects.all().delete()
Day.objects.all().delete()

print("Loading 35 days and 57 questions...")

DAYS = [
    # (day_number, title, topics, questions_list)
    # Each question: (order, title, description, input_fmt, output_fmt, constraints, sample_in, sample_out, difficulty, test_cases)
    # Each test_case: (input_data, expected_output, is_sample)
    (1, "Introduction to Programming", "Variables, Input/Output, Data types, Operators", [
        (1, "Sum of Two Numbers",
         "Given two integers A and B, print their sum.",
         "Two space-separated integers A and B",
         "A single integer — the sum of A and B",
         "0 <= A, B <= 10^9",
         "3 5", "8", "easy",
         [("3 5","8",True),("0 0","0",False),("100 200","300",False),("-5 10","5",False),("1000000000 1","1000000001",False)]
        ),
        (2, "Area of a Circle",
         "Given radius r (integer), print the area of a circle rounded to 2 decimal places.\nUse pi = 3.14159265358979",
         "A single integer r",
         "Area rounded to 2 decimal places",
         "1 <= r <= 1000",
         "5", "78.54", "easy",
         [("5","78.54",True),("1","3.14",False),("7","153.94",False),("10","314.16",False),("100","31415.93",False)]
        ),
    ]),
    (2, "Conditionals", "if-else, Comparison operators, Nested if", [
        (1, "Largest of Three Numbers",
         "Given three integers A, B, C, print the largest.",
         "Three space-separated integers A B C",
         "The largest integer",
         "-10^9 <= A, B, C <= 10^9",
         "3 7 5", "7", "easy",
         [("3 7 5","7",True),("10 2 8","10",False),("1 1 1","1",False),("-5 -3 -10","-3",False),("0 0 1","1",False)]
        ),
        (2, "Leap Year Check",
         "Given a year Y, print 'Leap Year' if it is a leap year, else print 'Not a Leap Year'.\nA year is a leap year if divisible by 4, except century years must be divisible by 400.",
         "A single integer Y",
         "'Leap Year' or 'Not a Leap Year'",
         "1 <= Y <= 9999",
         "2000", "Leap Year", "easy",
         [("2000","Leap Year",True),("1900","Not a Leap Year",False),("2024","Leap Year",False),("2023","Not a Leap Year",False),("400","Leap Year",False)]
        ),
        (3, "Check Even or Odd",
         "Given an integer N, print 'Even' if it is even, else print 'Odd'.",
         "A single integer N",
         "'Even' or 'Odd'",
         "-10^9 <= N <= 10^9",
         "4", "Even", "easy",
         [("4","Even",True),("7","Odd",False),("0","Even",False),("-3","Odd",False),("-8","Even",False)]
        ),
    ]),
    (3, "Loops", "for, while, range()", [
        (1, "Multiplication Table of a Number",
         "Given N, print its multiplication table from 1 to 10.\nFormat: 'N x i = result' for i from 1 to 10.",
         "A single integer N",
         "10 lines in format: N x i = result",
         "1 <= N <= 100",
         "3", "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30", "easy",
         [("3","3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30",True),
          ("5","5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50",False),
          ("1","1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10",False)]
        ),
        (2, "Sum of Numbers from 1 to N",
         "Given N, print the sum of all integers from 1 to N (inclusive).",
         "A single integer N",
         "The sum",
         "1 <= N <= 10^6",
         "5", "15", "easy",
         [("5","15",True),("1","1",False),("10","55",False),("100","5050",False),("1000","500500",False)]
        ),
        (3, "Factorial of a Number",
         "Given N, print N! (factorial of N).",
         "A single integer N",
         "The factorial of N",
         "0 <= N <= 15",
         "5", "120", "easy",
         [("5","120",True),("0","1",False),("1","1",False),("10","3628800",False),("7","5040",False)]
        ),
    ]),
    (4, "Nested Loops & Patterns", "Nested loops, Pattern printing", [
        (1, "Print a Square Pattern",
         "Given N, print an N x N square of asterisks.",
         "A single integer N",
         "N lines each with N asterisks separated by spaces",
         "1 <= N <= 10",
         "3", "* * *\n* * *\n* * *", "easy",
         [("3","* * *\n* * *\n* * *",True),("1","*",False),("2","* *\n* *",False),("4","* * * *\n* * * *\n* * * *\n* * * *",False)]
        ),
        (2, "Print a Pyramid Pattern",
         "Given N, print a right-aligned pyramid of N rows.\nRow i has i asterisks separated by spaces.",
         "A single integer N",
         "N lines",
         "1 <= N <= 10",
         "4", "*\n* *\n* * *\n* * * *", "easy",
         [("4","*\n* *\n* * *\n* * * *",True),("1","*",False),("3","*\n* *\n* * *",False),("5","*\n* *\n* * *\n* * * *\n* * * * *",False)]
        ),
    ]),
    (5, "Functions", "Parameters, return, Variable scope", [
        (1, "Check Prime Number",
         "Given N, print 'Prime' if N is prime, else print 'Not Prime'.",
         "A single integer N",
         "'Prime' or 'Not Prime'",
         "1 <= N <= 10^6",
         "7", "Prime", "easy",
         [("7","Prime",True),("1","Not Prime",False),("2","Prime",False),("100","Not Prime",False),("97","Prime",False)]
        ),
        (2, "GCD of Two Numbers",
         "Given two integers A and B, print their Greatest Common Divisor (GCD).",
         "Two space-separated integers A B",
         "The GCD of A and B",
         "1 <= A, B <= 10^9",
         "12 18", "6", "easy",
         [("12 18","6",True),("1 1","1",False),("100 75","25",False),("7 5","1",False),("48 36","12",False)]
        ),
        (3, "Power of a Number (Iterative)",
         "Given base B and exponent E, print B raised to the power E.\nDo not use the ** operator or pow().",
         "Two space-separated integers B E",
         "B^E",
         "1 <= B <= 10, 0 <= E <= 10",
         "2 10", "1024", "easy",
         [("2 10","1024",True),("3 0","1",False),("5 3","125",False),("2 0","1",False),("10 4","10000",False)]
        ),
    ]),
    (6, "Strings", "Indexing, slicing, common methods", [
        (1, "Reverse a String",
         "Given a string S, print it reversed.",
         "A single string S (no spaces)",
         "The reversed string",
         "1 <= len(S) <= 1000",
         "hello", "olleh", "easy",
         [("hello","olleh",True),("a","a",False),("racecar","racecar",False),("python","nohtyp",False),("abcde","edcba",False)]
        ),
        (2, "Check if a String is a Palindrome",
         "Given a string S, print 'Palindrome' if it reads the same forwards and backwards, else print 'Not Palindrome'.",
         "A single string S (no spaces, lowercase)",
         "'Palindrome' or 'Not Palindrome'",
         "1 <= len(S) <= 1000",
         "racecar", "Palindrome", "easy",
         [("racecar","Palindrome",True),("hello","Not Palindrome",False),("a","Palindrome",False),("abba","Palindrome",False),("python","Not Palindrome",False)]
        ),
        (3, "Count Vowels in a String",
         "Given a string S, print the count of vowels (a, e, i, o, u — lowercase only).",
         "A single string S (lowercase, no spaces)",
         "Count of vowels",
         "1 <= len(S) <= 1000",
         "hello", "2", "easy",
         [("hello","2",True),("aeiou","5",False),("xyz","0",False),("programming","3",False),("a","1",False)]
        ),
    ]),
    (7, "Data Structures Basics", "Lists, Tuples, Sets, Dictionaries", [
        (1, "Find the Largest Element in a List",
         "Given N integers, print the largest.",
         "First line: N\nSecond line: N space-separated integers",
         "The largest integer",
         "1 <= N <= 10^5",
         "5\n3 1 4 1 5", "5", "easy",
         [("5\n3 1 4 1 5","5",True),("1\n42","42",False),("4\n-1 -5 -3 -2","-1",False),("3\n0 0 0","0",False),("5\n100 200 50 300 150","300",False)]
        ),
        (2, "Find the Second Largest Element",
         "Given N integers, print the second largest. All elements are distinct.",
         "First line: N\nSecond line: N space-separated integers",
         "The second largest integer",
         "2 <= N <= 10^5, all elements distinct",
         "5\n3 1 4 1 5", "4", "easy",
         [("5\n3 1 4 1 5","4",True),("2\n10 20","10",False),("4\n5 3 8 1","5",False),("3\n100 200 300","200",False)]
        ),
        (3, "Count Frequency of Elements",
         "Given N integers, print each unique element and its frequency in ascending order of element.",
         "First line: N\nSecond line: N space-separated integers",
         "Each line: 'element: count' sorted by element ascending",
         "1 <= N <= 1000, 0 <= each element <= 1000",
         "6\n1 2 1 3 2 1", "1: 3\n2: 2\n3: 1", "easy",
         [("6\n1 2 1 3 2 1","1: 3\n2: 2\n3: 1",True),("3\n5 5 5","5: 3",False),("4\n1 2 3 4","1: 1\n2: 1\n3: 1\n4: 1",False)]
        ),
    ]),
    (8, "Time & Space Complexity", "Big-O, Best/Average/Worst case", []),  # No coding questions this day
    (9, "Arrays — Traversal", "Arrays, traversal, basic operations", [
        (1, "Linear Search",
         "Given N integers and a target T, print the index (0-based) of T. If not found, print -1.",
         "First line: N\nSecond line: N space-separated integers\nThird line: T",
         "Index of T or -1",
         "1 <= N <= 10^5",
         "5\n2 4 6 8 10\n6", "2", "easy",
         [("5\n2 4 6 8 10\n6","2",True),("3\n1 2 3\n5","-1",False),("1\n7\n7","0",False),("4\n10 20 30 40\n10","0",False),("4\n10 20 30 40\n40","3",False)]
        ),
        (2, "Find the Maximum Element in an Array",
         "Given N integers, print the maximum element.",
         "First line: N\nSecond line: N space-separated integers",
         "The maximum element",
         "1 <= N <= 10^5",
         "5\n3 1 4 1 5", "5", "easy",
         [("5\n3 1 4 1 5","5",True),("1\n-100","-100",False),("3\n0 0 0","0",False),("4\n-5 -1 -3 -2","-1",False)]
        ),
    ]),
    (10, "Arrays — Reversal & Rotation", "Reversal, rotation", [
        (1, "Reverse an Array (In Place)",
         "Given N integers, print them in reverse order.",
         "First line: N\nSecond line: N space-separated integers",
         "N space-separated integers in reverse order",
         "1 <= N <= 10^5",
         "5\n1 2 3 4 5", "5 4 3 2 1", "easy",
         [("5\n1 2 3 4 5","5 4 3 2 1",True),("1\n42","42",False),("3\n1 2 3","3 2 1",False),("4\n10 20 30 40","40 30 20 10",False)]
        ),
        (2, "Rotate an Array by K Positions",
         "Given N integers and K, print the array rotated K positions to the right.",
         "First line: N K\nSecond line: N space-separated integers",
         "N space-separated integers after rotation",
         "1 <= N <= 10^5, 0 <= K <= N",
         "5 2\n1 2 3 4 5", "4 5 1 2 3", "easy",
         [("5 2\n1 2 3 4 5","4 5 1 2 3",True),("3 1\n1 2 3","3 1 2",False),("4 0\n1 2 3 4","1 2 3 4",False),("3 3\n1 2 3","1 2 3",False)]
        ),
    ]),
    (11, "Arrays — Interview Patterns", "Move zeroes, remove duplicates", [
        (1, "Move All Zeroes to the End",
         "Given N integers, move all zeroes to the end while maintaining relative order of non-zero elements.",
         "First line: N\nSecond line: N space-separated integers",
         "N space-separated integers",
         "1 <= N <= 10^5",
         "6\n0 1 0 3 12 0", "1 3 12 0 0 0", "easy",
         [("6\n0 1 0 3 12 0","1 3 12 0 0 0",True),("3\n0 0 0","0 0 0",False),("3\n1 2 3","1 2 3",False),("4\n0 1 2 0","1 2 0 0",False)]
        ),
        (2, "Remove Duplicates from a Sorted Array",
         "Given a sorted array of N integers, print only the unique elements in sorted order.",
         "First line: N\nSecond line: N space-separated sorted integers",
         "Unique elements space-separated",
         "1 <= N <= 10^5",
         "6\n1 1 2 3 3 4", "1 2 3 4", "easy",
         [("6\n1 1 2 3 3 4","1 2 3 4",True),("4\n1 1 1 1","1",False),("3\n1 2 3","1 2 3",False),("5\n1 2 2 3 4","1 2 3 4",False)]
        ),
    ]),
    (12, "Sorting I", "Bubble Sort, Selection Sort", [
        (1, "Implement Bubble Sort",
         "Given N integers, sort them using Bubble Sort and print in ascending order.",
         "First line: N\nSecond line: N space-separated integers",
         "Sorted integers space-separated",
         "1 <= N <= 1000",
         "5\n5 3 1 4 2", "1 2 3 4 5", "easy",
         [("5\n5 3 1 4 2","1 2 3 4 5",True),("3\n3 1 2","1 2 3",False),("1\n5","5",False),("4\n4 3 2 1","1 2 3 4",False),("3\n1 1 1","1 1 1",False)]
        ),
        (2, "Implement Selection Sort",
         "Given N integers, sort them using Selection Sort and print in ascending order.",
         "First line: N\nSecond line: N space-separated integers",
         "Sorted integers space-separated",
         "1 <= N <= 1000",
         "5\n64 25 12 22 11", "11 12 22 25 64", "easy",
         [("5\n64 25 12 22 11","11 12 22 25 64",True),("3\n3 1 2","1 2 3",False),("1\n99","99",False),("4\n-3 -1 -2 -4","-4 -3 -2 -1",False)]
        ),
    ]),
    (13, "Sorting II", "Insertion Sort, built-in sort", [
        (1, "Implement Insertion Sort",
         "Given N integers, sort them using Insertion Sort and print in ascending order.",
         "First line: N\nSecond line: N space-separated integers",
         "Sorted integers space-separated",
         "1 <= N <= 1000",
         "5\n12 11 13 5 6", "5 6 11 12 13", "easy",
         [("5\n12 11 13 5 6","5 6 11 12 13",True),("3\n3 1 2","1 2 3",False),("4\n4 3 2 1","1 2 3 4",False),("1\n7","7",False)]
        ),
        (2, "Check if an Array is Sorted",
         "Given N integers, print 'Sorted' if they are in non-decreasing order, else print 'Not Sorted'.",
         "First line: N\nSecond line: N space-separated integers",
         "'Sorted' or 'Not Sorted'",
         "1 <= N <= 10^5",
         "4\n1 2 3 4", "Sorted", "easy",
         [("4\n1 2 3 4","Sorted",True),("3\n3 1 2","Not Sorted",False),("1\n5","Sorted",False),("3\n1 1 1","Sorted",False),("3\n3 2 1","Not Sorted",False)]
        ),
    ]),
    (14, "Revision — Arrays & Sorting", "Timed mini-contest", []),
    (15, "Hashing I", "Dictionaries, sets for lookup", [
        (1, "Frequency of Each Character in a String",
         "Given a string S, print each character and its frequency in the order they first appear.",
         "A single string S (lowercase, no spaces)",
         "Each line: 'char: count'",
         "1 <= len(S) <= 1000",
         "hello", "h: 1\ne: 1\nl: 2\no: 1", "easy",
         [("hello","h: 1\ne: 1\nl: 2\no: 1",True),("aab","a: 2\nb: 1",False),("abc","a: 1\nb: 1\nc: 1",False),("aaa","a: 3",False)]
        ),
        (2, "Find the First Non-Repeating Character",
         "Given a string S (lowercase), print the first character that appears exactly once. If none, print -1.",
         "A single string S (lowercase, no spaces)",
         "The first non-repeating character or -1",
         "1 <= len(S) <= 10^5",
         "leetcode", "l", "easy",
         [("leetcode","l",True),("aabb","-1",False),("abcd","a",False),("aabbc","c",False),("z","z",False)]
        ),
    ]),
    (16, "Hashing II", "Interview classics", [
        (1, "Two Sum — Unsorted Array",
         "Given N integers and a target T, print the indices (0-based) of the two numbers that add up to T.\nPrint the smaller index first. Exactly one solution exists.",
         "First line: N\nSecond line: N space-separated integers\nThird line: T",
         "Two space-separated indices",
         "2 <= N <= 10^4",
         "4\n2 7 11 15\n9", "0 1", "medium",
         [("4\n2 7 11 15\n9","0 1",True),("3\n3 2 4\n6","1 2",False),("2\n3 3\n6","0 1",False),("4\n1 5 3 2\n4","2 3",False)]
        ),
        (2, "Check for Duplicates in an Array",
         "Given N integers, print 'True' if any value appears more than once, else print 'False'.",
         "First line: N\nSecond line: N space-separated integers",
         "'True' or 'False'",
         "1 <= N <= 10^5",
         "4\n1 2 3 1", "True", "easy",
         [("4\n1 2 3 1","True",True),("3\n1 2 3","False",False),("1\n1","False",False),("3\n1 1 1","True",False)]
        ),
    ]),
    (17, "Binary Search I", "Iterative and recursive", [
        (1, "Binary Search (Iterative)",
         "Given N sorted integers and target T, print the index (0-based) of T. If not found, print -1.\nImplement iterative binary search.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: T",
         "Index of T or -1",
         "1 <= N <= 10^5",
         "6\n1 3 5 7 9 11\n7", "3", "easy",
         [("6\n1 3 5 7 9 11\n7","3",True),("5\n1 2 3 4 5\n6","-1",False),("1\n1\n1","0",False),("4\n2 4 6 8\n2","0",False),("4\n2 4 6 8\n8","3",False)]
        ),
        (2, "Binary Search (Recursive)",
         "Given N sorted integers and target T, print the index (0-based) of T. If not found, print -1.\nImplement recursive binary search.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: T",
         "Index of T or -1",
         "1 <= N <= 10^5",
         "6\n1 3 5 7 9 11\n5", "2", "easy",
         [("6\n1 3 5 7 9 11\n5","2",True),("3\n1 2 3\n4","-1",False),("1\n5\n5","0",False),("4\n1 3 5 7\n1","0",False)]
        ),
    ]),
    (18, "Binary Search II", "Variants", [
        (1, "First and Last Occurrence of an Element",
         "Given a sorted array of N integers and target T, print the first and last index (0-based) of T.\nIf not found, print '-1 -1'.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: T",
         "Two space-separated integers: first_index last_index",
         "1 <= N <= 10^5",
         "7\n1 2 2 2 3 4 5\n2", "1 3", "medium",
         [("7\n1 2 2 2 3 4 5\n2","1 3",True),("5\n1 2 3 4 5\n6","-1 -1",False),("4\n1 1 1 1\n1","0 3",False),("3\n1 2 3\n3","2 2",False)]
        ),
        (2, "Find Floor and Ceil in a Sorted Array",
         "Given a sorted array and target T, print floor and ceil of T.\nFloor = largest element <= T. Ceil = smallest element >= T.\nIf floor doesn't exist print -1. If ceil doesn't exist print -1.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: T",
         "Two space-separated integers: floor ceil",
         "1 <= N <= 10^5",
         "6\n1 2 4 6 8 10\n5", "4 6", "medium",
         [("6\n1 2 4 6 8 10\n5","4 6",True),("4\n1 2 3 4\n2","2 2",False),("3\n1 3 5\n0","-1 1",False),("3\n1 3 5\n6","5 -1",False)]
        ),
    ]),
    (19, "Two Pointer", "Two pointer technique", [
        (1, "Two Sum — Sorted Array",
         "Given a sorted array of N integers and a target T, print the indices (1-based) of the two numbers that add up to T.\nPrint smaller index first. Exactly one solution exists.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: T",
         "Two space-separated 1-based indices",
         "2 <= N <= 10^4",
         "4\n2 7 11 15\n9", "1 2", "easy",
         [("4\n2 7 11 15\n9","1 2",True),("4\n1 2 3 4\n7","3 4",False),("2\n1 3\n4","1 2",False),("4\n1 3 4 6\n7","2 4",False)]
        ),
        (2, "Pair with a Given Sum (Sorted Array)",
         "Given a sorted array of N integers and target S, print 'Found' if any pair sums to S, else 'Not Found'.",
         "First line: N\nSecond line: N sorted space-separated integers\nThird line: S",
         "'Found' or 'Not Found'",
         "2 <= N <= 10^5",
         "5\n1 2 3 4 5\n9", "Found", "easy",
         [("5\n1 2 3 4 5\n9","Found",True),("4\n1 2 3 4\n10","Not Found",False),("3\n1 2 3\n5","Found",False),("2\n1 2\n3","Found",False)]
        ),
    ]),
    (20, "Sliding Window", "Fixed and variable window", [
        (1, "Maximum Sum Subarray of Size K",
         "Given N integers and K, print the maximum sum of any contiguous subarray of size K.",
         "First line: N K\nSecond line: N space-separated integers",
         "The maximum sum",
         "1 <= K <= N <= 10^5",
         "5 3\n2 1 5 1 3", "9", "easy",
         [("5 3\n2 1 5 1 3","9",True),("4 2\n1 2 3 4","7",False),("3 1\n5 3 8","8",False),("5 5\n1 2 3 4 5","15",False)]
        ),
        (2, "Longest Subarray with Sum <= K",
         "Given N positive integers and K, print the length of the longest subarray whose sum is <= K.",
         "First line: N K\nSecond line: N space-separated positive integers",
         "Length of the longest valid subarray",
         "1 <= N <= 10^5, 1 <= K <= 10^9",
         "5 10\n1 2 3 4 5", "4", "medium",
         [("5 10\n1 2 3 4 5","4",True),("3 1\n1 1 1","1",False),("4 15\n1 2 3 4","4",False),("3 3\n4 2 1","1",False)]
        ),
    ]),
    (21, "Revision — Hashing, Binary Search, Two Pointer", "Mock test", []),
    (22, "Stack", "Concept and implementation", [
        (1, "Implement a Stack Using a List",
         "Perform Q stack operations. Operations: PUSH x, POP, PEEK, SIZE.\nFor POP: print popped element or 'Empty' if stack is empty.\nFor PEEK: print top element or 'Empty' if stack is empty.\nFor SIZE: print current size.",
         "First line: Q (number of operations)\nNext Q lines: operation",
         "Output for POP, PEEK, SIZE operations",
         "1 <= Q <= 1000",
         "5\nPUSH 1\nPUSH 2\nPEEK\nPOP\nSIZE", "2\n2\n1", "easy",
         [("5\nPUSH 1\nPUSH 2\nPEEK\nPOP\nSIZE","2\n2\n1",True),("3\nPOP\nPUSH 5\nPEEK","Empty\n5",False),("4\nPUSH 3\nPUSH 4\nPOP\nPOP","4\n3",False)]
        ),
        (2, "Valid Parentheses / Balanced Brackets",
         "Given a string of brackets, print 'Valid' if they are balanced, else print 'Invalid'.\nBrackets: ( ) [ ] { }",
         "A single string of brackets",
         "'Valid' or 'Invalid'",
         "1 <= len(S) <= 10^4",
         "([]{})", "Valid", "easy",
         [("([]{})","Valid",True),("([)]","Invalid",False),("","Valid",False),("{[]}","Valid",False),("((","Invalid",False)]
        ),
    ]),
    (23, "Stack — Interview Application", "Next Greater Element", [
        (1, "Next Greater Element (Brute Force)",
         "Given N integers, for each element print the next greater element to its right. If none exists, print -1.",
         "First line: N\nSecond line: N space-separated integers",
         "N space-separated integers (next greater elements)",
         "1 <= N <= 10^4",
         "4\n4 5 2 10", "5 10 10 -1", "medium",
         [("4\n4 5 2 10","5 10 10 -1",True),("3\n3 2 1","-1 -1 -1",False),("3\n1 2 3","2 3 -1",False),("1\n5","-1",False)]
        ),
    ]),
    (24, "Queue", "Concept and implementation", [
        (1, "Implement a Queue Using a List",
         "Perform Q queue operations: ENQUEUE x, DEQUEUE, FRONT, SIZE.\nFor DEQUEUE: print dequeued element or 'Empty'.\nFor FRONT: print front element or 'Empty'.\nFor SIZE: print current size.",
         "First line: Q\nNext Q lines: operation",
         "Output for DEQUEUE, FRONT, SIZE operations",
         "1 <= Q <= 1000",
         "5\nENQUEUE 1\nENQUEUE 2\nFRONT\nDEQUEUE\nSIZE", "1\n1\n1", "easy",
         [("5\nENQUEUE 1\nENQUEUE 2\nFRONT\nDEQUEUE\nSIZE","1\n1\n1",True),("3\nDEQUEUE\nENQUEUE 5\nFRONT","Empty\n5",False),("4\nENQUEUE 3\nENQUEUE 4\nDEQUEUE\nDEQUEUE","3\n4",False)]
        ),
    ]),
    (25, "Linked List I", "Traversal, insertion, deletion", [
        (1, "Traverse and Print a Linked List",
         "Given N integers, build a linked list and print all elements separated by ' -> ', ending with 'None'.",
         "First line: N\nSecond line: N space-separated integers",
         "Elements separated by ' -> ' followed by ' -> None'",
         "1 <= N <= 1000",
         "4\n1 2 3 4", "1 -> 2 -> 3 -> 4 -> None", "easy",
         [("4\n1 2 3 4","1 -> 2 -> 3 -> 4 -> None",True),("1\n5","5 -> None",False),("3\n10 20 30","10 -> 20 -> 30 -> None",False)]
        ),
        (2, "Search an Element in a Linked List",
         "Given N integers forming a linked list and a target T, print the 0-based index of T. If not found, print -1.",
         "First line: N\nSecond line: N space-separated integers\nThird line: T",
         "Index of T or -1",
         "1 <= N <= 1000",
         "5\n1 2 3 4 5\n3", "2", "easy",
         [("5\n1 2 3 4 5\n3","2",True),("3\n1 2 3\n5","-1",False),("1\n7\n7","0",False),("4\n10 20 30 40\n40","3",False)]
        ),
    ]),
    (26, "Linked List II", "Reverse, find middle", [
        (1, "Reverse a Linked List (Iterative)",
         "Given N integers forming a linked list, reverse it and print elements separated by ' -> ', ending with 'None'.",
         "First line: N\nSecond line: N space-separated integers",
         "Reversed linked list as 'e1 -> e2 -> ... -> None'",
         "1 <= N <= 1000",
         "4\n1 2 3 4", "4 -> 3 -> 2 -> 1 -> None", "easy",
         [("4\n1 2 3 4","4 -> 3 -> 2 -> 1 -> None",True),("1\n5","5 -> None",False),("3\n1 2 3","3 -> 2 -> 1 -> None",False),("2\n10 20","20 -> 10 -> None",False)]
        ),
        (2, "Find the Middle Node of a Linked List",
         "Given N integers forming a linked list, print the value of the middle node.\nIf two middle nodes, print the second middle (standard slow/fast pointer behavior).",
         "First line: N\nSecond line: N space-separated integers",
         "The middle element",
         "1 <= N <= 1001",
         "5\n1 2 3 4 5", "3", "easy",
         [("5\n1 2 3 4 5","3",True),("1\n7","7",False),("4\n1 2 3 4","3",False),("6\n1 2 3 4 5 6","4",False),("3\n1 2 3","2",False)]
        ),
    ]),
    (27, "Recursion I", "Basics", [
        (1, "Fibonacci Using Recursion",
         "Given N, print the Nth Fibonacci number.\nF(0) = 0, F(1) = 1, F(N) = F(N-1) + F(N-2)",
         "A single integer N",
         "The Nth Fibonacci number",
         "0 <= N <= 20",
         "7", "13", "easy",
         [("7","13",True),("0","0",False),("1","1",False),("10","55",False),("15","610",False)]
        ),
        (2, "Sum of First N Numbers Using Recursion",
         "Given N, print the sum of all integers from 1 to N using recursion.",
         "A single integer N",
         "The sum",
         "1 <= N <= 1000",
         "5", "15", "easy",
         [("5","15",True),("1","1",False),("10","55",False),("100","5050",False)]
        ),
    ]),
    (28, "Recursion + Mini Contest", "Recursion practice", [
        (1, "Check if a String is a Palindrome (Recursion)",
         "Given a string S, print 'Palindrome' if it reads same forwards and backwards using a recursive approach, else print 'Not Palindrome'.",
         "A single string S (lowercase, no spaces)",
         "'Palindrome' or 'Not Palindrome'",
         "1 <= len(S) <= 1000",
         "madam", "Palindrome", "easy",
         [("madam","Palindrome",True),("hello","Not Palindrome",False),("a","Palindrome",False),("abba","Palindrome",False)]
        ),
    ]),
    (29, "High-Frequency Patterns", "Kadane's, Stock problem", [
        (1, "Maximum Subarray Sum — Kadane's Algorithm",
         "Given N integers (may include negatives), print the maximum sum of any contiguous subarray.",
         "First line: N\nSecond line: N space-separated integers",
         "The maximum subarray sum",
         "1 <= N <= 10^5",
         "8\n-2 1 -3 4 -1 2 1 -5 4", "6", "medium",
         [("8\n-2 1 -3 4 -1 2 1 -5 4","6",True),("1\n-1","-1",False),("3\n1 2 3","6",False),("4\n-3 -1 -2 -4","-1",False),("5\n5 -3 5 -1 5","11",False)]
        ),
        (2, "Best Time to Buy and Sell Stock",
         "Given N prices, print the maximum profit from one buy and one sell (buy before sell). If no profit possible, print 0.",
         "First line: N\nSecond line: N space-separated integers",
         "Maximum profit",
         "1 <= N <= 10^5",
         "6\n7 1 5 3 6 4", "5", "medium",
         [("6\n7 1 5 3 6 4","5",True),("5\n7 6 4 3 1","0",False),("3\n1 2 3","2",False),("4\n3 3 3 3","0",False),("5\n1 5 2 8 3","7",False)]
        ),
    ]),
    (30, "Mock Interview Round I", "Mixed topics", [
        (1, "Merge Two Sorted Arrays Without Extra Space",
         "Given two sorted arrays of sizes M and N, print the merged sorted array.",
         "First line: M N\nSecond line: M space-separated sorted integers\nThird line: N space-separated sorted integers",
         "M+N space-separated sorted integers",
         "1 <= M, N <= 10^4",
         "3 3\n1 3 5\n2 4 6", "1 2 3 4 5 6", "medium",
         [("3 3\n1 3 5\n2 4 6","1 2 3 4 5 6",True),("2 2\n1 2\n3 4","1 2 3 4",False),("1 3\n2\n1 3 5","1 2 3 5",False),("3 1\n1 2 3\n4","1 2 3 4",False)]
        ),
    ]),
    (31, "Mock Online Assessment", "Full timed test", []),
    (32, "Mock Interview — Approach Explanation", "Time complexity Q&A", []),
    (33, "Company-Style Problems", "Anagrams, Longest Common Prefix", [
        (1, "Check if Two Strings are Anagrams",
         "Given two strings A and B (lowercase), print 'Anagram' if they are anagrams, else print 'Not Anagram'.",
         "First line: A\nSecond line: B",
         "'Anagram' or 'Not Anagram'",
         "1 <= len(A), len(B) <= 10^4",
         "listen\nsilent", "Anagram", "easy",
         [("listen\nsilent","Anagram",True),("hello\nworld","Not Anagram",False),("abc\ncba","Anagram",False),("a\naa","Not Anagram",False)]
        ),
        (2, "Longest Common Prefix",
         "Given N strings, print the longest common prefix among all of them. If none, print ''.",
         "First line: N\nNext N lines: one string each",
         "The longest common prefix (or empty line if none)",
         "1 <= N <= 100, 1 <= len(each string) <= 200",
         "3\nflower\nflow\nflight", "fl", "easy",
         [("3\nflower\nflow\nflight","fl",True),("3\ndog\ncar\nrace","",False),("2\nabc\nabc","abc",False),("1\nhello","hello",False)]
        ),
    ]),
    (34, "Mixed Revision", "Quick recap across all topics", []),
    (35, "Final Contest + Wrap-up", "Mixed questions from full bank", []),
]

total_q = 0
for day_data in DAYS:
    day_num, title, topics, questions = day_data
    day = Day.objects.create(
        day_number=day_num,
        title=title,
        topics=topics,
        is_unlocked=(day_num == 1),  # Day 1 unlocked by default
    )
    for q_data in questions:
        order, qtitle, desc, inp_fmt, out_fmt, constraints, s_in, s_out, diff, test_cases = q_data
        question = Question.objects.create(
            day=day, order=order, title=qtitle,
            description=desc, input_format=inp_fmt,
            output_format=out_fmt, constraints=constraints,
            sample_input=s_in, sample_output=s_out,
            difficulty=diff,
        )
        for tc_order, (inp, out, is_sample) in enumerate(test_cases, 1):
            TestCase.objects.create(
                question=question, input_data=inp,
                expected_output=out, is_sample=is_sample, order=tc_order,
            )
        total_q += 1

print(f"Done! Loaded 35 days and {total_q} questions with test cases.")
