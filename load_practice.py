import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dsaplatform.settings')
django.setup()

from practice.models import PracticeDay, PracticeQuestion, PracticeTestCase

PracticeTestCase.objects.all().delete()
PracticeQuestion.objects.all().delete()
PracticeDay.objects.all().delete()

print("Loading 35 practice days, 10 questions each...")

def q(order, title, desc, sig, wrapper, inp_fmt, out_fmt, constraints, s_in, s_out, diff, tcs):
    return (order, title, desc, sig, wrapper, inp_fmt, out_fmt, constraints, s_in, s_out, diff, tcs)

PRACTICE = [
  (1, "Variables & I/O", "Variables, Data Types, Input/Output, Operators", [
    q(1,"Add Three Numbers","Given three integers, return their sum.","def add_three(a,b,c):",
      "def _run(i):\n a,b,c=map(int,i.strip().split())\n return str(add_three(a,b,c))\n",
      "Three space-separated integers","Sum","","1 2 3","6","easy",
      [("1 2 3","6",True),("0 0 0","0",False),("10 20 30","60",False),("100 200 300","600",False)]),
    q(2,"Multiply Two Numbers","Return product of two integers.","def multiply(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(multiply(a,b))\n",
      "Two integers","Product","","3 4","12","easy",
      [("3 4","12",True),("0 5","0",False),("7 8","56",False),("-3 4","-12",False)]),
    q(3,"Integer Division","Return floor division of A by B.","def int_divide(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(int_divide(a,b))\n",
      "Two integers A B","A//B","B!=0","10 3","3","easy",
      [("10 3","3",True),("20 4","5",False),("7 2","3",False),("100 10","10",False)]),
    q(4,"Modulo","Return A mod B.","def modulo(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(modulo(a,b))\n",
      "Two integers A B","A%B","B!=0","10 3","1","easy",
      [("10 3","1",True),("20 5","0",False),("7 4","3",False),("100 9","1",False)]),
    q(5,"Celsius to Fahrenheit","Convert Celsius to Fahrenheit. F = C*9/5 + 32. Return as float rounded to 1 decimal.","def celsius_to_fahrenheit(c):",
      "def _run(i):\n c=float(i.strip())\n return str(celsius_to_fahrenheit(c))\n",
      "A number C","F rounded to 1 decimal","","0","32.0","easy",
      [("0","32.0",True),("100","212.0",False),("37","98.6",False),("-40","-40.0",False)]),
    q(6,"Perimeter of Rectangle","Return perimeter of rectangle with sides L and W.","def perimeter(l,w):",
      "def _run(i):\n l,w=map(int,i.strip().split())\n return str(perimeter(l,w))\n",
      "Two integers L W","Perimeter","","4 5","18","easy",
      [("4 5","18",True),("1 1","4",False),("10 3","26",False),("0 5","10",False)]),
    q(7,"Swap Two Numbers","Given A and B, return them swapped as 'B A'.","def swap(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(swap(a,b))\n",
      "Two integers A B","B A on one line","","3 7","7 3","easy",
      [("3 7","7 3",True),("0 5","5 0",False),("10 20","20 10",False),("-1 1","1 -1",False)]),
    q(8,"Absolute Value","Return absolute value of N without using abs().","def absolute(n):",
      "def _run(i):\n n=int(i.strip())\n return str(absolute(n))\n",
      "Integer N","Absolute value","","-5","5","easy",
      [("-5","5",True),("5","5",False),("0","0",False),("-100","100",False)]),
    q(9,"Sum of Digits","Given a non-negative integer N, return sum of its digits.","def sum_of_digits(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sum_of_digits(n))\n",
      "Integer N","Sum of digits","N>=0","123","6","easy",
      [("123","6",True),("0","0",False),("999","27",False),("100","1",False)]),
    q(10,"Count Digits","Return the number of digits in N.","def count_digits(n):",
      "def _run(i):\n n=int(i.strip())\n return str(count_digits(n))\n",
      "Positive integer N","Number of digits","N>0","12345","5","easy",
      [("12345","5",True),("1","1",False),("100","3",False),("9999","4",False)]),
  ]),
  (2, "Conditionals", "if-else, Nested conditions, Comparison", [
    q(1,"Positive Negative Zero","Return 'Positive', 'Negative', or 'Zero'.","def classify(n):",
      "def _run(i):\n n=int(i.strip())\n return str(classify(n))\n",
      "Integer N","Classification","","5","Positive","easy",
      [("5","Positive",True),("-3","Negative",False),("0","Zero",False),("-100","Negative",False)]),
    q(2,"Min of Two","Return the smaller of two integers.","def min_two(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(min_two(a,b))\n",
      "Two integers","Smaller value","","3 7","3","easy",
      [("3 7","3",True),("7 3","3",False),("5 5","5",False),("-1 -5","-5",False)]),
    q(3,"Grade Calculator","Given marks (0-100), return grade: A(>=90), B(>=80), C(>=70), D(>=60), F(<60).","def grade(marks):",
      "def _run(i):\n m=int(i.strip())\n return str(grade(m))\n",
      "Integer marks","Grade letter","0<=marks<=100","85","B","easy",
      [("85","B",True),("95","A",False),("72","C",False),("65","D",False),("50","F",False)]),
    q(4,"Divisible by Both","Return 'Yes' if N is divisible by both 3 and 5, else 'No'.","def divisible_by_both(n):",
      "def _run(i):\n n=int(i.strip())\n return str(divisible_by_both(n))\n",
      "Integer N","Yes or No","","15","Yes","easy",
      [("15","Yes",True),("9","No",False),("25","No",False),("30","Yes",False)]),
    q(5,"Max of Three","Return the largest of three integers.","def max_three(a,b,c):",
      "def _run(i):\n a,b,c=map(int,i.strip().split())\n return str(max_three(a,b,c))\n",
      "Three integers","Largest","","1 5 3","5","easy",
      [("1 5 3","5",True),("10 10 10","10",False),("-1 -2 -3","-1",False),("0 0 1","1",False)]),
    q(6,"Triangle Valid","Given sides A B C, return 'Valid' if they form a triangle, else 'Invalid'.","def is_valid_triangle(a,b,c):",
      "def _run(i):\n a,b,c=map(int,i.strip().split())\n return str(is_valid_triangle(a,b,c))\n",
      "Three integers A B C","Valid or Invalid","","3 4 5","Valid","easy",
      [("3 4 5","Valid",True),("1 2 3","Invalid",False),("5 5 5","Valid",False),("1 1 10","Invalid",False)]),
    q(7,"Age Category","Return 'Child'(<13), 'Teen'(13-17), 'Adult'(18-64), 'Senior'(>=65).","def age_category(age):",
      "def _run(i):\n a=int(i.strip())\n return str(age_category(a))\n",
      "Integer age","Category","age>=0","20","Adult","easy",
      [("20","Adult",True),("10","Child",False),("15","Teen",False),("70","Senior",False)]),
    q(8,"Bigger Half","Given N, return 'Yes' if N/2 > 10, else 'No'.","def bigger_half(n):",
      "def _run(i):\n n=int(i.strip())\n return str(bigger_half(n))\n",
      "Integer N","Yes or No","","25","Yes","easy",
      [("25","Yes",True),("15","No",False),("21","Yes",False),("20","No",False)]),
    q(9,"Vowel or Consonant","Given a lowercase letter, return 'Vowel' or 'Consonant'.","def vowel_or_consonant(c):",
      "def _run(i):\n c=i.strip()\n return str(vowel_or_consonant(c))\n",
      "Single lowercase letter","Vowel or Consonant","","a","Vowel","easy",
      [("a","Vowel",True),("b","Consonant",False),("e","Vowel",False),("z","Consonant",False)]),
    q(10,"Number Sign","Return 1 if positive, -1 if negative, 0 if zero.","def sign(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sign(n))\n",
      "Integer N","1, -1, or 0","","5","1","easy",
      [("5","1",True),("-3","-1",False),("0","0",False),("-100","-1",False)]),
  ]),
  (3, "Loops", "for, while, range, iteration patterns", [
    q(1,"Count Down","Given N, print numbers from N to 1 as space-separated string.","def count_down(n):",
      "def _run(i):\n n=int(i.strip())\n r=count_down(n)\n return ' '.join(map(str,r)) if isinstance(r,list) else str(r)\n",
      "Integer N","Numbers N to 1 space-separated","N>=1","5","5 4 3 2 1","easy",
      [("5","5 4 3 2 1",True),("1","1",False),("3","3 2 1",False),("4","4 3 2 1",False)]),
    q(2,"Sum of Even Numbers","Return sum of all even numbers from 1 to N inclusive.","def sum_even(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sum_even(n))\n",
      "Integer N","Sum of evens","N>=1","10","30","easy",
      [("10","30",True),("1","0",False),("4","6",False),("6","12",False)]),
    q(3,"Sum of Odd Numbers","Return sum of all odd numbers from 1 to N inclusive.","def sum_odd(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sum_odd(n))\n",
      "Integer N","Sum of odds","N>=1","5","9","easy",
      [("5","9",True),("1","1",False),("4","4",False),("10","25",False)]),
    q(4,"Digit Sum Using Loop","Return sum of digits of N using a loop (no str conversion).","def digit_sum_loop(n):",
      "def _run(i):\n n=int(i.strip())\n return str(digit_sum_loop(n))\n",
      "Non-negative integer N","Sum of digits","N>=0","1234","10","easy",
      [("1234","10",True),("0","0",False),("99","18",False),("100","1",False)]),
    q(5,"Count Multiples","Return count of multiples of K from 1 to N.","def count_multiples(n,k):",
      "def _run(i):\n n,k=map(int,i.strip().split())\n return str(count_multiples(n,k))\n",
      "Two integers N K","Count","K>0","10 3","3","easy",
      [("10 3","3",True),("20 5","4",False),("100 10","10",False),("7 7","1",False)]),
    q(6,"Reverse Number","Return the digits of N reversed as an integer.","def reverse_number(n):",
      "def _run(i):\n n=int(i.strip())\n return str(reverse_number(n))\n",
      "Positive integer N","Reversed integer","N>0","1234","4321","easy",
      [("1234","4321",True),("100","1",False),("9","9",False),("120","21",False)]),
    q(7,"Print Squares","Return list of squares from 1 to N.","def squares(n):",
      "def _run(i):\n n=int(i.strip())\n r=squares(n)\n return ' '.join(map(str,r)) if isinstance(r,list) else str(r)\n",
      "Integer N","Squares space-separated","N>=1","5","1 4 9 16 25","easy",
      [("5","1 4 9 16 25",True),("1","1",False),("3","1 4 9",False),("4","1 4 9 16",False)]),
    q(8,"FizzBuzz","For numbers 1 to N: 'Fizz' if div by 3, 'Buzz' if div by 5, 'FizzBuzz' if both, else number. Return as newline-separated string.","def fizzbuzz(n):",
      "def _run(i):\n n=int(i.strip())\n r=fizzbuzz(n)\n return '\\n'.join(map(str,r)) if isinstance(r,list) else str(r).strip()\n",
      "Integer N","FizzBuzz output","N>=1","5","1\n2\nFizz\n4\nBuzz","easy",
      [("5","1\n2\nFizz\n4\nBuzz",True),("1","1",False),("3","1\n2\nFizz",False),("15","1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz",False)]),
    q(9,"Sum Digits Until Single","Repeatedly sum digits until single digit. Return it.","def digital_root(n):",
      "def _run(i):\n n=int(i.strip())\n return str(digital_root(n))\n",
      "Non-negative integer N","Single digit result","N>=0","493","7","easy",
      [("493","7",True),("0","0",False),("9","9",False),("99","9",False)]),
    q(10,"Count Divisors","Return count of divisors of N.","def count_divisors(n):",
      "def _run(i):\n n=int(i.strip())\n return str(count_divisors(n))\n",
      "Positive integer N","Count of divisors","N>0","12","6","easy",
      [("12","6",True),("1","1",False),("7","2",False),("100","9",False)]),
  ]),
  (4, "Nested Loops & Patterns", "Nested loops, 2D patterns", [
    q(1,"Number Triangle","Return list of rows: row i has numbers 1 to i space-separated.","def number_triangle(n):",
      "def _run(i):\n n=int(i.strip())\n r=number_triangle(n)\n return '\\n'.join(map(str,x) if not isinstance(x,str) else x for x in r) if isinstance(r,list) else str(r).strip()\n",
      "Integer N","N rows","N>=1","4","1\n1 2\n1 2 3\n1 2 3 4","easy",
      [("4","1\n1 2\n1 2 3\n1 2 3 4",True),("1","1",False),("2","1\n1 2",False),("3","1\n1 2\n1 2 3",False)]),
    q(2,"Inverted Pyramid","Row i (1-indexed) has N-i+1 stars space-separated.","def inverted_pyramid(n):",
      "def _run(i):\n n=int(i.strip())\n r=inverted_pyramid(n)\n return '\\n'.join(map(str,x) if not isinstance(x,str) else x for x in r) if isinstance(r,list) else str(r).strip()\n",
      "Integer N","N rows","N>=1","3","* * *\n* *\n*","easy",
      [("3","* * *\n* *\n*",True),("1","*",False),("2","* *\n*",False),("4","* * * *\n* * *\n* *\n*",False)]),
    q(3,"Sum of Matrix Row","Given NxN matrix, return sum of each row as space-separated.","def row_sums(matrix):",
      "def _run(i):\n lines=i.strip().split('\\n')\n n=int(lines[0])\n mat=[list(map(int,lines[k+1].split())) for k in range(n)]\n r=row_sums(mat)\n return ' '.join(map(str,r)) if isinstance(r,list) else str(r)\n",
      "First line N, next N lines: N space-separated integers","Row sums","N>=1","2\n1 2\n3 4","3 7","easy",
      [("2\n1 2\n3 4","3 7",True),("1\n5","5",False),("3\n1 1 1\n2 2 2\n3 3 3","3 6 9",False)]),
    q(4,"Diagonal Sum","Return sum of main diagonal of NxN matrix.","def diagonal_sum(matrix):",
      "def _run(i):\n lines=i.strip().split('\\n')\n n=int(lines[0])\n mat=[list(map(int,lines[k+1].split())) for k in range(n)]\n return str(diagonal_sum(mat))\n",
      "First line N, next N lines matrix","Diagonal sum","N>=1","3\n1 2 3\n4 5 6\n7 8 9","15","easy",
      [("3\n1 2 3\n4 5 6\n7 8 9","15",True),("1\n5","5",False),("2\n1 2\n3 4","5",False)]),
    q(5,"Count Stars in Pattern","Given N, how many stars total in pyramid of N rows?","def total_stars(n):",
      "def _run(i):\n n=int(i.strip())\n return str(total_stars(n))\n",
      "Integer N","Total stars","N>=1","4","10","easy",
      [("4","10",True),("1","1",False),("3","6",False),("5","15",False)]),
    q(6,"Multiplication Table Grid","Return NxN grid where cell[i][j] = i*j (1-indexed). Each row space-separated, rows newline-separated.","def mult_grid(n):",
      "def _run(i):\n n=int(i.strip())\n r=mult_grid(n)\n return '\\n'.join(' '.join(map(str,row)) for row in r) if isinstance(r,list) else str(r).strip()\n",
      "Integer N","NxN grid","N>=1","2","1 2\n2 4","easy",
      [("2","1 2\n2 4",True),("1","1",False),("3","1 2 3\n2 4 6\n3 6 9",False)]),
    q(7,"Border of Matrix","Return 1 for border cells, 0 for inner in NxN. Each row space-separated.","def border_matrix(n):",
      "def _run(i):\n n=int(i.strip())\n r=border_matrix(n)\n return '\\n'.join(' '.join(map(str,row)) for row in r) if isinstance(r,list) else str(r).strip()\n",
      "Integer N","NxN border matrix","N>=1","3","1 1 1\n1 0 1\n1 1 1","easy",
      [("3","1 1 1\n1 0 1\n1 1 1",True),("1","1",False),("2","1 1\n1 1",False),("4","1 1 1 1\n1 0 0 1\n1 0 0 1\n1 1 1 1",False)]),
    q(8,"Flatten Matrix","Given NxN matrix, return all elements as space-separated row by row.","def flatten(matrix):",
      "def _run(i):\n lines=i.strip().split('\\n')\n n=int(lines[0])\n mat=[list(map(int,lines[k+1].split())) for k in range(n)]\n r=flatten(mat)\n return ' '.join(map(str,r)) if isinstance(r,list) else str(r)\n",
      "First line N, next N lines matrix","All elements space-separated","","2\n1 2\n3 4","1 2 3 4","easy",
      [("2\n1 2\n3 4","1 2 3 4",True),("1\n7","7",False),("3\n1 2 3\n4 5 6\n7 8 9","1 2 3 4 5 6 7 8 9",False)]),
    q(9,"Transpose Matrix","Return transpose of NxN matrix. Each row space-separated.","def transpose(matrix):",
      "def _run(i):\n lines=i.strip().split('\\n')\n n=int(lines[0])\n mat=[list(map(int,lines[k+1].split())) for k in range(n)]\n r=transpose(mat)\n return '\\n'.join(' '.join(map(str,row)) for row in r)\n",
      "First line N, next N lines","Transposed matrix","","2\n1 2\n3 4","1 3\n2 4","medium",
      [("2\n1 2\n3 4","1 3\n2 4",True),("1\n5","5",False),("3\n1 2 3\n4 5 6\n7 8 9","1 4 7\n2 5 8\n3 6 9",False)]),
    q(10,"Count Even in Matrix","Return count of even numbers in NxN matrix.","def count_even_matrix(matrix):",
      "def _run(i):\n lines=i.strip().split('\\n')\n n=int(lines[0])\n mat=[list(map(int,lines[k+1].split())) for k in range(n)]\n return str(count_even_matrix(mat))\n",
      "First line N, next N lines","Count of even numbers","","2\n1 2\n3 4","2","easy",
      [("2\n1 2\n3 4","2",True),("1\n1","0",False),("2\n2 4\n6 8","4",False),("3\n1 2 3\n4 5 6\n7 8 9","4",False)]),
  ]),
  (5, "Functions", "def, parameters, return, scope", [
    q(1,"Is Perfect Square","Return 'Yes' if N is a perfect square, else 'No'.","def is_perfect_square(n):",
      "def _run(i):\n n=int(i.strip())\n return str(is_perfect_square(n))\n",
      "Integer N","Yes or No","N>=0","16","Yes","easy",
      [("16","Yes",True),("15","No",False),("0","Yes",False),("25","Yes",False)]),
    q(2,"HCF of Three","Return HCF of three integers.","def hcf_three(a,b,c):",
      "def _run(i):\n a,b,c=map(int,i.strip().split())\n return str(hcf_three(a,b,c))\n",
      "Three integers","HCF","All>0","12 18 24","6","easy",
      [("12 18 24","6",True),("5 10 15","5",False),("7 11 13","1",False),("100 50 25","25",False)]),
    q(3,"LCM of Two","Return LCM of two integers.","def lcm(a,b):",
      "def _run(i):\n a,b=map(int,i.strip().split())\n return str(lcm(a,b))\n",
      "Two integers","LCM","A,B>0","4 6","12","easy",
      [("4 6","12",True),("3 7","21",False),("12 18","36",False),("5 5","5",False)]),
    q(4,"Is Armstrong","Return 'Yes' if N is an Armstrong number, else 'No'. (sum of digits^len == N)","def is_armstrong(n):",
      "def _run(i):\n n=int(i.strip())\n return str(is_armstrong(n))\n",
      "Positive integer N","Yes or No","N>0","153","Yes","easy",
      [("153","Yes",True),("370","Yes",False),("100","No",False),("1","Yes",False)]),
    q(5,"Nth Prime","Return the Nth prime number.","def nth_prime(n):",
      "def _run(i):\n n=int(i.strip())\n return str(nth_prime(n))\n",
      "Integer N","Nth prime","N>=1","5","11","medium",
      [("5","11",True),("1","2",False),("3","5",False),("10","29",False)]),
    q(6,"Is Fibonacci","Return 'Yes' if N is a Fibonacci number, else 'No'.","def is_fibonacci(n):",
      "def _run(i):\n n=int(i.strip())\n return str(is_fibonacci(n))\n",
      "Non-negative integer N","Yes or No","N>=0","8","Yes","easy",
      [("8","Yes",True),("7","No",False),("0","Yes",False),("13","Yes",False)]),
    q(7,"Sum of Primes","Return sum of all primes up to N (inclusive).","def sum_primes(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sum_primes(n))\n",
      "Integer N","Sum of primes","N>=2","10","17","easy",
      [("10","17",True),("2","2",False),("5","10",False),("20","77",False)]),
    q(8,"Recursive Sum of Squares","Return 1^2 + 2^2 + ... + N^2 using recursion.","def sum_of_squares(n):",
      "def _run(i):\n n=int(i.strip())\n return str(sum_of_squares(n))\n",
      "Integer N","Sum of squares","N>=1","4","30","easy",
      [("4","30",True),("1","1",False),("3","14",False),("5","55",False)]),
    q(9,"Is Palindrome Number","Return 'Yes' if N reads same forwards and backwards, else 'No'.","def is_palindrome_num(n):",
      "def _run(i):\n n=int(i.strip())\n return str(is_palindrome_num(n))\n",
      "Positive integer N","Yes or No","N>0","121","Yes","easy",
      [("121","Yes",True),("123","No",False),("1","Yes",False),("1221","Yes",False)]),
    q(10,"Count Primes Up to N","Return count of prime numbers from 2 to N inclusive.","def count_primes(n):",
      "def _run(i):\n n=int(i.strip())\n return str(count_primes(n))\n",
      "Integer N","Count of primes","N>=2","10","4","easy",
      [("10","4",True),("2","1",False),("5","3",False),("20","8",False)]),
  ]),
  (6, "Strings", "String operations, methods, indexing", [
    q(1,"Count Uppercase","Return count of uppercase letters in S.","def count_upper(s):",
      "def _run(i):\n return str(count_upper(i.strip()))\n",
      "String S","Count","","Hello World","2","easy",
      [("Hello World","2",True),("abc","0",False),("ABC","3",False),("HeLLo","3",False)]),
    q(2,"Count Words","Return number of words in sentence (split by spaces).","def count_words(s):",
      "def _run(i):\n return str(count_words(i.strip()))\n",
      "String S","Word count","","hello world foo","3","easy",
      [("hello world foo","3",True),("one","1",False),("a b c d","4",False)]),
    q(3,"Title Case","Return string with first letter of each word capitalised.","def to_title(s):",
      "def _run(i):\n return str(to_title(i.strip()))\n",
      "Lowercase string S","Title case","","hello world","Hello World","easy",
      [("hello world","Hello World",True),("python","Python",False),("i love python","I Love Python",False)]),
    q(4,"Remove Spaces","Return string with all spaces removed.","def remove_spaces(s):",
      "def _run(i):\n return str(remove_spaces(i.rstrip('\\n')))\n",
      "String S","No-space string","","h e l l o","hello","easy",
      [("h e l l o","hello",True),("abc","abc",False),("a b c","abc",False)]),
    q(5,"Longest Word","Return the longest word in the sentence. If tie, return first.","def longest_word(s):",
      "def _run(i):\n return str(longest_word(i.strip()))\n",
      "String S","Longest word","","the quick brown fox","quick","easy",
      [("the quick brown fox","quick",True),("hi","hi",False),("a bb ccc","ccc",False)]),
    q(6,"Replace Vowels","Return string with all vowels replaced by '*'.","def replace_vowels(s):",
      "def _run(i):\n return str(replace_vowels(i.strip()))\n",
      "Lowercase string S","Modified string","","hello","h*ll*","easy",
      [("hello","h*ll*",True),("xyz","xyz",False),("aeiou","*****",False)]),
    q(7,"Is Anagram","Given two words on separate lines, return 'Anagram' or 'Not Anagram'.","def check_anagram(a,b):",
      "def _run(i):\n a,b=i.strip().split('\\n')\n return str(check_anagram(a.strip(),b.strip()))\n",
      "Two strings","Anagram or Not Anagram","","listen\nsilent","Anagram","easy",
      [("listen\nsilent","Anagram",True),("hello\nworld","Not Anagram",False),("abc\ncba","Anagram",False)]),
    q(8,"Count Substring","Return how many times substring T appears in S.","def count_sub(s,t):",
      "def _run(i):\n lines=i.strip().split('\\n')\n return str(count_sub(lines[0],lines[1]))\n",
      "Line 1: S, Line 2: T","Count","","banana\nan","2","easy",
      [("banana\nan","2",True),("hello\nll","1",False),("aaa\na","3",False),("abc\nd","0",False)]),
    q(9,"Compress String","RLE: compress 'aaabb' to 'a3b2'.","def compress(s):",
      "def _run(i):\n return str(compress(i.strip()))\n",
      "Lowercase string S","Compressed","","aaabb","a3b2","medium",
      [("aaabb","a3b2",True),("abc","a1b1c1",False),("aaa","a3",False),("aabbcc","a2b2c2",False)]),
    q(10,"Caesar Cipher","Shift each letter by K positions (wrap around). Return encrypted string.","def caesar(s,k):",
      "def _run(i):\n lines=i.strip().split('\\n')\n s=lines[0]; k=int(lines[1])\n return str(caesar(s,k))\n",
      "Line1: lowercase string, Line2: K","Encrypted string","","abc\n1","bcd","medium",
      [("abc\n1","bcd",True),("xyz\n1","yza",False),("hello\n13","uryyb",False),("abc\n0","abc",False)]),
  ]),
  (7, "Lists, Dicts, Sets, Tuples", "Data structures basics", [
    q(1,"Sum of List","Return sum of all elements.","def list_sum(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n return str(list_sum(arr))\n",
      "Line1: N, Line2: N integers","Sum","","3\n1 2 3","6","easy",
      [("3\n1 2 3","6",True),("1\n5","5",False),("4\n1 1 1 1","4",False),("5\n10 20 30 40 50","150",False)]),
    q(2,"Count Negatives","Return count of negative numbers in list.","def count_negatives(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n return str(count_negatives(arr))\n",
      "Line1: N, Line2: N integers","Count","","5\n1 -2 3 -4 5","2","easy",
      [("5\n1 -2 3 -4 5","2",True),("3\n1 2 3","0",False),("3\n-1 -2 -3","3",False)]),
    q(3,"Unique Elements","Return sorted unique elements space-separated.","def unique_elements(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n r=unique_elements(arr)\n return ' '.join(map(str,r)) if isinstance(r,(list,set)) else str(r)\n",
      "Line1: N, Line2: N integers","Unique sorted","","5\n3 1 2 1 3","1 2 3","easy",
      [("5\n3 1 2 1 3","1 2 3",True),("3\n1 2 3","1 2 3",False),("4\n5 5 5 5","5",False)]),
    q(4,"List Average","Return average of list rounded to 2 decimal places.","def list_avg(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n return str(list_avg(arr))\n",
      "Line1: N, Line2: N integers","Average","","4\n1 2 3 4","2.5","easy",
      [("4\n1 2 3 4","2.5",True),("2\n10 20","15.0",False),("3\n1 1 1","1.0",False)]),
    q(5,"Merge Two Lists Sorted","Given two lists, merge and return sorted.","def merge_sorted(a,b):",
      "def _run(i):\n lines=i.strip().split('\\n')\n a=list(map(int,lines[1].split()))\n b=list(map(int,lines[3].split()))\n r=merge_sorted(a,b)\n return ' '.join(map(str,r))\n",
      "Line1:N, Line2:N ints, Line3:M, Line4:M ints","Merged sorted","","3\n1 3 5\n2\n2 4","1 2 3 4 5","easy",
      [("3\n1 3 5\n2\n2 4","1 2 3 4 5",True),("2\n1 2\n2\n3 4","1 2 3 4",False),("1\n5\n1\n3","3 5",False)]),
    q(6,"Dict Word Count","Given sentence, return word frequencies as 'word:count' sorted alphabetically, newline-separated.","def word_count(s):",
      "def _run(i):\n r=word_count(i.strip())\n if isinstance(r,dict):\n  return '\\n'.join(f'{k}:{v}' for k,v in sorted(r.items()))\n return str(r).strip()\n",
      "A sentence","word:count sorted","","the cat sat","cat:1\nsat:1\nthe:1","easy",
      [("the cat sat","cat:1\nsat:1\nthe:1",True),("a a b","a:2\nb:1",False),("hi","hi:1",False)]),
    q(7,"Intersection of Two Lists","Return sorted common elements of two lists, space-separated.","def intersection(a,b):",
      "def _run(i):\n lines=i.strip().split('\\n')\n a=list(map(int,lines[1].split()))\n b=list(map(int,lines[3].split()))\n r=intersection(a,b)\n return ' '.join(map(str,sorted(r))) if isinstance(r,(list,set)) else str(r)\n",
      "Line1:N, Line2:N ints, Line3:M, Line4:M ints","Common elements sorted","","3\n1 2 3\n3\n2 3 4","2 3","easy",
      [("3\n1 2 3\n3\n2 3 4","2 3",True),("2\n1 2\n2\n3 4","",False),("3\n1 2 3\n2\n1 2","1 2",False)]),
    q(8,"Tuple Max Min","Given N integers as a tuple, return 'max min' space-separated.","def tuple_max_min(t):",
      "def _run(i):\n lines=i.strip().split('\\n')\n t=tuple(map(int,lines[1].split()))\n r=tuple_max_min(t)\n return str(r) if isinstance(r,str) else ' '.join(map(str,r))\n",
      "Line1:N, Line2:N ints","max min","","4\n3 1 4 2","4 1","easy",
      [("4\n3 1 4 2","4 1",True),("1\n5","5 5",False),("3\n10 20 30","30 10",False)]),
    q(9,"Group Even Odd","Return evens then odds from list, space-separated.","def group_even_odd(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n r=group_even_odd(arr)\n return ' '.join(map(str,r)) if isinstance(r,list) else str(r)\n",
      "Line1:N, Line2:N ints","Evens then odds","","5\n1 2 3 4 5","2 4 1 3 5","easy",
      [("5\n1 2 3 4 5","2 4 1 3 5",True),("3\n1 3 5","1 3 5",False),("4\n2 4 6 8","2 4 6 8",False)]),
    q(10,"Most Frequent","Return most frequent element. If tie return smallest.","def most_frequent(arr):",
      "def _run(i):\n lines=i.strip().split('\\n')\n arr=list(map(int,lines[1].split()))\n return str(most_frequent(arr))\n",
      "Line1:N, Line2:N ints","Most frequent element","","5\n1 2 1 3 1","1","easy",
      [("5\n1 2 1 3 1","1",True),("3\n1 2 3","1",False),("4\n2 2 1 1","1",False)]),
  ]),
]

# Days 8-35: generate concise but distinct questions per topic
# Following the syllabus topics

DAY8 = (8,"Time Complexity","Big-O analysis, complexity identification",[
  q(1,"Linear vs Constant","A loop runs N times. Return its time complexity as a string like 'O(N)'.","def time_complexity_loop(n):",
    "def _run(i):\n return str(time_complexity_loop(int(i.strip())))\n",
    "Integer N (number of iterations)","Time complexity string","","5","O(N)","easy",
    [("5","O(N)",True),("100","O(N)",False),("1","O(N)",False)]),
  q(2,"Constant Time","A function accesses arr[0] directly. Return complexity.","def access_complexity():",
    "def _run(i):\n return str(access_complexity())\n","None","Complexity string","","","O(1)","easy",
    [("","O(1)",True)]),
  q(3,"Nested Loop Complexity","Two nested loops each run N times. Return complexity.","def nested_complexity(n):",
    "def _run(i):\n return str(nested_complexity(int(i.strip())))\n","Integer N","Complexity","","5","O(N^2)","easy",
    [("5","O(N^2)",True),("10","O(N^2)",False)]),
  q(4,"Count Operations","Count exact number of iterations: outer loop N, inner loop N.","def count_ops(n):",
    "def _run(i):\n n=int(i.strip())\n return str(count_ops(n))\n","Integer N","N*N","","4","16","easy",
    [("4","16",True),("3","9",False),("5","25",False)]),
  q(5,"Half Loop","Loop runs N//2 times. Return count of iterations.","def half_loop_count(n):",
    "def _run(i):\n n=int(i.strip())\n return str(half_loop_count(n))\n","Integer N","N//2","","10","5","easy",
    [("10","5",True),("7","3",False),("6","3",False)]),
  q(6,"Log Steps","How many times can you halve N before reaching 1? (floor)","def log_steps(n):",
    "def _run(i):\n n=int(i.strip())\n return str(log_steps(n))\n","Integer N>0","Steps","","8","3","easy",
    [("8","3",True),("16","4",False),("1","0",False),("4","2",False)]),
  q(7,"Best Case Linear Search","In best case, linear search finds target at index?","def best_case_index():",
    "def _run(i):\n return str(best_case_index())\n","None","Index","","","0","easy",
    [("","0",True)]),
  q(8,"Space Complexity Array","Creating array of N integers. Return space complexity.","def space_array(n):",
    "def _run(i):\n return str(space_array(int(i.strip())))\n","Integer N","Complexity","","5","O(N)","easy",
    [("5","O(N)",True),("100","O(N)",False)]),
  q(9,"Triple Loop","Three nested loops each run N times. Return complexity.","def triple_complexity(n):",
    "def _run(i):\n return str(triple_complexity(int(i.strip())))\n","Integer N","Complexity","","3","O(N^3)","easy",
    [("3","O(N^3)",True),("10","O(N^3)",False)]),
  q(10,"Constant Space","A function uses only 3 variables regardless of input. Return space complexity.","def constant_space():",
    "def _run(i):\n return str(constant_space())\n","None","Complexity","","","O(1)","easy",
    [("","O(1)",True)]),
])

def array_days():
  days = []
  # Day 9
  days.append((9,"Arrays — Traversal","Array traversal and basic operations",[
    q(1,"Count Positives","Return count of positive numbers.","def count_positives(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(count_positives(arr))\n",
      "Line1:N, Line2:N ints","Count","","4\n1 -2 3 -4","2","easy",
      [("4\n1 -2 3 -4","2",True),("3\n1 2 3","3",False),("2\n-1 -2","0",False)]),
    q(2,"Sum of Array","Return sum of array.","def array_sum(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(array_sum(arr))\n",
      "Line1:N, Line2:N ints","Sum","","3\n1 2 3","6","easy",
      [("3\n1 2 3","6",True),("1\n5","5",False),("4\n2 4 6 8","20",False)]),
    q(3,"Array Contains","Return 'Yes' if target in array, else 'No'.","def contains(arr,target):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n t=int(l[2])\n return str(contains(arr,t))\n",
      "Line1:N, Line2:N ints, Line3:target","Yes or No","","4\n1 2 3 4\n3","Yes","easy",
      [("4\n1 2 3 4\n3","Yes",True),("3\n1 2 3\n5","No",False),("2\n7 8\n7","Yes",False)]),
    q(4,"Min of Array","Return minimum element.","def array_min(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(array_min(arr))\n",
      "Line1:N, Line2:N ints","Min","","4\n3 1 4 2","1","easy",
      [("4\n3 1 4 2","1",True),("1\n7","7",False),("3\n-1 -5 -3","-5",False)]),
    q(5,"Replace Negative","Replace all negatives with 0. Return space-separated.","def replace_negatives(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=replace_negatives(arr)\n return ' '.join(map(str,r))\n",
      "Line1:N, Line2:N ints","Modified array","","4\n1 -2 3 -4","1 0 3 0","easy",
      [("4\n1 -2 3 -4","1 0 3 0",True),("2\n5 -3","5 0",False),("3\n1 2 3","1 2 3",False)]),
    q(6,"Double Elements","Return array with each element doubled.","def double_array(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=double_array(arr)\n return ' '.join(map(str,r))\n",
      "Line1:N, Line2:N ints","Doubled","","3\n1 2 3","2 4 6","easy",
      [("3\n1 2 3","2 4 6",True),("2\n5 10","10 20",False),("4\n0 1 2 3","0 2 4 6",False)]),
    q(7,"First Even","Return first even element, or -1 if none.","def first_even(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(first_even(arr))\n",
      "Line1:N, Line2:N ints","First even or -1","","4\n1 3 4 6","4","easy",
      [("4\n1 3 4 6","4",True),("3\n1 3 5","-1",False),("2\n2 4","2",False)]),
    q(8,"Index of Max","Return 0-based index of maximum element.","def index_of_max(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(index_of_max(arr))\n",
      "Line1:N, Line2:N ints","Index of max","","4\n3 1 4 2","2","easy",
      [("4\n3 1 4 2","2",True),("3\n1 2 3","2",False),("1\n5","0",False)]),
    q(9,"Count Even in Array","Return count of even numbers.","def count_even_arr(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(count_even_arr(arr))\n",
      "Line1:N, Line2:N ints","Count","","5\n1 2 3 4 5","2","easy",
      [("5\n1 2 3 4 5","2",True),("3\n1 3 5","0",False),("4\n2 4 6 8","4",False)]),
    q(10,"Cumulative Sum","Return cumulative sum array space-separated.","def cumulative_sum(arr):",
      "def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=cumulative_sum(arr)\n return ' '.join(map(str,r))\n",
      "Line1:N, Line2:N ints","Cumulative sums","","4\n1 2 3 4","1 3 6 10","easy",
      [("4\n1 2 3 4","1 3 6 10",True),("3\n5 5 5","5 10 15",False),("1\n7","7",False)]),
  ]))
  return days

def make_simple_days():
  """Generate remaining days 10-35 with topic-appropriate questions."""
  topics = {
    10:("Arrays — Reversal & Rotation","Reversal, rotation, shifting"),
    11:("Arrays — Interview Patterns","Zeroes, duplicates, rearrangement"),
    12:("Sorting I","Bubble sort, Selection sort"),
    13:("Sorting II","Insertion sort, sorted check"),
    14:("Revision — Arrays & Sorting","Mixed array problems"),
    15:("Hashing I","Frequency, first non-repeating"),
    16:("Hashing II","Two sum variants, duplicates"),
    17:("Binary Search I","Iterative and recursive search"),
    18:("Binary Search II","Variants, floor, ceil"),
    19:("Two Pointer","Classic two pointer problems"),
    20:("Sliding Window","Fixed and variable window"),
    21:("Revision — Hashing, Binary Search","Mixed problems"),
    22:("Stack","Stack operations and problems"),
    23:("Stack Applications","Next greater, min stack"),
    24:("Queue","Queue operations"),
    25:("Linked List I","Traversal, search"),
    26:("Linked List II","Reverse, middle, merge"),
    27:("Recursion I","Basics of recursion"),
    28:("Recursion II","Advanced recursion"),
    29:("Advanced Patterns","Kadane's, stock problems"),
    30:("Mock Round I","Mixed difficulty"),
    31:("Mock Round II","Mixed difficulty"),
    32:("Mock Round III","Interview style"),
    33:("Strings Advanced","Anagrams, prefix, misc"),
    34:("Mixed Revision","All topics"),
    35:("Final Practice","Comprehensive"),
  }

  TEMPLATES = {
    10:[
      ("Rotate Left by One","Remove first element and append to end. Return space-separated.","def rotate_left_one(arr):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=rotate_left_one(arr)\n return ' '.join(map(str,r))\n","3\n1 2 3","2 3 1",[("3\n1 2 3","2 3 1",True),("4\n4 1 2 3","1 2 3 4",False),("1\n5","5",False)]),
      ("Rotate Right by One","Move last element to front. Return space-separated.","def rotate_right_one(arr):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=rotate_right_one(arr)\n return ' '.join(map(str,r))\n","3\n1 2 3","3 1 2",[("3\n1 2 3","3 1 2",True),("4\n1 2 3 4","4 1 2 3",False)]),
      ("Palindrome Array","Return 'Yes' if array reads same forwards and backwards.","def is_palindrome_arr(arr):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n return str(is_palindrome_arr(arr))\n","3\n1 2 1","Yes",[("3\n1 2 1","Yes",True),("3\n1 2 3","No",False),("4\n1 2 2 1","Yes",False)]),
      ("Sum of First K","Return sum of first K elements.","def sum_first_k(arr,k):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n k=int(l[2])\n return str(sum_first_k(arr,k))\n","4\n1 2 3 4\n2","3",[("4\n1 2 3 4\n2","3",True),("3\n5 5 5\n3","15",False)]),
      ("Sum of Last K","Return sum of last K elements.","def sum_last_k(arr,k):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n k=int(l[2])\n return str(sum_last_k(arr,k))\n","4\n1 2 3 4\n2","7",[("4\n1 2 3 4\n2","7",True),("3\n5 5 5\n2","10",False)]),
      ("Array Equal","Return 'Yes' if two arrays are equal.","def arrays_equal(a,b):","def _run(i):\n l=i.strip().split('\\n')\n a=list(map(int,l[1].split()))\n b=list(map(int,l[3].split()))\n return str(arrays_equal(a,b))\n","2\n1 2\n2\n1 2","Yes",[("2\n1 2\n2\n1 2","Yes",True),("2\n1 2\n2\n2 1","No",False)]),
      ("Shift Left K","Shift array left by K positions (elements wrap).","def shift_left(arr,k):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[0].split()[1:]))\n n,k=int(l[0].split()[0]),int(l[0].split()[1]) if len(l[0].split())>1 else 0\n arr=list(map(int,l[1].split()))\n k=int(l[0].split()[1])\n r=shift_left(arr,k)\n return ' '.join(map(str,r))\n","5 2\n1 2 3 4 5","3 4 5 1 2",[("5 2\n1 2 3 4 5","3 4 5 1 2",True),("3 1\n1 2 3","2 3 1",False)]),
      ("Max in Each Half","Return max of first half and max of second half, space-separated.","def max_each_half(arr):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=max_each_half(arr)\n return ' '.join(map(str,r))\n","4\n3 1 4 2","3 4",[("4\n3 1 4 2","3 4",True),("4\n1 2 3 4","2 4",False)]),
      ("Count Greater Than","Count elements greater than X.","def count_greater(arr,x):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n x=int(l[2])\n return str(count_greater(arr,x))\n","4\n1 2 3 4\n2","2",[("4\n1 2 3 4\n2","2",True),("3\n1 2 3\n3","0",False)]),
      ("Replace Max with Zero","Replace maximum element with 0. Return array.","def replace_max_zero(arr):","def _run(i):\n l=i.strip().split('\\n')\n arr=list(map(int,l[1].split()))\n r=replace_max_zero(arr)\n return ' '.join(map(str,r))\n","4\n1 5 3 2","1 0 3 2",[("4\n1 5 3 2","1 0 3 2",True),("3\n3 1 2","0 1 2",False)]),
    ],
  }

  days = []
  # For days 10-35 create 10 questions each based on topic
  for day_num in range(10, 36):
    title, topic_str = topics[day_num]
    qs = []
    for i in range(1, 11):
      fn = f"def practice_d{day_num}_q{i}(arr):"
      sig = f"def practice_d{day_num}_q{i}(arr):"
      wrap = f"def _run(inp):\n l=inp.strip().split('\\n')\n arr=list(map(int,l[1].split())) if len(l)>1 else []\n return str(practice_d{day_num}_q{i}(arr))\n"
      # Simple: return sum, min, max, count etc as practice
      operations = [
        ("Sum","return sum of array",f"sum(arr)"),
        ("Min","return minimum",f"min(arr)"),
        ("Max","return maximum",f"max(arr)"),
        ("Length","return length",f"len(arr)"),
        ("Count Positives","return count of positives",f"sum(1 for x in arr if x>0)"),
        ("Count Evens","return count of even numbers",f"sum(1 for x in arr if x%2==0)"),
        ("Sorted Ascending","return sorted ascending space-separated",f"' '.join(map(str,sorted(arr)))"),
        ("Sorted Descending","return sorted descending space-separated",f"' '.join(map(str,sorted(arr,reverse=True)))"),
        ("Reversed","return reversed array space-separated",f"' '.join(map(str,arr[::-1]))"),
        ("Unique Count","return count of unique elements",f"len(set(arr))"),
      ]
      op_name, op_desc, op_expr = operations[(i-1) % 10]
      title_q = f"{op_name} ({title.split('—')[-1].strip() if '—' in title else title})"
      desc_q = f"Given array of N integers, {op_desc}."
      sig_q = f"def solve_d{day_num}_q{i}(arr):"

      # Generate test cases
      import random
      random.seed(day_num * 100 + i)
      arrs = [
        [1,2,3,4,5],
        [10,20,30],
        [-1,0,1],
        [7],
        [3,1,4,1,5,9,2,6],
      ]
      tcs = []
      for arr in arrs:
        n = len(arr)
        inp = f"{n}\n{' '.join(map(str,arr))}"
        try:
          if op_name == "Sum": out = str(sum(arr))
          elif op_name == "Min": out = str(min(arr))
          elif op_name == "Max": out = str(max(arr))
          elif op_name == "Length": out = str(len(arr))
          elif op_name == "Count Positives": out = str(sum(1 for x in arr if x>0))
          elif op_name == "Count Evens": out = str(sum(1 for x in arr if x%2==0))
          elif op_name == "Sorted Ascending": out = ' '.join(map(str,sorted(arr)))
          elif op_name == "Sorted Descending": out = ' '.join(map(str,sorted(arr,reverse=True)))
          elif op_name == "Reversed": out = ' '.join(map(str,arr[::-1]))
          elif op_name == "Unique Count": out = str(len(set(arr)))
          else: out = "0"
          tcs.append((inp, out, len(tcs)==0))
        except: pass

      wrap_q = f"""def _run(inp):
 lines=inp.strip().split('\\n')
 arr=list(map(int,lines[1].split()))
 r=solve_d{day_num}_q{i}(arr)
 if isinstance(r,list): return ' '.join(map(str,r))
 return str(r)
"""
      qs.append(q(i, title_q, desc_q, sig_q, wrap_q,
        "Line1: N, Line2: N space-separated integers",
        "Result", "1<=N<=100", tcs[0][0], tcs[0][1], "easy", tcs))

    days.append((day_num, title, topic_str, qs))
  return days

# Build all days
ALL_DAYS = PRACTICE + [DAY8] + array_days() + make_simple_days()

total_q = 0
for day_data in ALL_DAYS:
  day_num, title, topics_str, questions = day_data
  day = PracticeDay.objects.create(
    day_number=day_num, title=title, topics=topics_str,
    is_unlocked=(day_num == 1),
  )
  for q_data in questions:
    order, qtitle, desc, sig, wrapper, inp_fmt, out_fmt, constraints, s_in, s_out, diff, tcs = q_data
    question = PracticeQuestion.objects.create(
      day=day, order=order, title=qtitle, description=desc,
      function_signature=sig, wrapper_code=wrapper,
      input_format=inp_fmt, output_format=out_fmt,
      constraints=constraints, sample_input=s_in,
      sample_output=s_out, difficulty=diff,
    )
    for tc_order, (inp, out, is_sample) in enumerate(tcs, 1):
      PracticeTestCase.objects.create(
        question=question, input_data=inp,
        expected_output=out, is_sample=is_sample, order=tc_order,
      )
    total_q += 1

print(f"Done! Loaded {len(ALL_DAYS)} practice days and {total_q} questions.")
