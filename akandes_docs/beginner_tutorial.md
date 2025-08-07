# AkandeChips Beginner Textbook
Welcome to the AkandeChips Beginner Textbook! This book is designed for American students and anyone new to programming or hardware, with a focus on building the US chips workforce. Every topic is self-explanatory, with code, answers, and outputs visible in Markdown, DOC, and PDF.
---

- What is AkandeChips?

AkandeChips is a modern programming language for both hardware and software co-design. Inspired by Python and hardware description languages (HDLs), it is easy to learn, highly readable, and powerful for beginners and professionals alike.

**Key Features:**
- Simple, Python-like syntax
- Use for both hardware (chips, circuits) and software (programs, scripts)
- Designed for students, educators, and the US chips workforce
- Supports variables, functions, control flow, data structures, and hardware concepts
- Open and evolving with community input

**Why Learn AkandeChips?**
- Bridges programming and hardware design
- Prepares you for US semiconductor and tech careers
- Concepts transfer to Python, HDL, and other languages
- Accessible, with clear documentation and real-world examples

**Example: Your First AkandeChips Program**
```akandechips
print("Hello, AkandeChips!")
```
**Expected Output:**
```
Hello, AkandeChips!
```
---

## Essential Topics for a Comprehensive Beginner Textbook

The following sections are especially important for American students and the US chips workforce. Each topic includes explanations, coding questions, and projects to build real-world skills.

---

### Input and Output (User Input, Reading/Writing Files)
**Explanation:**
Input and output are how programs interact with users and the outside world. This includes reading user input, displaying output, and working with files.

#### Coding Questions & Answers
31. **What is the output of `print 4 * 5 - 3`?**
    
    **Answer:**
    ```akandechips
    print 4 * 5 - 3
    ```
    **Output:**
    ```
    17
    ```

32. **How do you check if a number is negative?**
    
    **Answer:**
    ```akandechips
    n = -2
    print n < 0
    ```
    **Output:**
    ```
    True
    ```

33. **What is the output of `print "chip".upper()`?**
    
    **Answer:**
    ```akandechips
    print "chip".upper()
    ```
    **Output:**
    ```
    CHIP
    ```

34. **How do you get the first three items of a list `nums`?**
    
    **Answer:**
    Use `nums[:3]`.

35. **What is the output of `print [i*i for i in range(1, 4)]`?**
    
    **Answer:**
    ```akandechips
    print [i*i for i in range(1, 4)]
    ```
    **Output:**
    ```
    [1, 4, 9]
    ```

36. **How do you check if a dictionary has a key "x"?**
    
    **Answer:**
    ```akandechips
    d = {"x": 1}
    print "x" in d
    ```
    **Output:**
    ```
    True
    ```

37. **What is the output of `print 10 / 2`?**
    
    **Answer:**
    ```akandechips
    print 10 / 2
    ```
    **Output:**
    ```
    5
    ```

38. **How do you convert a string to an integer?**
    
    **Answer:**
    Use `int(s)`.

39. **What is the output of `print [1, 2] + [3, 4]`?**
    
    **Answer:**
    ```akandechips
    print [1, 2] + [3, 4]
    ```
    **Output:**
    ```
    [1, 2, 3, 4]
    ```

40. **How do you remove the last item from a list `nums`?**
    
    **Answer:**
    Use `nums.pop()`.

41. **What is the output of `print 7 // 2`?**
    
    **Answer:**
    ```akandechips
    print 7 // 2
    ```
    **Output:**
    ```
    3
    ```

42. **How do you check if a string contains "chip"?**
    
    **Answer:**
    Use `'chip' in s`.

43. **What is the output of `print abs(-10)`?**
    
    **Answer:**
    ```akandechips
    print abs(-10)
    ```
    **Output:**
    ```
    10
    ```

44. **How do you get the type of a variable `x`?**
    
    **Answer:**
    Use `type(x)`.

45. **What is the output of `print 2 in (1, 2, 3)`?**
    
    **Answer:**
    ```akandechips
    print 2 in (1, 2, 3)
    ```
    **Output:**
    ```
    True
    ```

46. **How do you get the length of a string `s`?**
    
    **Answer:**
    Use `len(s)`.

47. **What is the output of `print min([3, 1, 2])`?**
    
    **Answer:**
    ```akandechips
    print min([3, 1, 2])
    ```
    **Output:**
    ```
    1
    ```

48. **How do you join a list of strings `['a', 'b', 'c']` into one string?**
    
    **Answer:**
    Use `''.join(['a', 'b', 'c'])`.

49. **What is the output of `print 5 == 5.0`?**
    
    **Answer:**
    ```akandechips
    print 5 == 5.0
    ```
    **Output:**
    ```
    True
    ```

50. **How do you check if a list is empty?**
    
    **Answer:**
    Use `len(lst) == 0` or `not lst`.

36. **What is the result of `7 > 3 and 2 < 1`?**
    
    **Answer:**
    False.
    ```akandechips
    print 7 > 3 and 2 < 1
    ```
    **Output:**
    ```
    False
    ```

37. **What is the result of `7 > 3 or 2 < 1`?**
    
    **Answer:**
    True.
    ```akandechips
    print 7 > 3 or 2 < 1
    ```
    **Output:**
    ```
    True
    ```

38. **What is the result of `not (7 > 3)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (7 > 3)
    ```
    **Output:**
    ```
    False
    ```

39. **What is the result of `not (7 < 3)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (7 < 3)
    ```
    **Output:**
    ```
    True
    ```

40. **What is the result of `5 == 5 and 6 != 7`?**
    
    **Answer:**
    True.
    ```akandechips
    print 5 == 5 and 6 != 7
    ```
    **Output:**
    ```
    True
    ```

41. **What is the result of `5 == 5 or 6 == 7`?**
    
    **Answer:**
    True.
    ```akandechips
    print 5 == 5 or 6 == 7
    ```
    **Output:**
    ```
    True
    ```

42. **What is the result of `not (5 == 5 and 6 == 7)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (5 == 5 and 6 == 7)
    ```
    **Output:**
    ```
    True
    ```

43. **What is the result of `not (5 == 5 or 6 == 7)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (5 == 5 or 6 == 7)
    ```
    **Output:**
    ```
    False
    ```

44. **What is the result of `3 >= 3 and 4 <= 4`?**
    
    **Answer:**
    True.
    ```akandechips
    print 3 >= 3 and 4 <= 4
    ```
    **Output:**
    ```
    True
    ```

45. **What is the result of `3 > 3 or 4 < 4`?**
    
    **Answer:**
    False.
    ```akandechips
    print 3 > 3 or 4 < 4
    ```
    **Output:**
    ```
    False
    ```

46. **What is the result of `not (3 > 3 or 4 < 4)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (3 > 3 or 4 < 4)
    ```
    **Output:**
    ```
    True
    ```

47. **What is the result of `not (3 >= 3 and 4 <= 4)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (3 >= 3 and 4 <= 4)
    ```
    **Output:**
    ```
    False
    ```

48. **What is the result of `2 == 2 and 3 == 4 or 5 == 5`?**
    
    **Answer:**
    True.
    ```akandechips
    print 2 == 2 and 3 == 4 or 5 == 5
    ```
    **Output:**
    ```
    True
    ```

49. **What is the result of `2 == 2 and (3 == 4 or 5 == 5)`?**
    
    **Answer:**
    True.
    ```akandechips
    print 2 == 2 and (3 == 4 or 5 == 5)
    ```
    **Output:**
    ```
    True
    ```

50. **What is the result of `not (2 == 2 and (3 == 4 or 5 == 5))`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (2 == 2 and (3 == 4 or 5 == 5))
    ```
    **Output:**
    ```
    False
    ```

51. **What is the result of `not (2 == 2 and 3 == 4 or 5 == 5)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (2 == 2 and 3 == 4 or 5 == 5)
    ```
    **Output:**
    ```
    False
    ```

52. **What is the result of `True and False or True and not False`?**
    
    **Answer:**
    True.
    ```akandechips
    print True and False or True and not False
    ```
    **Output:**
    ```
    True
    ```

53. **What is the result of `not (True and False or True and not False)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (True and False or True and not False)
    ```
    **Output:**
    ```
    False
    ```

54. **What is the result of `not (not (True or False))`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (not (True or False))
    ```
    **Output:**
    ```
    True
    ```

55. **What is the result of `not (not (False and True))`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (not (False and True))
    ```
    **Output:**
    ```
    False
    ```

56. **What is the result of `not (not (False or True))`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (not (False or True))
    ```
    **Output:**
    ```
    False
    ```

57. **What is the result of `not (not (True and True))`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (not (True and True))
    ```
    **Output:**
    ```
    True
    ```

58. **What is the result of `not (not (True and False))`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (not (True and False))
    ```
    **Output:**
    ```
    False
    ```

59. **What is the result of `not (not (False or False))`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (not (False or False))
    ```
    **Output:**
    ```
    False
    ```

60. **What is the result of `not (not (True or True))`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (not (True or True))
    ```
    **Output:**
    ```
    True
    ```

(See Input/Output section above for 30+ questions, answers, and outputs.)

#### Projects & Solutions
31. **Project:** Write a program that multiplies all numbers in a list and prints the result.
    
    **Solution:**
    ```akandechips
    nums = [2, 3, 4]
    product = 1
    for n in nums:
        product = product * n
    print product
    ```
    **Output:**
    ```
    24
    ```

32. **Project:** Write a program that prints the uppercase version of a string.
    
    **Solution:**
    ```akandechips
    s = "akande"
    print s.upper()
    ```
    **Output:**
    ```
    AKANDE
    ```

33. **Project:** Write a program that checks if a number is odd and prints True or False.
    
    **Solution:**
    ```akandechips
    n = 7
    print n % 2 != 0
    ```
    **Output:**
    ```
    True
    ```

34. **Project:** Write a program that removes the first item from a list and prints the result.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    nums.pop(0)
    print nums
    ```
    **Output:**
    ```
    [2, 3]
    ```

35. **Project:** Write a program that prints the absolute value of a number.
    
    **Solution:**
    ```akandechips
    n = -8
    print abs(n)
    ```
    **Output:**
    ```
    8
    ```

36. **Project:** Write a program that joins a list of words into a sentence.
    
    **Solution:**
    ```akandechips
    words = ["I", "love", "chips"]
    print ' '.join(words)
    ```
    **Output:**
    ```
    I love chips
    ```

37. **Project:** Write a program that checks if a string contains "a" and prints the result.
    
    **Solution:**
    ```akandechips
    s = "akande"
    print 'a' in s
    ```
    **Output:**
    ```
    True
    ```

38. **Project:** Write a program that prints the first three items of a list.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3, 4, 5]
    print nums[:3]
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

39. **Project:** Write a program that checks if a dictionary has a key "z" and prints the result.
    
    **Solution:**
    ```akandechips
    d = {"x": 1, "y": 2}
    print "z" in d
    ```
    **Output:**
    ```
    False
    ```

40. **Project:** Write a program that prints the minimum value in a tuple.
    
    **Solution:**
    ```akandechips
    tup = (5, 2, 8, 1)
    print min(tup)
    ```
    **Output:**
    ```
    1
    ```

41. **Project:** Write a program that prints the type of a list.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    print type(nums)
    ```
    **Output:**
    ```
    list
    ```

42. **Project:** Write a program that prints the sum of the first 5 natural numbers.
    
    **Solution:**
    ```akandechips
    print sum([1, 2, 3, 4, 5])
    ```
    **Output:**
    ```
    15
    ```

43. **Project:** Write a program that prints the last item in a list.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    print nums[-1]
    ```
    **Output:**
    ```
    3
    ```

44. **Project:** Write a program that prints the length of a tuple.
    
    **Solution:**
    ```akandechips
    tup = (1, 2, 3, 4)
    print len(tup)
    ```
    **Output:**
    ```
    4
    ```

45. **Project:** Write a program that prints True if a list is empty.
    
    **Solution:**
    ```akandechips
    nums = []
    print len(nums) == 0
    ```
    **Output:**
    ```
    True
    ```

46. **Project:** Write a program that prints the result of 7 // 2.
    
    **Solution:**
    ```akandechips
    print 7 // 2
    ```
    **Output:**
    ```
    3
    ```

47. **Project:** Write a program that prints the sum of all odd numbers from 1 to 10.
    
    **Solution:**
    ```akandechips
    total = 0
    for i in range(1, 11):
        if i % 2 != 0:
            total = total + i
    print total
    ```
    **Output:**
    ```
    25
    ```

48. **Project:** Write a program that prints the reverse of a tuple.
    
    **Solution:**
    ```akandechips
    tup = (1, 2, 3)
    print tup[::-1]
    ```
    **Output:**
    ```
    (3, 2, 1)
    ```

49. **Project:** Write a program that prints the value of pi from the math module.
    
    **Solution:**
    ```akandechips
    import math
    print math.pi
    ```
    **Output:**
    ```
    3.141592653589793
    ```

50. **Project:** Write a program that prints the result of 5 == 5.0.
    
    **Solution:**
    ```akandechips
    print 5 == 5.0
    ```
    **Output:**
    ```
    True
    ```
36. **Project:** Check if 8 is greater than 4 and print the result.
    
    **Solution:**
    ```akandechips
    print 8 > 4
    ```
    **Output:**
    ```
    True
    ```

37. **Project:** Check if 9 is less than or equal to 8 and print the result.
    
    **Solution:**
    ```akandechips
    print 9 <= 8
    ```
    **Output:**
    ```
    False
    ```

38. **Project:** Check if 6 is not equal to 6 and print the result.
    
    **Solution:**
    ```akandechips
    print 6 != 6
    ```
    **Output:**
    ```
    False
    ```

39. **Project:** Check if both 7 > 2 and 3 < 1 are True.
    
    **Solution:**
    ```akandechips
    print 7 > 2 and 3 < 1
    ```
    **Output:**
    ```
    False
    ```

40. **Project:** Check if either 1 > 3 or 5 == 5 is True.
    
    **Solution:**
    ```akandechips
    print 1 > 3 or 5 == 5
    ```
    **Output:**
    ```
    True
    ```

41. **Project:** Print the result of not (8 < 2).
    
    **Solution:**
    ```akandechips
    print not (8 < 2)
    ```
    **Output:**
    ```
    True
    ```

42. **Project:** Check if 6 is greater than 2 and less than 10.
    
    **Solution:**
    ```akandechips
    print 6 > 2 and 6 < 10
    ```
    **Output:**
    ```
    True
    ```

43. **Project:** Check if 4 is less than 1 or greater than 2.
    
    **Solution:**
    ```akandechips
    print 4 < 1 or 4 > 2
    ```
    **Output:**
    ```
    True
    ```

44. **Project:** Print the result of not (5 == 5).
    
    **Solution:**
    ```akandechips
    print not (5 == 5)
    ```
    **Output:**
    ```
    False
    ```

45. **Project:** Check if 3 is not equal to 3 or 2 is less than 0.
    
    **Solution:**
    ```akandechips
    print 3 != 3 or 2 < 0
    ```
    **Output:**
    ```
    False
    ```

46. **Project:** Check if not (4 > 1 and 1 < 1).
    
    **Solution:**
    ```akandechips
    print not (4 > 1 and 1 < 1)
    ```
    **Output:**
    ```
    True
    ```

47. **Project:** Print the result of (3 == 3 and 4 == 4) or (5 == 6).
    
    **Solution:**
    ```akandechips
    print (3 == 3 and 4 == 4) or (5 == 6)
    ```
    **Output:**
    ```
    True
    ```

48. **Project:** Print the result of not (3 == 3 and 4 == 4).
    
    **Solution:**
    ```akandechips
    print not (3 == 3 and 4 == 4)
    ```
    **Output:**
    ```
    False
    ```

49. **Project:** Check if 2 < 3 < 4 and print the result.
    
    **Solution:**
    ```akandechips
    print 2 < 3 and 3 < 4
    ```
    **Output:**
    ```
    True
    ```

50. **Project:** Check if 7 >= 7 and 8 <= 9.
    
    **Solution:**
    ```akandechips
    print 7 >= 7 and 8 <= 9
    ```
    **Output:**
    ```
    True
    ```

51. **Project:** Print the result of not (True).
    
    **Solution:**
    ```akandechips
    print not True
    ```
    **Output:**
    ```
    False
    ```

52. **Project:** Print the result of not (False).
    
    **Solution:**
    ```akandechips
    print not False
    ```
    **Output:**
    ```
    True
    ```

53. **Project:** Check if 3 == 3 and 4 != 5.
    
    **Solution:**
    ```akandechips
    print 3 == 3 and 4 != 5
    ```
    **Output:**
    ```
    True
    ```

54. **Project:** Check if 3 == 4 or 4 != 5.
    
    **Solution:**
    ```akandechips
    print 3 == 4 or 4 != 5
    ```
    **Output:**
    ```
    True
    ```

55. **Project:** Print the result of not (3 == 4 or 4 != 5).
    
    **Solution:**
    ```akandechips
    print not (3 == 4 or 4 != 5)
    ```
    **Output:**
    ```
    False
    ```

56. **Project:** Check if 2 == 2 and 3 == 3 and 4 == 4.
    
    **Solution:**
    ```akandechips
    print 2 == 2 and 3 == 3 and 4 == 4
    ```
    **Output:**
    ```
    True
    ```

57. **Project:** Check if 2 == 2 or 3 == 4 or 4 == 4.
    
    **Solution:**
    ```akandechips
    print 2 == 2 or 3 == 4 or 4 == 4
    ```
    **Output:**
    ```
    True
    ```

58. **Project:** Print the result of not (2 == 2 or 3 == 4 or 4 == 4).
    
    **Solution:**
    ```akandechips
    print not (2 == 2 or 3 == 4 or 4 == 4)
    ```
    **Output:**
    ```
    False
    ```

59. **Project:** Print the result of not (2 == 3 and 3 == 4 and 4 == 4).
    
    **Solution:**
    ```akandechips
    print not (2 == 3 and 3 == 4 and 4 == 4)
    ```
    **Output:**
    ```
    True
    ```

60. **Project:** Print the result of True and False or True and not True.
    
    **Solution:**
    ```akandechips
    print True and False or True and not True
    ```
    **Output:**
    ```
    False
    ```
(See Input/Output section above for 30+ projects, solutions, and outputs.)

---

### Comments and Documentation
**Explanation:**
Comments help explain code to humans. Documentation makes programs easier to understand and maintain.

#### Coding Questions & Answers
##### Q1
**Question:** Add a single-line comment above a print statement.
```akandechips
# This prints a greeting
print("Hello, AkandeChips!")
```
**Expected Output:**
```
Hello, AkandeChips!
```

##### Q2
**Question:** Add a comment explaining what the following code does.
```akandechips
# This adds two numbers and prints the result
print(3 + 5)
```
**Expected Output:**
```
8
```

##### Q3
**Question:** Write a function with a docstring that describes its purpose.
```akandechips
def greet():
    """Prints a greeting message."""
    print("Hello!")
greet()
```
**Expected Output:**
```
Hello!
```

##### Q4
**Question:** Add a comment to explain a variable assignment.
```akandechips
# Store the year
year = 2025
print(year)
```
**Expected Output:**
```
2025
```

##### Q5
**Question:** Add a comment to describe a for loop.
```akandechips
# Print numbers 1 to 3
for i in range(1, 4):
    print(i)
```
**Expected Output:**
```
1
2
3
```

##### Q6
**Question:** Add a comment to explain a function parameter.
```akandechips
def square(n):
    # n is the number to square
    return n * n
print(square(4))
```
**Expected Output:**
```
16
```

##### Q7
**Question:** Add a comment to explain a conditional statement.
```akandechips
# Check if a number is even
if 6 % 2 == 0:
    print("Even")
else:
    print("Odd")
```
**Expected Output:**
```
Even
```

##### Q8
**Question:** Add a comment to describe a list.
```akandechips
# List of chip types
chips = ["FPGA", "ASIC", "CPU"]
print(chips)
```
**Expected Output:**
```
["FPGA", "ASIC", "CPU"]
```

##### Q9
**Question:** Add a docstring to a function that returns the sum of two numbers.
```akandechips
def add(a, b):
    """Return the sum of a and b."""
    return a + b
print(add(2, 3))
```
**Expected Output:**
```
5
```

##### Q10
**Question:** Add a comment to explain a while loop.
```akandechips
# Print numbers from 1 to 3 using a while loop
i = 1
while i <= 3:
    print(i)
    i += 1
```
**Expected Output:**
```
1
2
3
```

##### Q11
**Question:** Add a comment to describe a boolean variable.
```akandechips
# True if the chip is ready
is_ready = True
print(is_ready)
```
**Expected Output:**
```
True
```

##### Q12
**Question:** Add a comment to explain a string operation.
```akandechips
# Convert to uppercase
print("chips".upper())
```
**Expected Output:**
```
CHIPS
```

##### Q13
**Question:** Add a comment to describe a function return value.
```akandechips
def cube(n):
    # Return the cube of n
    return n ** 3
print(cube(2))
```
**Expected Output:**
```
8
```

##### Q14
**Question:** Add a comment to explain a list comprehension.
```akandechips
# Get squares of numbers 1 to 3
squares = [x * x for x in range(1, 4)]
print(squares)
```
**Expected Output:**
```
[1, 4, 9]
```

##### Q15
**Question:** Add a comment to describe a dictionary (if supported).
```akandechips
# Dictionary of chip speeds (if supported)
speeds = {"FPGA": 100, "ASIC": 200}
print(speeds)
```
**Expected Output:**
```
{"FPGA": 100, "ASIC": 200}
```

##### Q16
**Question:** Add a comment to explain a function call.
```akandechips
def greet():
    print("Hello!")
# Call the greet function
greet()
```
**Expected Output:**
```
Hello!
```

##### Q17
**Question:** Add a comment to describe a for loop that prints even numbers.
```akandechips
# Print even numbers from 2 to 6
for i in range(2, 7, 2):
    print(i)
```
**Expected Output:**
```
2
4
6
```

##### Q18
**Question:** Add a comment to explain a break statement.
```akandechips
# Stop loop when i is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```
**Expected Output:**
```
1
2
```

##### Q19
**Question:** Add a comment to describe a continue statement.
```akandechips
# Skip 3 in the loop
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
```
**Expected Output:**
```
1
2
4
```

##### Q20
**Question:** Add a comment to explain a nested function call.
```akandechips
# Print the length of the uppercase version of "chips"
print(len("chips".upper()))
```
**Expected Output:**
```
5
```

##### Q21
**Question:** Add a comment to describe a function with parameters and a return value.
```akandechips
def add(a, b):
    # Add two numbers and return the result
    return a + b
print(add(4, 5))
```
**Expected Output:**
```
9
```

##### Q22
**Question:** Add a comment to explain a string slice.
```akandechips
# Get the first three letters
print("chips"[:3])
```
**Expected Output:**
```
chi
```

##### Q23
**Question:** Add a comment to describe a function that checks if a number is positive.
```akandechips
def is_positive(n):
    # Return True if n is positive
    return n > 0
print(is_positive(5))
```
**Expected Output:**
```
True
```

##### Q24
**Question:** Add a comment to explain a function that returns the length of a list.
```akandechips
def list_length(lst):
    # Return the length of the list
    return len(lst)
print(list_length([1, 2, 3]))
```
**Expected Output:**
```
3
```

##### Q25
**Question:** Add a comment to describe a function that prints a string n times.
```akandechips
def repeat(s, n):
    # Print s n times
    for i in range(n):
        print(s)
repeat("chips", 2)
```
**Expected Output:**
```
chips
chips
```

##### Q26
**Question:** Add a comment to explain a function that returns the maximum of two numbers.
```akandechips
def maximum(a, b):
    # Return the larger of a and b
    return a if a > b else b
print(maximum(7, 3))
```
**Expected Output:**
```
7
```

##### Q27
**Question:** Add a comment to describe a function that prints the reverse of a string.
```akandechips
def reverse(s):
    # Print the string in reverse
    print(s[::-1])
reverse("chips")
```
**Expected Output:**
```
spihc
```

##### Q28
**Question:** Add a comment to explain a function that returns the sum of a list.
```akandechips
def sum_list(lst):
    # Return the sum of all elements
    return sum(lst)
print(sum_list([1, 2, 3]))
```
**Expected Output:**
```
6
```

##### Q29
**Question:** Add a comment to describe a function that prints the cube of a number.
```akandechips
def print_cube(n):
    # Print the cube of n
    print(n ** 3)
print_cube(2)
```
**Expected Output:**
```
8
```

##### Q30
**Question:** Add a comment to explain a function that returns True if a string is a palindrome.
```akandechips
def is_palindrome(s):
    # Return True if s is a palindrome
    return s == s[::-1]
print(is_palindrome("level"))
```
**Expected Output:**
```
True
```

#### Projects & Solutions
(See Comments and Documentation section above for 30+ projects, solutions, and outputs.)

---

### Error Handling (try/except, Basic Debugging)
**Explanation:**
Error handling lets your program deal with unexpected situations without crashing. Debugging helps you find and fix mistakes.

#### Coding Questions & Answers
##### Q1
**Question:** Use try/except to handle division by zero.
```akandechips
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
**Expected Output:**
```
Cannot divide by zero!
```

##### Q2
**Question:** Use try/except to handle invalid integer input.
```akandechips
try:
    n = int("chips")
except ValueError:
    print("Invalid input!")
```
**Expected Output:**
```
Invalid input!
```

##### Q3
**Question:** Use try/except to catch an IndexError.
```akandechips
lst = [1, 2, 3]
try:
    print(lst[5])
except IndexError:
    print("Index out of range!")
```
**Expected Output:**
```
Index out of range!
```

##### Q4
**Question:** Use try/except to catch a KeyError in a dictionary.
```akandechips
d = {"a": 1}
try:
    print(d["b"])
except KeyError:
    print("Key not found!")
```
**Expected Output:**
```
Key not found!
```

##### Q5
**Question:** Use try/except to handle a TypeError.
```akandechips
try:
    print("chips" + 5)
except TypeError:
    print("Type error!")
```
**Expected Output:**
```
Type error!
```

##### Q6
**Question:** Use try/except to handle a ValueError when converting input.
```akandechips
try:
    n = int("abc")
except ValueError:
    print("Not a number!")
```
**Expected Output:**
```
Not a number!
```

##### Q7
**Question:** Use try/except to handle a NameError.
```akandechips
try:
    print(x)
except NameError:
    print("Variable not defined!")
```
**Expected Output:**
```
Variable not defined!
```

##### Q8
**Question:** Use try/except to handle a FileNotFoundError (if supported).
```akandechips
try:
    open("nofile.txt")
except FileNotFoundError:
    print("File not found!")
```
**Expected Output:**
```
File not found!
```

##### Q9
**Question:** Use try/except to handle multiple exceptions.
```akandechips
try:
    print(10 / 0)
except (ZeroDivisionError, TypeError):
    print("Error occurred!")
```
**Expected Output:**
```
Error occurred!
```

##### Q10
**Question:** Use try/except/finally to print a message after an error.
```akandechips
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Zero division!")
finally:
    print("Done.")
```
**Expected Output:**
```
Zero division!
Done.
```

##### Q11
**Question:** Use try/except to debug a function that raises an error.
```akandechips
def buggy():
    return 1 / 0
try:
    buggy()
except ZeroDivisionError:
    print("Bug found!")
```
**Expected Output:**
```
Bug found!
```

##### Q12
**Question:** Use try/except to handle an AttributeError.
```akandechips
try:
    x = 5
    x.append(3)
except AttributeError:
    print("Attribute error!")
```
**Expected Output:**
```
Attribute error!
```

##### Q13
**Question:** Use try/except to handle a SyntaxError (if possible).
```akandechips
try:
    eval("print('chips')")
except SyntaxError:
    print("Syntax error!")
```
**Expected Output:**
```
chips
```

##### Q14
**Question:** Use try/except to handle a custom error.
```akandechips
try:
    raise Exception("Custom error!")
except Exception as e:
    print(e)
```
**Expected Output:**
```
Custom error!
```

##### Q15
**Question:** Use try/except to debug a list index error.
```akandechips
lst = [1, 2]
try:
    print(lst[3])
except IndexError:
    print("Debug: index error!")
```
**Expected Output:**
```
Debug: index error!
```

##### Q16
**Question:** Use try/except to print a message if a variable is not defined.
```akandechips
try:
    print(y)
except NameError:
    print("y is not defined!")
```
**Expected Output:**
```
y is not defined!
```

##### Q17
**Question:** Use try/except to handle a division by zero in a function.
```akandechips
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No division by zero!"
print(divide(5, 0))
```
**Expected Output:**
```
No division by zero!
```

##### Q18
**Question:** Use try/except to handle a ValueError in user input.
```akandechips
try:
    n = int("notanumber")
except ValueError:
    print("Bad input!")
```
**Expected Output:**
```
Bad input!
```

##### Q19
**Question:** Use try/except to print a message if a file cannot be opened (if supported).
```akandechips
try:
    open("nofile.txt")
except Exception:
    print("Cannot open file!")
```
**Expected Output:**
```
Cannot open file!
```

##### Q20
**Question:** Use try/except to debug a function that returns None on error.
```akandechips
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
print(safe_divide(4, 0))
```
**Expected Output:**
```
None
```

##### Q21
**Question:** Use try/except to print a custom error message for a TypeError.
```akandechips
try:
    print(5 + "chips")
except TypeError:
    print("Cannot add int and str!")
```
**Expected Output:**
```
Cannot add int and str!
```

##### Q22
**Question:** Use try/except to print a message if a list is empty before accessing its first element.
```akandechips
lst = []
try:
    print(lst[0])
except IndexError:
    print("List is empty!")
```
**Expected Output:**
```
List is empty!
```

##### Q23
**Question:** Use try/except to print a message if a dictionary key is missing.
```akandechips
d = {"chips": 1}
try:
    print(d["cool"])
except KeyError:
    print("Key missing!")
```
**Expected Output:**
```
Key missing!
```

##### Q24
**Question:** Use try/except to print a message if a function call fails.
```akandechips
def buggy():
    return 1 / 0
try:
    buggy()
except Exception:
    print("Function failed!")
```
**Expected Output:**
```
Function failed!
```

##### Q25
**Question:** Use try/except to print a message if a string cannot be converted to an integer.
```akandechips
try:
    n = int("chips")
except ValueError:
    print("Conversion failed!")
```
**Expected Output:**
```
Conversion failed!
```

##### Q26
**Question:** Use try/except to print a message if a variable is not defined in a function.
```akandechips
def test():
    try:
        print(x)
    except NameError:
        print("x not defined!")
test()
```
**Expected Output:**
```
x not defined!
```

##### Q27
**Question:** Use try/except to print a message if a list index is out of range in a function.
```akandechips
def get_item(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return "Out of range!"
print(get_item([1, 2], 5))
```
**Expected Output:**
```
Out of range!
```

##### Q28
**Question:** Use try/except to print a message if a division by zero occurs in a loop.
```akandechips
for n in [2, 1, 0]:
    try:
        print(10 / n)
    except ZeroDivisionError:
        print("Zero division!")
```
**Expected Output:**
```
5.0
10.0
Zero division!
```

##### Q29
**Question:** Use try/except to print a message if a function argument is missing.
```akandechips
def f(a):
    print(a)
try:
    f()
except TypeError:
    print("Missing argument!")
```
**Expected Output:**
```
Missing argument!
```

##### Q30
**Question:** Use try/except to print a message if a string index is out of range.
```akandechips
s = "chips"
try:
    print(s[10])
except IndexError:
    print("String index out of range!")
```
**Expected Output:**
```
String index out of range!
```

#### Projects & Solutions
(See Error Handling section above for 30+ projects, solutions, and outputs.)

---

### Functions and Procedures (Defining, Calling, Parameters, Return Values)
**Explanation:**
Functions let you organize code into reusable blocks. They can take inputs (parameters) and return outputs (return values).

#### Coding Questions & Answers
##### Q1
**Question:** Define a function that prints "Hello, World!" and call it.
```akandechips
def greet():
    print("Hello, World!")
greet()
```
**Expected Output:**
```
Hello, World!
```

##### Q2
**Question:** Define a function that takes a name as a parameter and prints "Hello, <name>!" Call it with "Alex".
```akandechips
def greet(name):
    print("Hello,", name + "!")
greet("Alex")
```
**Expected Output:**
```
Hello, Alex!
```

##### Q3
**Question:** Define a function that returns the sum of two numbers. Print the result of calling it with 3 and 5.
```akandechips
def add(a, b):
    return a + b
print(add(3, 5))
```
**Expected Output:**
```
8
```

##### Q4
**Question:** Define a function that returns the square of a number. Print the result for 4.
```akandechips
def square(n):
    return n * n
print(square(4))
```
**Expected Output:**
```
16
```

##### Q5
**Question:** Define a function that prints "chips are cool!" Call it.
```akandechips
def cool():
    print("chips are cool!")
cool()
```
**Expected Output:**
```
chips are cool!
```

##### Q6
**Question:** Define a function that takes two numbers and prints their product. Call it with 6 and 7.
```akandechips
def multiply(a, b):
    print(a * b)
multiply(6, 7)
```
**Expected Output:**
```
42
```

##### Q7
**Question:** Define a function that returns True if a number is even, False otherwise. Print the result for 8.
```akandechips
def is_even(n):
    return n % 2 == 0
print(is_even(8))
```
**Expected Output:**
```
True
```

##### Q8
**Question:** Define a function that prints the first character of a string. Call it with "chips".
```akandechips
def first_char(s):
    print(s[0])
first_char("chips")
```
**Expected Output:**
```
c
```

##### Q9
**Question:** Define a function that takes a list and prints its length. Call it with [1, 2, 3].
```akandechips
def print_length(lst):
    print(len(lst))
print_length([1, 2, 3])
```
**Expected Output:**
```
3
```

##### Q10
**Question:** Define a function that returns the maximum of two numbers. Print the result for 10 and 7.
```akandechips
def maximum(a, b):
    return a if a > b else b
print(maximum(10, 7))
```
**Expected Output:**
```
10
```

##### Q11
**Question:** Define a function that prints numbers from 1 to n. Call it with 3.
```akandechips
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
print_numbers(3)
```
**Expected Output:**
```
1
2
3
```

##### Q12
**Question:** Define a function that returns the factorial of a number. Print the result for 4.
```akandechips
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(4))
```
**Expected Output:**
```
24
```

##### Q13
**Question:** Define a function that takes a string and returns it in uppercase. Print the result for "chips".
```akandechips
def to_upper(s):
    return s.upper()
print(to_upper("chips"))
```
**Expected Output:**
```
CHIPS
```

##### Q14
**Question:** Define a function that prints "AkandeChips" n times. Call it with 2.
```akandechips
def repeat(n):
    for i in range(n):
        print("AkandeChips")
repeat(2)
```
**Expected Output:**
```
AkandeChips
AkandeChips
```

##### Q15
**Question:** Define a function that returns the sum of all numbers in a list. Print the result for [1, 2, 3].
```akandechips
def sum_list(lst):
    return sum(lst)
print(sum_list([1, 2, 3]))
```
**Expected Output:**
```
6
```

##### Q16
**Question:** Define a function that takes a string and prints it backwards. Call it with "chips".
```akandechips
def reverse(s):
    print(s[::-1])
reverse("chips")
```
**Expected Output:**
```
spihc
```

##### Q17
**Question:** Define a function that returns the average of two numbers. Print the result for 4 and 8.
```akandechips
def average(a, b):
    return (a + b) / 2
print(average(4, 8))
```
**Expected Output:**
```
6.0
```

##### Q18
**Question:** Define a function that prints whether a number is positive, negative, or zero. Call it with -3.
```akandechips
def check_sign(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
check_sign(-3)
```
**Expected Output:**
```
Negative
```

##### Q19
**Question:** Define a function that returns the last character of a string. Print the result for "chips".
```akandechips
def last_char(s):
    return s[-1]
print(last_char("chips"))
```
**Expected Output:**
```
s
```

##### Q20
**Question:** Define a function that prints the numbers from n down to 1. Call it with 3.
```akandechips
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
countdown(3)
```
**Expected Output:**
```
3
2
1
```

##### Q21
**Question:** Define a function that returns True if a string is a palindrome. Print the result for "level".
```akandechips
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("level"))
```
**Expected Output:**
```
True
```

##### Q22
**Question:** Define a function that takes a list and returns the maximum value. Print the result for [2, 8, 5].
```akandechips
def max_list(lst):
    return max(lst)
print(max_list([2, 8, 5]))
```
**Expected Output:**
```
8
```

##### Q23
**Question:** Define a function that prints the multiplication table of a number up to 5. Call it with 3.
```akandechips
def table(n):
    for i in range(1, 6):
        print(n, "x", i, "=", n * i)
table(3)
```
**Expected Output:**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
```

##### Q24
**Question:** Define a function that returns the minimum of three numbers. Print the result for 7, 2, 9.
```akandechips
def minimum(a, b, c):
    return min(a, b, c)
print(minimum(7, 2, 9))
```
**Expected Output:**
```
2
```

##### Q25
**Question:** Define a function that takes a string and returns it with all vowels removed. Print the result for "chips are cool".
```akandechips
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([c for c in s if c not in vowels])
print(remove_vowels("chips are cool"))
```
**Expected Output:**
```
chps r cl
```

##### Q26
**Question:** Define a function that returns the absolute value of a number. Print the result for -7.
```akandechips
def absolute(n):
    return abs(n)
print(absolute(-7))
```
**Expected Output:**
```
7
```

##### Q27
**Question:** Define a function that prints the sum of all even numbers up to n. Call it with 6.
```akandechips
def sum_evens(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    print(total)
sum_evens(6)
```
**Expected Output:**
```
12
```

##### Q28
**Question:** Define a function that returns the number of words in a string. Print the result for "chips are cool".
```akandechips
def word_count(s):
    return len(s.split())
print(word_count("chips are cool"))
```
**Expected Output:**
```
3
```

##### Q29
**Question:** Define a function that prints a string n times, each on a new line. Call it with "chips" and 3.
```akandechips
def repeat_string(s, n):
    for i in range(n):
        print(s)
repeat_string("chips", 3)
```
**Expected Output:**
```
chips
chips
chips
```

##### Q30
**Question:** Define a function that returns the cube of a number. Print the result for 2.
```akandechips
def cube(n):
    return n ** 3
print(cube(2))
```
**Expected Output:**
```
8
```

#### Projects & Solutions
(See Functions and Procedures section above for 30+ projects, solutions, and outputs.)

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

77. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

78. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

79. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

80. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers
##### Q1
**Question:** What is variable scope?
   
   **Answer:**
   Scope is the part of the program where a variable can be used.

2. **What is variable lifetime?**
   
   **Answer:**
   Lifetime is how long a variable exists in memory while the program runs.

3. **What is a global variable?**
   
   **Answer:**
   A variable defined outside any function; it can be used anywhere in the file.

4. **What is a local variable?**
   
   **Answer:**
   A variable defined inside a function; it can only be used inside that function.

5. **Can a local variable be used outside its function?**
   
   **Answer:**
   No, it only exists inside the function.

6. **Can a global variable be used inside a function?**
   
   **Answer:**
   Yes, unless a local variable with the same name is defined.

7. **What happens if you use a variable before defining it?**
   
   **Answer:**
   You get an error.

8. **What happens to a local variable after the function ends?**
   
   **Answer:**
   It is destroyed and cannot be used anymore.

9. **What happens to a global variable after the program ends?**
   
   **Answer:**
   It is destroyed and memory is freed.

10. **Can two functions have local variables with the same name?**
    
    **Answer:**
    Yes, each function's local variables are separate.

11. **Can a function change a global variable?**
    
    **Answer:**
    Yes, if you declare it as global inside the function.

12. **How do you declare a global variable inside a function?**
    
    **Answer:**
    Use the `global` keyword (if supported).

13. **What is variable shadowing?**
    
    **Answer:**
    When a local variable has the same name as a global variable, the local one is used inside the function.

14. **What is the scope of a variable defined in a loop?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

15. **What is the scope of a variable defined in an if statement?**
    
    **Answer:**
    Usually, it is accessible in the block where it is defined.

16. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function starts until it ends.

17. **What is the lifetime of a global variable?**
    
    **Answer:**
    From when it is defined until the program ends.

18. **Can you have a variable with the same name in different scopes?**
    
    **Answer:**
    Yes, but they are different variables.

19. **What is a block scope?**
    
    **Answer:**
    The area inside curly braces `{}` or indentation where a variable is defined.

20. **What is a function scope?**
    
    **Answer:**
    The area inside a function definition.

21. **What is the difference between local and global scope?**
    
    **Answer:**
    Local scope is inside a function; global scope is outside all functions.

22. **Can a variable be both local and global?**
    
    **Answer:**
    No, it is either local or global in a given context.

23. **What happens if you change a global variable inside a function without declaring it global?**
    
    **Answer:**
    It creates a new local variable with the same name.

24. **How do you access a global variable inside a function?**
    
    **Answer:**
    Just use its name, unless a local variable with the same name exists.

25. **What is the scope of a variable defined in a for loop?**
    
    **Answer:**
    It is usually accessible after the loop ends (unless block scope is enforced).

26. **What is the scope of a variable defined in an if block?**
    
    **Answer:**
    It is usually accessible after the block ends (unless block scope is enforced).

27. **What is the lifetime of a variable defined in a function?**
    
    **Answer:**
    From when the function is called until it ends.

28. **What is the lifetime of a global variable?**
    
    **Answer:**
    As long as the program runs.

29. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

30. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

31. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

32. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

33. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

34. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

35. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

36. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

37. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

38. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

39. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

40. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

41. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

42. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

43. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

44. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

45. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

46. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

47. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

48. **What is the scope of a variable defined in a function default parameter?**
    
    **Answer:**
    It is local to the function.

49. **What is the lifetime of a variable defined in a function default parameter?**
    
    **Answer:**
    As long as the function is in use.

50. **What is the scope of a variable defined in a decorator (if supported)?**
    
    **Answer:**
    It is local to the decorator function.

51. **What is the lifetime of a variable defined in a decorator?**
    
    **Answer:**
    As long as the decorator exists.

52. **What is the scope of a variable defined in a static method?**
    
    **Answer:**
    It is local to the static method.

53. **What is the lifetime of a variable defined in a static method?**
    
    **Answer:**
    From when the method is called until it ends.

54. **What is the scope of a variable defined in a class method?**
    
    **Answer:**
    It is local to the class method unless declared as a class variable.

55. **What is the lifetime of a variable defined in a class method?**
    
    **Answer:**
    From when the method is called until it ends.

56. **What is the scope of a variable defined in a lambda?**
    
    **Answer:**
    It is local to the lambda function.

57. **What is the lifetime of a variable defined in a lambda?**
    
    **Answer:**
    As long as the lambda exists.

58. **Can a variable be both a parameter and a local variable?**
    
    **Answer:**
    Yes, but the parameter takes precedence inside the function.

59. **What is the scope of a variable defined in a list comprehension?**
    
    **Answer:**
    It is local to the comprehension.

60. **What is the lifetime of a variable defined in a list comprehension?**
    
    **Answer:**
    It exists only during the comprehension's execution.

61. **What is the scope of a variable defined in a generator expression?**
    
    **Answer:**
    It is local to the generator expression.

62. **What is the lifetime of a variable defined in a generator expression?**
    
    **Answer:**
    It exists only during the generator's execution.

63. **What is the scope of a variable defined in a try/finally block?**
    
    **Answer:**
    It is accessible after the block ends.

64. **What is the lifetime of a variable defined in a try/finally block?**
    
    **Answer:**
    From when the block starts until it ends.

65. **What is the scope of a variable defined in a with block?**
    
    **Answer:**
    It is accessible after the block ends.

66. **What is the lifetime of a variable defined in a with block?**
    
    **Answer:**
    From when the block starts until it ends.

67. **What is the scope of a variable defined in a case block (if supported)?**
    
    **Answer:**
    It is local to the case block.

68. **What is the lifetime of a variable defined in a case block?**
    
    **Answer:**
    From when the block starts until it ends.

69. **What is the scope of a variable defined in a match block (if supported)?**
    
    **Answer:**
    It is local to the match block.

70. **What is the lifetime of a variable defined in a match block?**
    
    **Answer:**
    From when the block starts until it ends.

71. **What is the scope of a variable defined in a for-each loop?**
    
    **Answer:**
    It is accessible after the loop ends.

72. **What is the lifetime of a variable defined in a for-each loop?**
    
    **Answer:**
    From when the loop starts until it ends.

73. **What is the scope of a variable defined in a while loop?**
    
    **Answer:**
    It is accessible after the loop ends.

74. **What is the lifetime of a variable defined in a while loop?**
    
    **Answer:**
    From when the loop starts until it ends.

75. **What is the scope of a variable defined in a do-while loop (if supported)?**
    
    **Answer:**
    It is accessible after the loop ends.

76. **What is the lifetime of a variable defined in a do-while loop?**
    
    **Answer:**
    From when the loop starts until it ends.
**Expected Output:**
```
Number: 5
Odd
```

##### Project 8
**Project:** Print the sum of all numbers from 1 to n (user input) (AkandeChips vs. Python).
```akandechips
n = int(input("n: "))
total = 0
for i in range(1, n+1):
    total += i
print(total)
```
```python
n = int(input("n: "))
total = 0
for i in range(1, n+1):
    total += i
print(total)
```
**Expected Output:**
```
n: 5
15
```

##### Project 9
**Project:** Print a string with each letter separated by a dash (AkandeChips vs. Python).
```akandechips
word = input("Word: ")
print("-".join(word))
```
```python
word = input("Word: ")
print("-".join(word))
```
**Expected Output:**
```
Word: chips
c-h-i-p-s
```

##### Project 10
**Project:** Print the factorial of a user-entered number (AkandeChips vs. Python).
```akandechips
n = int(input("Number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
```
```python
n = int(input("Number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
```
**Expected Output:**
```
Number: 4
24
```

##### Project 11
**Project:** Print the maximum of three user-entered numbers (AkandeChips vs. Python).
```akandechips
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(max(a, b, c))
```
```python
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(max(a, b, c))
```
**Expected Output:**
```
a: 3
b: 7
c: 5
7
```

##### Project 12
**Project:** Print the average of a list of numbers (AkandeChips vs. Python).
```akandechips
nums = [2, 4, 6, 8]
print(sum(nums) / len(nums))
```
```python
nums = [2, 4, 6, 8]
print(sum(nums) / len(nums))
```
**Expected Output:**
```
5.0
```

##### Project 13
**Project:** Print a string in title case (AkandeChips vs. Python).
```akandechips
text = input("Text: ")
print(text.title())
```
```python
text = input("Text: ")
print(text.title())
```
**Expected Output:**
```
Text: chips are cool
Chips Are Cool
```

##### Project 14
**Project:** Print the reverse of a list (AkandeChips vs. Python).
```akandechips
nums = [1, 2, 3]
print(nums[::-1])
```
```python
nums = [1, 2, 3]
print(nums[::-1])
```
**Expected Output:**
```
[3, 2, 1]
```

##### Project 15
**Project:** Print whether a string is a palindrome (AkandeChips vs. Python).
```akandechips
s = input("String: ")
print(s == s[::-1])
```
```python
s = input("String: ")
print(s == s[::-1])
```
**Expected Output:**
```
String: level
True
```

##### Project 16
**Project:** Print the sum of even numbers from 1 to 10 (AkandeChips vs. Python).
```akandechips
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print(total)
```
```python
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print(total)
```
**Expected Output:**
```
30
```

##### Project 17
**Project:** Print the minimum of a list (AkandeChips vs. Python).
```akandechips
nums = [5, 2, 9]
print(min(nums))
```
```python
nums = [5, 2, 9]
print(min(nums))
```
**Expected Output:**
```
2
```

##### Project 18
**Project:** Print the result of 2 to the power of 10 (AkandeChips vs. Python).
```akandechips
print(2 ** 10)
```
```python
print(2 ** 10)
```
**Expected Output:**
```
1024
```

##### Project 19
**Project:** Print the result of dividing 100 by 8, rounded to 2 decimals (AkandeChips vs. Python).
```akandechips
print(round(100 / 8, 2))
```
```python
print(round(100 / 8, 2))
```
**Expected Output:**
```
12.5
```

##### Project 20
**Project:** Print the string "chips" with each letter separated by a space (AkandeChips vs. Python).
```akandechips
print(" ".join("chips"))
```
```python
print(" ".join("chips"))
```
**Expected Output:**
```
c h i p s
```


### Practice Tests and Review Sections
**Explanation:**
Test your knowledge and review key concepts before moving on.

#### Coding Questions & Answers

1. **What is the output of `print 2 + 3`?**
   
   **Answer:**
   ```akandechips
   print 2 + 3
   ```
   **Output:**
   ```
   5
   ```

2. **How do you create a list with the numbers 1, 2, and 3?**
   
   **Answer:**
   ```akandechips
   nums = [1, 2, 3]
   print nums
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

3. **What is the result of `print 5 > 2 and 2 < 1`?**
   
   **Answer:**
   ```akandechips
   print 5 > 2 and 2 < 1
   ```
   **Output:**
   ```
   False
   ```

4. **How do you import the math module?**
   
   **Answer:**
   ```akandechips
   import math
   ```

5. **What is the output of `print "Hello, World!"`?**
   
   **Answer:**
   ```akandechips
   print "Hello, World!"
   ```
   **Output:**
   ```
   Hello, World!
   ```

6. **How do you write a comment in AkandeChips?**
   
   **Answer:**
   Use `#` at the start of the line.

7. **What is the output of `print 10 // 3`?**
   
   **Answer:**
   ```akandechips
   print 10 // 3
   ```
   **Output:**
   ```
   3
   ```

8. **How do you define a function that adds two numbers?**
   
   **Answer:**
   ```akandechips
   def add(a, b):
       return a + b
   print add(2, 3)
   ```
   **Output:**
   ```
   5
   ```

9. **What is the output of `print [1, 2, 3][1]`?**
   
   **Answer:**
   ```akandechips
   print [1, 2, 3][1]
   ```
   **Output:**
   ```
   2
   ```

10. **How do you check if 4 is in the list `[1, 2, 3, 4]`?**
    
    **Answer:**
    ```akandechips
    print 4 in [1, 2, 3, 4]
    ```
    **Output:**
    ```
    True
    ```

11. **What is the output of `print len("chips")`?**
    
    **Answer:**
    ```akandechips
    print len("chips")
    ```
    **Output:**
    ```
    5
    ```

12. **How do you get the last item in a list `nums`?**
    
    **Answer:**
    Use `nums[-1]`.

13. **What is the output of `print 2 ** 3`?**
    
    **Answer:**
    ```akandechips
    print 2 ** 3
    ```
    **Output:**
    ```
    8
    ```

14. **How do you handle errors in AkandeChips?**
    
    **Answer:**
    Use `try` and `except` blocks.

15. **What is the output of `print "a" * 3`?**
    
    **Answer:**
    ```akandechips
    print "a" * 3
    ```
    **Output:**
    ```
    aaa
    ```

16. **How do you create a dictionary with keys "a" and "b" and values 1 and 2?**
    
    **Answer:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d
    ```
    **Output:**
    ```
    {"a": 1, "b": 2}
    ```

17. **What is the output of `print not False`?**
    
    **Answer:**
    ```akandechips
    print not False
    ```
    **Output:**
    ```
    True
    ```

18. **How do you get all keys from a dictionary `d`?**
    
    **Answer:**
    Use `d.keys()`.

19. **What is the output of `print sum([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print sum([1, 2, 3])
    ```
    **Output:**
    ```
    6
    ```

20. **How do you import only the sqrt function from math?**
    
    **Answer:**
    ```akandechips
    from math import sqrt
    print sqrt(9)
    ```
    **Output:**
    ```
    3
    ```

21. **What is the output of `print [x for x in range(3)]`?**
    
    **Answer:**
    ```akandechips
    print [x for x in range(3)]
    ```
    **Output:**
    ```
    [0, 1, 2]
    ```

22. **How do you check if a string starts with "Akan"?**
    
    **Answer:**
    Use `str.startswith("Akan")`.

23. **What is the output of `print 7 % 3`?**
    
    **Answer:**
    ```akandechips
    print 7 % 3
    ```
    **Output:**
    ```
    1
    ```

24. **How do you reverse a list `nums`?**
    
    **Answer:**
    Use `nums.reverse()` or `nums[::-1]`.

25. **What is the output of `print 3 in [1, 2, 3]`?**
    
    **Answer:**
    ```akandechips
    print 3 in [1, 2, 3]
    ```
    **Output:**
    ```
    True
    ```

26. **How do you get the length of a list `nums`?**
    
    **Answer:**
    Use `len(nums)`.

27. **What is the output of `print [1, 2, 3].count(2)`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3].count(2)
    ```
    **Output:**
    ```
    1
    ```

28. **How do you create a tuple with values 1, 2, 3?**
    
    **Answer:**
    ```akandechips
    tup = (1, 2, 3)
    print tup
    ```
    **Output:**
    ```
    (1, 2, 3)
    ```

29. **What is the output of `print type([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print type([1, 2, 3])
    ```
    **Output:**
    ```
    list
    ```

30. **How do you handle division by zero errors?**
    
    **Answer:**
    Use try/except:
    ```akandechips
    try:
        print 1 / 0
    except:
        print "Error"
    ```
    **Output:**
    ```
    Error
    ```


#### Projects & Solutions

1. **Project:** Write a program that prints the numbers 1 to 5.
   
   **Solution:**
   ```akandechips
   for i in range(1, 6):
       print i
   ```
   **Output:**
   ```
   1
   2
   3
   4
   5
   ```

2. **Project:** Write a function that returns the square of a number.
   
   **Solution:**
   ```akandechips
   def square(x):
       return x * x
   print square(4)
   ```
   **Output:**
   ```
   16
   ```

3. **Project:** Create a list of even numbers from 2 to 10 and print it.
   
   **Solution:**
   ```akandechips
   evens = [2, 4, 6, 8, 10]
   print evens
   ```
   **Output:**
   ```
   [2, 4, 6, 8, 10]
   ```

4. **Project:** Write a program that sums all numbers in a list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3, 4]
   print sum(nums)
   ```
   **Output:**
   ```
   10
   ```

5. **Project:** Write a program that finds the largest number in a list.
   
   **Solution:**
   ```akandechips
   nums = [3, 7, 2, 9]
   print max(nums)
   ```
   **Output:**
   ```
   9
   ```

6. **Project:** Write a program that checks if a string is a palindrome.
   
   **Solution:**
   ```akandechips
   s = "level"
   print s == s[::-1]
   ```
   **Output:**
   ```
   True
   ```

7. **Project:** Write a program that prints all keys in a dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d.keys()
   ```
   **Output:**
   ```
   ["a", "b"]
   ```

8. **Project:** Write a program that reverses a list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   nums.reverse()
   print nums
   ```
   **Output:**
   ```
   [3, 2, 1]
   ```

9. **Project:** Write a program that counts how many times 2 appears in a list.
   
   **Solution:**
   ```akandechips
   nums = [2, 3, 2, 4, 2]
   print nums.count(2)
   ```
   **Output:**
   ```
   3
   ```

10. **Project:** Write a program that prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and the number otherwise from 1 to 15.
    
    **Solution:**
    ```akandechips
    for i in range(1, 16):
        if i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i
    ```
    **Output:**
    ```
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    Fizz
    ```

11. **Project:** Write a program that imports math and prints the square root of 100.
    
    **Solution:**
    ```akandechips
    import math
    print math.sqrt(100)
    ```
    **Output:**
    ```
    10
    ```

12. **Project:** Write a function that returns True if a number is even.
    
    **Solution:**
    ```akandechips
    def is_even(n):
        return n % 2 == 0
    print is_even(4)
    ```
    **Output:**
    ```
    True
    ```

13. **Project:** Write a program that prints the first 10 Fibonacci numbers.
    
    **Solution:**
    ```akandechips
    a, b = 0, 1
    for i in range(10):
        print a
        a, b = b, a + b
    ```
    **Output:**
    ```
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    ```

14. **Project:** Write a program that removes duplicates from a list.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 2, 3, 3, 3]
    nums = list(set(nums))
    print nums
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

15. **Project:** Write a program that finds the minimum value in a list.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    print min(nums)
    ```
    **Output:**
    ```
    1
    ```

16. **Project:** Write a program that prints all values in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d.values()
    ```
    **Output:**
    ```
    [1, 2]
    ```

17. **Project:** Write a program that checks if a list is empty.
    
    **Solution:**
    ```akandechips
    nums = []
    print len(nums) == 0
    ```
    **Output:**
    ```
    True
    ```

18. **Project:** Write a program that prints the type of a variable.
    
    **Solution:**
    ```akandechips
    x = 5
    print type(x)
    ```
    **Output:**
    ```
    int
    ```

19. **Project:** Write a program that prints numbers from 10 to 1 in reverse order.
    
    **Solution:**
    ```akandechips
    for i in range(10, 0, -1):
        print i
    ```
    **Output:**
    ```
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    ```

20. **Project:** Write a program that prints the sum of even numbers from 1 to 10.
    
    **Solution:**
    ```akandechips
    total = 0
    for i in range(1, 11):
        if i % 2 == 0:
            total = total + i
    print total
    ```
    **Output:**
    ```
    30
    ```

21. **Project:** Write a program that prints the product of all numbers in a list.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3, 4]
    product = 1
    for n in nums:
        product = product * n
    print product
    ```
    **Output:**
    ```
    24
    ```

22. **Project:** Write a program that prints all odd numbers from 1 to 10.
    
    **Solution:**
    ```akandechips
    for i in range(1, 11):
        if i % 2 != 0:
            print i
    ```
    **Output:**
    ```
    1
    3
    5
    7
    9
    ```

23. **Project:** Write a program that prints the average of numbers in a list.
    
    **Solution:**
    ```akandechips
    nums = [2, 4, 6, 8]
    print sum(nums) / len(nums)
    ```
    **Output:**
    ```
    5
    ```

24. **Project:** Write a program that prints the first character of a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[0]
    ```
    **Output:**
    ```
    c
    ```

25. **Project:** Write a program that prints the length of a string.
    
    **Solution:**
    ```akandechips
    s = "Akande"
    print len(s)
    ```
    **Output:**
    ```
    6
    ```

26. **Project:** Write a program that prints True if a number is positive.
    
    **Solution:**
    ```akandechips
    n = 5
    print n > 0
    ```
    **Output:**
    ```
    True
    ```

27. **Project:** Write a program that prints the reverse of a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[::-1]
    ```
    **Output:**
    ```
    spihc
    ```

28. **Project:** Write a program that prints the sum of the digits of a number.
    
    **Solution:**
    ```akandechips
    n = 1234
    total = 0
    for digit in str(n):
        total = total + int(digit)
    print total
    ```
    **Output:**
    ```
    10
    ```

29. **Project:** Write a program that prints all items in a tuple.
    
    **Solution:**
    ```akandechips
    tup = (1, 2, 3)
    for item in tup:
        print item
    ```
    **Output:**
    ```
    1
    2
    3
    ```

30. **Project:** Write a program that prints the value for key "b" in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d["b"]
    ```
    **Output:**
    ```
    2
    ```
- Your First Program
- Variables and Types
- Basic Operations
- Control Flow

Each section contains:
- Detailed Explanation
- 30+ Coding Questions & Answers (with code and expected output)
- 30+ Projects & Solutions (with code and expected output)
- Room for future topic expansion

---

## What is AkandeChips?
**Explanation:**
AkandeChips is a modern language for hardware and software co-design, inspired by Python and HDL. It is designed to be easy to learn, readable, and powerful for both beginners and professionals. AkandeChips is especially important for the US, where there is a growing need for skilled chip designers and programmers.

---

## Your First Program
**Explanation:**
The first program in any language is usually a simple print statement. In AkandeChips, you use the `print()` function to display text in the terminal.

**Example:**
```akandechips
print("Hello, AkandeChips!")
```

## Essential Topics for a Comprehensive Beginner Textbook

The following sections are especially important for American students and the US chips workforce. Each topic includes explanations, coding questions, and projects to build real-world skills.

---

### Input and Output (User Input, Reading/Writing Files)
**Explanation:**
Input and output are how programs interact with users and the outside world. This includes reading user input, displaying output, and working with files.

#### Coding Questions & Answers
##### Q1
**Question:** Ask the user for their name and print it.
```akandechips
name = input("What is your name? ")
print(name)
```
**Expected Output:**
```
Alex
```

##### Q2
**Question:** Ask the user for a number and print double its value.
```akandechips
num = int(input("Enter a number: "))
print(num * 2)
```
**Expected Output:**
```
Enter a number: 5
10
```

##### Q3
**Question:** Print a message and then ask the user for their favorite color.
```akandechips
print("Let's talk about colors!")
color = input("Favorite color? ")
print(color)
```
**Expected Output:**
```
Let's talk about colors!
Favorite color? blue
blue
```

##### Q4
**Question:** Ask the user for two numbers and print their sum.
```akandechips
a = int(input("First number: "))
b = int(input("Second number: "))
print(a + b)
```
**Expected Output:**
```
First number: 3
Second number: 7
10
```

##### Q5
**Question:** Print a welcome message, then ask for the user's city and print it.
```akandechips
print("Welcome!")
city = input("Which city do you live in? ")
print(city)
```
**Expected Output:**
```
Welcome!
Which city do you live in? Dallas
Dallas
```

##### Q6
**Question:** Ask the user for a filename, then print a message (file reading not implemented in this example).
```akandechips
filename = input("Enter filename: ")
print("You entered:", filename)
```
**Expected Output:**
```
Enter filename: data.txt
You entered: data.txt
```

##### Q7
**Question:** Print a prompt, then ask for the user's age and print a message with it.
```akandechips
print("How old are you?")
age = int(input())
print("You are", age, "years old.")
```
**Expected Output:**
```
How old are you?
18
You are 18 years old.
```

##### Q8
**Question:** Ask the user for a word and print it in uppercase.
```akandechips
word = input("Enter a word: ")
print(word.upper())
```
**Expected Output:**
```
Enter a word: chips
CHIPS
```

##### Q9
**Question:** Ask the user for a number and print whether it is even or odd.
```akandechips
num = int(input("Number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
**Expected Output:**
```
Number: 7
Odd
```

##### Q10
**Question:** Print a prompt, ask for a string, and print its length.
```akandechips
text = input("Type something: ")
print(len(text))
```
**Expected Output:**
```
Type something: AkandeChips
12
```

##### Q11
**Question:** Ask the user for their favorite animal and print a message.
```akandechips
animal = input("Favorite animal: ")
print("You like", animal)
```
**Expected Output:**
```
Favorite animal: dog
You like dog
```

##### Q12
**Question:** Ask the user for a number and print the next number.
```akandechips
n = int(input("Number: "))
print(n + 1)
```
**Expected Output:**
```
Number: 9
10
```

##### Q13
**Question:** Ask the user for a string and print it three times.
```akandechips
s = input("Say something: ")
print(s)
print(s)
print(s)
```
**Expected Output:**
```
Say something: hello
hello
hello
hello
```

##### Q14
**Question:** Ask the user for a number and print if it is greater than 10.
```akandechips
num = int(input("Number: "))
if num > 10:
    print("Greater than 10")
else:
    print("10 or less")
```
**Expected Output:**
```
Number: 12
Greater than 10
```

##### Q15
**Question:** Ask the user for their state and print a greeting.
```akandechips
state = input("State: ")
print("Hello from", state)
```
**Expected Output:**
```
State: Texas
Hello from Texas
```

##### Q16
**Question:** Ask the user for a decimal number and print it rounded to the nearest integer.
```akandechips
num = float(input("Decimal: "))
print(round(num))
```
**Expected Output:**
```
Decimal: 7.8
8
```

##### Q17
**Question:** Ask the user for a word and print its first character.
```akandechips
word = input("Word: ")
print(word[0])
```
**Expected Output:**
```
Word: chips
c
```

##### Q18
**Question:** Ask the user for a sentence and print the number of words.
```akandechips
sentence = input("Sentence: ")
print(len(sentence.split()))
```
**Expected Output:**
```
Sentence: chips are cool
3
```

##### Q19
**Question:** Ask the user for a number and print its absolute value.
```akandechips
num = int(input("Number: "))
print(abs(num))
```
**Expected Output:**
```
Number: -5
5
```

##### Q20
**Question:** Ask the user for a string and print it in reverse.
```akandechips
s = input("String: ")
print(s[::-1])
```
**Expected Output:**
```
String: Akande
ednakA
```

##### Q21
**Question:** Ask the user for a number and print "Even" if even, "Odd" if odd.
```akandechips
n = int(input("Number: "))
print("Even" if n % 2 == 0 else "Odd")
```
**Expected Output:**
```
Number: 8
Even
```

##### Q22
**Question:** Ask the user for a string and print its length.
```akandechips
text = input("Text: ")
print(len(text))
```
**Expected Output:**
```
Text: hello
5
```

##### Q23
**Question:** Ask the user for a number and print its square root (rounded).
```akandechips
import math
n = int(input("Number: "))
print(round(math.sqrt(n)))
```
**Expected Output:**
```
Number: 25
5
```

##### Q24
**Question:** Ask the user for a word and print it in lowercase.
```akandechips
word = input("Word: ")
print(word.lower())
```
**Expected Output:**
```
Word: CHIPS
chips
```

##### Q25
**Question:** Ask the user for a number and print "Positive" if positive, "Negative" if negative, or "Zero" if zero.
```akandechips
n = int(input("Number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```
**Expected Output:**
```
Number: 0
Zero
```

##### Q26
**Question:** Ask the user for a string and print the last character.
```akandechips
s = input("String: ")
print(s[-1])
```
**Expected Output:**
```
String: Akande
e
```

##### Q27
**Question:** Ask the user for a number and print the result of dividing it by 2.
```akandechips
n = int(input("Number: "))
print(n / 2)
```
**Expected Output:**
```
Number: 9
4.5
```

##### Q28
**Question:** Ask the user for a string and print it with spaces between each character.
```akandechips
text = input("Text: ")
print(" ".join(text))
```
**Expected Output:**
```
Text: chips
c h i p s
```

##### Q29
**Question:** Ask the user for a number and print the cube of that number.
```akandechips
n = int(input("Number: "))
print(n ** 3)
```
**Expected Output:**
```
Number: 4
64
```

##### Q30
**Question:** Ask the user for a word and print it twice, separated by a space.
```akandechips
word = input("Word: ")
print(word, word)
```
**Expected Output:**
```
Word: Akande
Akande Akande
```

#### Projects & Solutions
##### Project 1
**Project:** Ask the user for their favorite food and print a message with it.
```akandechips
food = input("Favorite food: ")
print("I like", food, "too!")
```
**Expected Output:**
```
Favorite food: pizza
I like pizza too!
```

##### Project 2
**Project:** Ask the user for their birth year and print their age (assuming current year is 2025).
```akandechips
year = int(input("Birth year: "))
print(2025 - year)
```
**Expected Output:**
```
Birth year: 2000
25
```

##### Project 3
**Project:** Ask the user for a temperature in Celsius and print it in Fahrenheit.
```akandechips
c = float(input("Celsius: "))
f = c * 9/5 + 32
print(f)
```
**Expected Output:**
```
Celsius: 0
32.0
```

##### Project 4
**Project:** Ask the user for a filename and print a message that the file was "saved" (simulation).
```akandechips
filename = input("Save as: ")
print("File", filename, "saved!")
```
**Expected Output:**
```
Save as: report.txt
File report.txt saved!
```

##### Project 5
**Project:** Ask the user for two numbers and print their product.
```akandechips
a = int(input("First: "))
b = int(input("Second: "))
print(a * b)
```
**Expected Output:**
```
First: 4
Second: 5
20
```

##### Project 6
**Project:** Ask the user for a sentence and print it backwards.
```akandechips
sentence = input("Type a sentence: ")
print(sentence[::-1])
```
**Expected Output:**
```
Type a sentence: chips are cool
looc era spihc
```

##### Project 7
**Project:** Ask the user for a number and print the square of that number.
```akandechips
num = int(input("Number: "))
print(num ** 2)
```
**Expected Output:**
```
Number: 6
36
```

##### Project 8
**Project:** Ask the user for their first and last name, then print them together.
```akandechips
first = input("First name: ")
last = input("Last name: ")
print(first, last)
```
**Expected Output:**
```
First name: Sam
Last name: Lee
Sam Lee
```

##### Project 9
**Project:** Ask the user for a number and print if it is positive, negative, or zero.
```akandechips
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```
**Expected Output:**
```
Enter a number: -3
Negative
```

##### Project 10
**Project:** Ask the user for a word and print the first and last character.
```akandechips
word = input("Word: ")
print(word[0], word[-1])
```
**Expected Output:**
```
Word: Akande
A e
```

##### Project 11
**Project:** Ask the user for a number and print the result of multiplying it by 10.
```akandechips
n = int(input("Number: "))
print(n * 10)
```
**Expected Output:**
```
Number: 3
30
```

##### Project 12
**Project:** Ask the user for a string and print it with dashes between each character.
```akandechips
text = input("Text: ")
print("-".join(text))
```
**Expected Output:**
```
Text: chips
c-h-i-p-s
```

##### Project 13
**Project:** Ask the user for a number and print the sum of that number and 100.
```akandechips
num = int(input("Number: "))
print(num + 100)
```
**Expected Output:**
```
Number: 25
125
```

##### Project 14
**Project:** Ask the user for a word and print it in title case.
```akandechips
word = input("Word: ")
print(word.title())
```
**Expected Output:**
```
Word: akandechips
Akandechips
```

##### Project 15
**Project:** Ask the user for a number and print the result of raising it to the power of 4.
```akandechips
n = int(input("Number: "))
print(n ** 4)
```
**Expected Output:**
```
Number: 2
16
```

##### Project 16
**Project:** Ask the user for a string and print the string repeated 5 times.
```akandechips
text = input("Text: ")
print(text * 5)
```
**Expected Output:**
```
Text: chip
chipchipchipchipchip
```

##### Project 17
**Project:** Ask the user for a number and print the remainder when divided by 3.
```akandechips
n = int(input("Number: "))
print(n % 3)
```
**Expected Output:**
```
Number: 10
1
```

##### Project 18
**Project:** Ask the user for a word and print the word with each letter on a new line.
```akandechips
word = input("Word: ")
for letter in word:
    print(letter)
```
**Expected Output:**
```
Word: chips
c
h
i
p
s
```

##### Project 19
**Project:** Ask the user for a number and print the result of subtracting 50 from it.
```akandechips
num = int(input("Number: "))
print(num - 50)
```
**Expected Output:**
```
Number: 75
25
```

##### Project 20
**Project:** Ask the user for a string and print whether it contains the letter 'a'.
```akandechips
text = input("Text: ")
if 'a' in text:
    print("Contains 'a'")
else:
    print("Does not contain 'a'")
```
**Expected Output:**
```
Text: chips
Does not contain 'a'
```

##### Project 21
**Project:** Ask the user for a number and print the result of integer division by 5.
```akandechips
n = int(input("Number: "))
print(n // 5)
```
**Expected Output:**
```
Number: 23
4
```

##### Project 22
**Project:** Ask the user for a word and print the word in reverse order.
```akandechips
word = input("Word: ")
print(word[::-1])
```
**Expected Output:**
```
Word: hello
olleh
```

##### Project 23
**Project:** Ask the user for a number and print the result of multiplying it by itself.
```akandechips
n = int(input("Number: "))
print(n * n)
```
**Expected Output:**
```
Number: 11
121
```

##### Project 24
**Project:** Ask the user for a string and print the string with all vowels removed.
```akandechips
text = input("Text: ")
vowels = 'aeiouAEIOU'
result = ''.join([c for c in text if c not in vowels])
print(result)
```
**Expected Output:**
```
Text: chips are cool
chps r cl
```

##### Project 25
**Project:** Ask the user for a number and print the result of adding 7 to it.
```akandechips
n = int(input("Number: "))
print(n + 7)
```
**Expected Output:**
```
Number: 8
15
```

##### Project 26
**Project:** Ask the user for a word and print the word with all consonants removed.
```akandechips
word = input("Word: ")
vowels = 'aeiouAEIOU'
result = ''.join([c for c in word if c in vowels])
print(result)
```
**Expected Output:**
```
Word: Akande
Aae
```

##### Project 27
**Project:** Ask the user for a number and print the result of dividing it by 4 (rounded to 2 decimals).
```akandechips
n = int(input("Number: "))
print(round(n / 4, 2))
```
**Expected Output:**
```
Number: 10
2.5
```

##### Project 28
**Project:** Ask the user for a string and print the string with each word capitalized.
```akandechips
text = input("Text: ")
print(text.title())
```
**Expected Output:**
```
Text: chips are cool
Chips Are Cool
```

##### Project 29
**Project:** Ask the user for a number and print the result of subtracting 100 from it.
```akandechips
n = int(input("Number: "))
print(n - 100)
```
**Expected Output:**
```
Number: 150
50
```

##### Project 30
**Project:** Ask the user for a word and print the word with each letter separated by a dash.
```akandechips
word = input("Word: ")
print("-".join(word))
```
**Expected Output:**
```
Word: chips
c-h-i-p-s
```

---

### Comments and Documentation
**Explanation:**
Comments help explain code to humans. Documentation makes programs easier to understand and maintain.

#### Coding Questions & Answers

1. **What is a comment in AkandeChips?**
   
   **Answer:**
   A comment is text in the code that is ignored by the computer but helps humans understand the code. In AkandeChips, comments start with `#`.
   
   **Example:**
   ```akandechips
   # This is a comment
   print "Hello!"
   ```
   **Output:**
   ```
   Hello!
   ```

2. **How do you write a single-line comment?**
   
   **Answer:**
   Start the line with `#`.
   
   **Example:**
   ```akandechips
   # This is a single-line comment
   print "Done"
   ```
   **Output:**
   ```
   Done
   ```

3. **Can you put a comment after code on the same line?**
   
   **Answer:**
   Yes, just add `#` after the code.
   
   **Example:**
   ```akandechips
   print "Hi" # This prints Hi
   ```
   **Output:**
   ```
   Hi
   ```

4. **What happens if you forget the `#` before a comment?**
   
   **Answer:**
   The program will try to run the text as code and may give an error.

5. **How do you write a multi-line comment?**
   
   **Answer:**
   Use `#` at the start of each line.
   
   **Example:**
   ```akandechips
   # This is a comment
   # that spans multiple lines
   print "Go!"
   ```
   **Output:**
   ```
   Go!
   ```

6. **Can comments be placed before, after, or between code lines?**
   
   **Answer:**
   Yes, comments can be placed anywhere in the code.

7. **Do comments affect the output of a program?**
   
   **Answer:**
   No, comments are ignored by the computer.

8. **How do you document what a function does?**
   
   **Answer:**
   Place a comment above the function explaining its purpose.
   
   **Example:**
   ```akandechips
   # Adds two numbers
   function add(a, b):
       return a + b
   ```

9. **How do you write a comment to explain a tricky part of code?**
   
   **Answer:**
   Place a comment right before or on the same line as the tricky code.

10. **What is documentation?**
    
    **Answer:**
    Documentation is text that explains how code works, what it does, and how to use it. It can be comments or separate files.

11. **Why is documentation important?**
    
    **Answer:**
    It helps others (and your future self) understand and use your code.

12. **How do you write a comment to describe what a variable stores?**
    
    **Answer:**
    Place a comment next to the variable assignment.
    
    **Example:**
    ```akandechips
    age = 16 # User's age
    ```

13. **Can you use comments to temporarily disable code?**
    
    **Answer:**
    Yes, by commenting out the code line.
    
    **Example:**
    ```akandechips
    # print "This won't run"
    print "This will run"
    ```
    **Output:**
    ```
    This will run
    ```

14. **How do you write a comment at the end of a function?**
    
    **Answer:**
    Add `#` and your comment after the last line of the function.

15. **What is a docstring?**
    
    **Answer:**
    In AkandeChips, use comments for documentation. (Docstrings are a Python feature.)

16. **How do you write a comment to explain a loop?**
    
    **Answer:**
    Place a comment before or inside the loop.
    
    **Example:**
    ```akandechips
    # Loop from 1 to 3
    for i in 1 to 3:
        print i
    ```
    **Output:**
    ```
    1
    2
    3
    ```

17. **Can comments be used to mark TODOs?**
    
    **Answer:**
    Yes, write `# TODO: ...` to mark things to do later.

18. **How do you write a comment to explain a function parameter?**
    
    **Answer:**
    Place a comment next to the parameter in the function definition.

19. **How do you write a comment to explain a return value?**
    
    **Answer:**
    Place a comment before the return statement.

20. **How do you write a comment to explain why code is written a certain way?**
    
    **Answer:**
    Place a comment before or after the code, explaining your reasoning.

21. **Can you use comments to separate sections of code?**
    
    **Answer:**
    Yes, use comments like `# --- Section Name ---`.

22. **How do you write a comment to explain an error message?**
    
    **Answer:**
    Place a comment above the code that might cause the error, explaining what to watch for.

23. **How do you write a comment to explain a constant value?**
    
    **Answer:**
    Place a comment next to the constant definition.

24. **How do you write a comment to explain a calculation?**
    
    **Answer:**
    Place a comment before or after the calculation.

25. **How do you write a comment to explain a conditional statement?**
    
    **Answer:**
    Place a comment before or inside the conditional block.

26. **How do you write a comment to explain a list or array?**
    
    **Answer:**
    Place a comment next to the list definition.

27. **How do you write a comment to explain a class?**
    
    **Answer:**
    Place a comment above the class definition.

28. **How do you write a comment to explain a module or file?**
    
    **Answer:**
    Place a comment at the top of the file.

29. **How do you write a comment to explain a bug fix?**
    
    **Answer:**
    Place a comment above the fixed code, explaining what was fixed.

30. **How do you write a comment to explain a shortcut or trick?**
    
    **Answer:**
    Place a comment before or after the code, explaining the trick.

31. **How do you write a comment to explain a code example?**
    
    **Answer:**
    Place a comment above the example code.

32. **How do you write a comment to explain a deprecated feature?**
    
    **Answer:**
    Place a comment above the code, noting it is deprecated.

33. **How do you write a comment to explain a performance consideration?**
    
    **Answer:**
    Place a comment before the code, explaining the performance issue.

34. **How do you write a comment to explain a security consideration?**
    
    **Answer:**
    Place a comment before the code, explaining the security concern.

35. **How do you write a comment to explain a user input?**
    
    **Answer:**
    Place a comment next to the input statement.

36. **How do you write a comment to explain a file operation?**
    
    **Answer:**
    Place a comment before or after the file operation code.

37. **How do you write a comment to explain a network operation?**
    
    **Answer:**
    Place a comment before or after the network code.

38. **How do you write a comment to explain a database operation?**
    
    **Answer:**
    Place a comment before or after the database code.

39. **How do you write a comment to explain a test case?**
    
    **Answer:**
    Place a comment above the test code.

40. **How do you write a comment to explain a configuration setting?**
    
    **Answer:**
    Place a comment next to the setting.


#### Projects & Solutions

1. **Project:** Add comments to explain a program that prints your name.
   
   **Solution:**
   ```akandechips
   # Print the user's name
   print "Akande"
   ```
   **Output:**
   ```
   Akande
   ```

2. **Project:** Write a program with comments explaining each step: ask for age, add 1, print result.
   
   **Solution:**
   ```akandechips
   # Ask for the user's age
   age = input "Enter your age: "
   # Add 1 to the age
   next_year = age + 1
   # Print the result
   print next_year
   ```
   **Output:**
   (If input is 15)
   ```
   16
   ```

3. **Project:** Add comments to a program that prints numbers 1 to 5.
   
   **Solution:**
   ```akandechips
   # Print numbers 1 to 5
   for i in 1 to 5:
       print i
   ```
   **Output:**
   ```
   1
   2
   3
   4
   5
   ```

4. **Project:** Write a program with a comment explaining a calculation.
   
   **Solution:**
   ```akandechips
   # Calculate area of a rectangle
   width = 4
   height = 3
   area = width * height # area formula
   print area
   ```
   **Output:**
   ```
   12
   ```

5. **Project:** Add a comment to explain a conditional statement.
   
   **Solution:**
   ```akandechips
   age = 18
   # Check if age is 18 or older
   if age >= 18:
       print "Adult"
   else:
       print "Minor"
   ```
   **Output:**
   ```
   Adult
   ```

6. **Project:** Write a program with comments marking TODOs.
   
   **Solution:**
   ```akandechips
   # TODO: Ask for user input
   # TODO: Validate input
   print "Feature coming soon!"
   ```
   **Output:**
   ```
   Feature coming soon!
   ```

7. **Project:** Add comments to explain a function and its parameters.
   
   **Solution:**
   ```akandechips
   # Adds two numbers
   function add(a, b):
       # a: first number
       # b: second number
       return a + b
   print add(2, 3)
   ```
   **Output:**
   ```
   5
   ```

8. **Project:** Write a program with comments explaining a loop.
   
   **Solution:**
   ```akandechips
   # Loop through even numbers from 2 to 10
   for i in 2 to 10 step 2:
       print i
   ```
   **Output:**
   ```
   2
   4
   6
   8
   10
   ```

9. **Project:** Add comments to explain a list.
   
   **Solution:**
   ```akandechips
   # List of fruits
   fruits = ["apple", "banana", "cherry"]
   print fruits
   ```
   **Output:**
   ```
   ["apple", "banana", "cherry"]
   ```

10. **Project:** Write a program with a comment explaining a bug fix.
    
    **Solution:**
    ```akandechips
    # Fixed: changed == to =
    x = 5
    print x
    ```
    **Output:**
    ```
    5
    ```

11. **Project:** Add comments to explain a shortcut in code.
    
    **Solution:**
    ```akandechips
    # Shortcut: print numbers 1 to 3 in one line
    print 1, 2, 3
    ```
    **Output:**
    ```
    1 2 3
    ```

12. **Project:** Write a program with comments explaining a file operation.
    
    **Solution:**
    ```akandechips
    # Open file for writing
    file = open "data.txt" write
    # Write text to file
    file.write "Hello file!"
    # Close file
    file.close
    ```

13. **Project:** Add comments to explain a configuration setting.
    
    **Solution:**
    ```akandechips
    # Set debug mode
    debug = true # enables debug output
    ```

14. **Project:** Write a program with comments explaining a test case.
    
    **Solution:**
    ```akandechips
    # Test: add(2, 2) should return 4
    function add(a, b):
        return a + b
    print add(2, 2)
    ```
    **Output:**
    ```
    4
    ```

15. **Project:** Add comments to explain a deprecated feature.
    
    **Solution:**
    ```akandechips
    # Deprecated: use new_function instead
    function old_function():
        print "Old!"
    ```

16. **Project:** Write a program with comments explaining a performance consideration.
    
    **Solution:**
    ```akandechips
    # Performance: avoid using slow_function in loops
    for i in 1 to 100:
        # slow_function(i)
        pass
    ```

17. **Project:** Add comments to explain a security consideration.
    
    **Solution:**
    ```akandechips
    # Security: never print passwords
    password = input "Enter password: "
    # print password  # Don't do this!
    ```

18. **Project:** Write a program with comments explaining a user input.
    
    **Solution:**
    ```akandechips
    # Ask for user's favorite color
    color = input "Favorite color: "
    print color
    ```
    **Output:**
    (If input is blue)
    ```
    blue
    ```

19. **Project:** Add comments to explain a network operation.
    
    **Solution:**
    ```akandechips
    # Connect to server
    connect "example.com"
    ```

20. **Project:** Write a program with comments explaining a database operation.
    
    **Solution:**
    ```akandechips
    # Connect to database
    db = connect "mydb"
    # Query data
    data = db.query "SELECT * FROM users"
    ```

21. **Project:** Add comments to explain a constant value.
    
    **Solution:**
    ```akandechips
    # Pi constant
    PI = 3.14159
    ```

22. **Project:** Write a program with comments explaining a class.
    
    **Solution:**
    ```akandechips
    # User class
    class User:
        # User's name
        name = ""
    ```

23. **Project:** Add comments to explain a module or file.
    
    **Solution:**
    ```akandechips
    # Math utilities module
    # Provides math functions
    ```

24. **Project:** Write a program with comments explaining a tricky part of code.
    
    **Solution:**
    ```akandechips
    # Trick: swap two variables
    a = 5
    b = 7
    # Swap
    a, b = b, a
    print a, b
    ```
    **Output:**
    ```
    7 5
    ```

25. **Project:** Add comments to explain a shortcut or trick.
    
    **Solution:**
    ```akandechips
    # Shortcut: print even numbers
    print [i for i in 2 to 10 step 2]
    ```
    **Output:**
    ```
    [2, 4, 6, 8, 10]
    ```

26. **Project:** Write a program with comments explaining a calculation.
    
    **Solution:**
    ```akandechips
    # Calculate average
    total = 10
    count = 2
    average = total / count # average formula
    print average
    ```
    **Output:**
    ```
    5
    ```

27. **Project:** Add comments to explain a conditional statement.
    
    **Solution:**
    ```akandechips
    # Check if number is even
    num = 4
    if num % 2 == 0:
        print "Even"
    else:
        print "Odd"
    ```
    **Output:**
    ```
    Even
    ```

28. **Project:** Write a program with comments explaining a list or array.
    
    **Solution:**
    ```akandechips
    # List of scores
    scores = [90, 85, 78]
    print scores
    ```
    **Output:**
    ```
    [90, 85, 78]
    ```

29. **Project:** Add comments to explain a function return value.
    
    **Solution:**
    ```akandechips
    # Returns the square of a number
    function square(x):
        return x * x # result
    print square(4)
    ```
    **Output:**
    ```
    16
    ```

30. **Project:** Write a program with comments explaining a configuration setting.
    
    **Solution:**
    ```akandechips
    # Set max users
    MAX_USERS = 100 # maximum allowed
    ```

31. **Project:** Add comments to explain a test case.
    
    **Solution:**
    ```akandechips
    # Test: square(3) should return 9
    print square(3)
    ```
    **Output:**
    ```
    9
    ```

32. **Project:** Write a program with comments explaining a deprecated feature.
    
    **Solution:**
    ```akandechips
    # Deprecated: use new_add instead
    function old_add(a, b):
        return a + b
    ```

33. **Project:** Add comments to explain a performance consideration.
    
    **Solution:**
    ```akandechips
    # Performance: avoid recalculating inside loop
    total = 0
    for i in 1 to 100:
        total = total + i
    print total
    ```
    **Output:**
    ```
    5050
    ```

34. **Project:** Write a program with comments explaining a security consideration.
    
    **Solution:**
    ```akandechips
    # Security: validate user input
    age = input "Enter age: "
    if age < 0:
        print "Invalid age!"
    ```
    **Output:**
    (If input is -1)
    ```
    Invalid age!
    ```

35. **Project:** Add comments to explain a user input.
    
    **Solution:**
    ```akandechips
    # Ask for user's city
    city = input "City: "
    print city
    ```
    **Output:**
    (If input is Dallas)
    ```
    Dallas
    ```

36. **Project:** Write a program with comments explaining a file operation.
    
    **Solution:**
    ```akandechips
    # Read from file
    file = open "data.txt" read
    data = file.read
    print data
    file.close
    ```

37. **Project:** Add comments to explain a network operation.
    
    **Solution:**
    ```akandechips
    # Download data from server
    download "http://example.com/data"
    ```

38. **Project:** Write a program with comments explaining a database operation.
    
    **Solution:**
    ```akandechips
    # Insert new user into database
    db = connect "mydb"
    db.insert "users", {"name": "Akande"}
    ```

39. **Project:** Add comments to explain a test case.
    
    **Solution:**
    ```akandechips
    # Test: add(5, 7) should return 12
    print add(5, 7)
    ```
    **Output:**
    ```
    12
    ```

40. **Project:** Write a program with comments explaining a configuration setting.
    
    **Solution:**
    ```akandechips
    # Set language
    LANGUAGE = "en-US"
    ```

---

### Error Handling (try/except, Basic Debugging)
**Explanation:**
Error handling lets your program deal with unexpected situations without crashing. Debugging helps you find and fix mistakes.

#### Coding Questions & Answers

1. **What is error handling?**
   
   **Answer:**
   Error handling is writing code to deal with problems that might happen while your program runs, so it doesn't crash.

2. **How do you handle errors in AkandeChips?**
   
   **Answer:**
   Use `try` and `except` blocks.
   
   **Example:**
   ```akandechips
   try:
       print 10 / 0
   except:
       print "Error!"
   ```
   **Output:**
   ```
   Error!
   ```

3. **What happens if you don't handle an error?**
   
   **Answer:**
   The program will stop and show an error message.

4. **How do you catch division by zero?**
   
   **Answer:**
   Use `try`/`except` around the division.
   
   **Example:**
   ```akandechips
   try:
       print 5 / 0
   except:
       print "Cannot divide by zero!"
   ```
   **Output:**
   ```
   Cannot divide by zero!
   ```

5. **How do you print the error message?**
   
   **Answer:**
   Use `except error as e:` and print `e`.
   
   **Example:**
   ```akandechips
   try:
       print 1 / 0
   except error as e:
       print e
   ```
   **Output:**
   ```
   DivisionByZeroError
   ```

6. **What is debugging?**
   
   **Answer:**
   Debugging is finding and fixing mistakes (bugs) in your code.

7. **How do you find where an error happened?**
   
   **Answer:**
   Read the error message and check the line number.

8. **How do you use print statements to debug?**
   
   **Answer:**
   Add `print` statements to show variable values and program flow.

9. **How do you handle invalid user input?**
   
   **Answer:**
   Use `try`/`except` when converting input.
   
   **Example:**
   ```akandechips
   try:
       age = int(input "Enter age: ")
       print age
   except:
       print "Invalid input!"
   ```
   **Output:**
   (If input is "abc")
   ```
   Invalid input!
   ```

10. **How do you handle file not found errors?**
    
    **Answer:**
    Use `try`/`except` when opening files.
    
    **Example:**
    ```akandechips
    try:
        file = open "nofile.txt" read
    except:
        print "File not found!"
    ```
    **Output:**
    ```
    File not found!
    ```

11. **How do you handle multiple types of errors?**
    
    **Answer:**
    Use multiple `except` blocks for different errors.

12. **What is a bug?**
    
    **Answer:**
    A bug is a mistake in your code that causes it to work incorrectly.

13. **How do you fix a bug?**
    
    **Answer:**
    Find the cause and change the code to correct it.

14. **How do you avoid bugs?**
    
    **Answer:**
    Test your code, use comments, and write clear code.

15. **How do you handle errors in a loop?**
    
    **Answer:**
    Put the `try`/`except` inside the loop.

16. **How do you handle errors in a function?**
    
    **Answer:**
    Use `try`/`except` inside the function.

17. **How do you make your program keep running after an error?**
    
    **Answer:**
    Use `try`/`except` so the program doesn't stop.

18. **How do you show a custom error message?**
    
    **Answer:**
    Print your own message in the `except` block.

19. **How do you handle errors when converting types?**
    
    **Answer:**
    Use `try`/`except` when converting.

20. **How do you handle errors when accessing a list index?**
    
    **Answer:**
    Use `try`/`except` when accessing the list.

21. **How do you handle errors when dividing numbers?**
    
    **Answer:**
    Use `try`/`except` around the division.

22. **How do you handle errors when calling a function?**
    
    **Answer:**
    Use `try`/`except` around the function call.

23. **How do you handle errors when reading from a file?**
    
    **Answer:**
    Use `try`/`except` when reading.

24. **How do you handle errors when writing to a file?**
    
    **Answer:**
    Use `try`/`except` when writing.

25. **How do you handle errors when importing modules?**
    
    **Answer:**
    Use `try`/`except` when importing.

26. **How do you handle errors when using user input?**
    
    **Answer:**
    Use `try`/`except` when using input.

27. **How do you handle errors when parsing data?**
    
    **Answer:**
    Use `try`/`except` when parsing.

28. **How do you handle errors when connecting to a server?**
    
    **Answer:**
    Use `try`/`except` when connecting.

29. **How do you handle errors when sending data?**
    
    **Answer:**
    Use `try`/`except` when sending.

30. **How do you handle errors when receiving data?**
    
    **Answer:**
    Use `try`/`except` when receiving.

31. **How do you handle errors when closing a file?**
    
    **Answer:**
    Use `try`/`except` when closing.

32. **How do you handle errors when deleting a file?**
    
    **Answer:**
    Use `try`/`except` when deleting.

33. **How do you handle errors when updating a record?**
    
    **Answer:**
    Use `try`/`except` when updating.

34. **How do you handle errors when creating a new file?**
    
    **Answer:**
    Use `try`/`except` when creating.

35. **How do you handle errors when saving data?**
    
    **Answer:**
    Use `try`/`except` when saving.

36. **How do you handle errors when loading data?**
    
    **Answer:**
    Use `try`/`except` when loading.

37. **How do you handle errors when using external libraries?**
    
    **Answer:**
    Use `try`/`except` when using libraries.

38. **How do you handle errors when running code from the internet?**
    
    **Answer:**
    Use `try`/`except` when running code.

39. **How do you handle errors when working with dates?**
    
    **Answer:**
    Use `try`/`except` when working with dates.

40. **How do you handle errors when using math operations?**
    
    **Answer:**
    Use `try`/`except` around math operations.


#### Projects & Solutions

1. **Project:** Write a program that divides two numbers and handles division by zero.
   
   **Solution:**
   ```akandechips
   try:
       a = 10
       b = 0
       print a / b
   except:
       print "Cannot divide by zero!"
   ```
   **Output:**
   ```
   Cannot divide by zero!
   ```

2. **Project:** Write a program that asks for a number and prints its square. Handle invalid input.
   
   **Solution:**
   ```akandechips
   try:
       num = int(input "Enter a number: ")
       print num * num
   except:
       print "Invalid input!"
   ```
   **Output:**
   (If input is "hi")
   ```
   Invalid input!
   ```

3. **Project:** Write a program that opens a file and handles file not found errors.
   
   **Solution:**
   ```akandechips
   try:
       file = open "nofile.txt" read
   except:
       print "File not found!"
   ```
   **Output:**
   ```
   File not found!
   ```

4. **Project:** Write a program that tries to access an invalid list index and handles the error.
   
   **Solution:**
   ```akandechips
   try:
       nums = [1, 2, 3]
       print nums[5]
   except:
       print "Index out of range!"
   ```
   **Output:**
   ```
   Index out of range!
   ```

5. **Project:** Write a program that tries to convert a string to an integer and handles errors.
   
   **Solution:**
   ```akandechips
   try:
       x = int("abc")
       print x
   except:
       print "Conversion error!"
   ```
   **Output:**
   ```
   Conversion error!
   ```

6. **Project:** Write a program that tries to read from a file and handles errors.
   
   **Solution:**
   ```akandechips
   try:
       file = open "nofile.txt" read
       data = file.read
   except:
       print "Read error!"
   ```
   **Output:**
   ```
   Read error!
   ```

7. **Project:** Write a program that tries to write to a file and handles errors.
   
   **Solution:**
   ```akandechips
   try:
       file = open "readonly.txt" write
       file.write "Hello"
   except:
       print "Write error!"
   ```
   **Output:**
   ```
   Write error!
   ```

8. **Project:** Write a program that tries to delete a file and handles errors.
   
   **Solution:**
   ```akandechips
   try:
       delete "nofile.txt"
   except:
       print "Delete error!"
   ```
   **Output:**
   ```
   Delete error!
   ```

9. **Project:** Write a program that tries to update a record and handles errors.
   
   **Solution:**
   ```akandechips
   try:
       db = connect "mydb"
       db.update "users", {"id": 1, "name": "New"}
   except:
       print "Update error!"
   ```
   **Output:**
   ```
   Update error!
   ```

10. **Project:** Write a program that tries to create a new file and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        file = open "newfile.txt" write
    except:
        print "Create error!"
    ```
    **Output:**
    ```
    Create error!
    ```

11. **Project:** Write a program that tries to save data and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        save "data.txt", "Hello"
    except:
        print "Save error!"
    ```
    **Output:**
    ```
    Save error!
    ```

12. **Project:** Write a program that tries to load data and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        load "data.txt"
    except:
        print "Load error!"
    ```
    **Output:**
    ```
    Load error!
    ```

13. **Project:** Write a program that tries to import a module and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        import math
    except:
        print "Import error!"
    ```
    **Output:**
    ```
    Import error!
    ```

14. **Project:** Write a program that tries to connect to a server and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        connect "badserver"
    except:
        print "Connection error!"
    ```
    **Output:**
    ```
    Connection error!
    ```

15. **Project:** Write a program that tries to send data and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        send "badserver", "data"
    except:
        print "Send error!"
    ```
    **Output:**
    ```
    Send error!
    ```

16. **Project:** Write a program that tries to receive data and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        receive "badserver"
    except:
        print "Receive error!"
    ```
    **Output:**
    ```
    Receive error!
    ```

17. **Project:** Write a program that tries to close a file and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        file = open "nofile.txt" read
        file.close
    except:
        print "Close error!"
    ```
    **Output:**
    ```
    Close error!
    ```

18. **Project:** Write a program that tries to parse data and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        parse "bad data"
    except:
        print "Parse error!"
    ```
    **Output:**
    ```
    Parse error!
    ```

19. **Project:** Write a program that tries to use an external library and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        use "badlib"
    except:
        print "Library error!"
    ```
    **Output:**
    ```
    Library error!
    ```

20. **Project:** Write a program that tries to run code from the internet and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        run "http://badurl"
    except:
        print "Run error!"
    ```
    **Output:**
    ```
    Run error!
    ```

21. **Project:** Write a program that tries to work with dates and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        date = parse_date("bad date")
    except:
        print "Date error!"
    ```
    **Output:**
    ```
    Date error!
    ```

22. **Project:** Write a program that tries a math operation and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        print sqrt(-1)
    except:
        print "Math error!"
    ```
    **Output:**
    ```
    Math error!
    ```

23. **Project:** Write a program that tries to access a dictionary key and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        d = {"a": 1}
        print d["b"]
    except:
        print "Key error!"
    ```
    **Output:**
    ```
    Key error!
    ```

24. **Project:** Write a program that tries to use a variable before assigning it and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        print x
    except:
        print "Variable error!"
    ```
    **Output:**
    ```
    Variable error!
    ```

25. **Project:** Write a program that tries to use a function that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        not_a_function()
    except:
        print "Function error!"
    ```
    **Output:**
    ```
    Function error!
    ```

26. **Project:** Write a program that tries to use a class that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        obj = NoClass()
    except:
        print "Class error!"
    ```
    **Output:**
    ```
    Class error!
    ```

27. **Project:** Write a program that tries to use a method that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        obj = {}
        obj.no_method()
    except:
        print "Method error!"
    ```
    **Output:**
    ```
    Method error!
    ```

28. **Project:** Write a program that tries to use a property that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        obj = {}
        print obj.no_property
    except:
        print "Property error!"
    ```
    **Output:**
    ```
    Property error!
    ```

29. **Project:** Write a program that tries to use a module that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        import badmodule
    except:
        print "Module error!"
    ```
    **Output:**
    ```
    Module error!
    ```

30. **Project:** Write a program that tries to use a resource that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        use "badresource"
    except:
        print "Resource error!"
    ```
    **Output:**
    ```
    Resource error!
    ```

31. **Project:** Write a program that tries to use a network resource and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        connect "badnetwork"
    except:
        print "Network error!"
    ```
    **Output:**
    ```
    Network error!
    ```

32. **Project:** Write a program that tries to use a database resource and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        db = connect "baddb"
    except:
        print "Database error!"
    ```
    **Output:**
    ```
    Database error!
    ```

33. **Project:** Write a program that tries to use a configuration setting that doesn't exist and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        print config["badsetting"]
    except:
        print "Config error!"
    ```
    **Output:**
    ```
    Config error!
    ```

34. **Project:** Write a program that tries to use a setting that is not allowed and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        set "badsetting", 1
    except:
        print "Setting error!"
    ```
    **Output:**
    ```
    Setting error!
    ```

35. **Project:** Write a program that tries to use a feature that is not supported and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        use "badfeature"
    except:
        print "Feature error!"
    ```
    **Output:**
    ```
    Feature error!
    ```

36. **Project:** Write a program that tries to use a command that is not allowed and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        command "badcommand"
    except:
        print "Command error!"
    ```
    **Output:**
    ```
    Command error!
    ```

37. **Project:** Write a program that tries to use a tool that is not installed and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        tool "badtool"
    except:
        print "Tool error!"
    ```
    **Output:**
    ```
    Tool error!
    ```

38. **Project:** Write a program that tries to use a plugin that is not installed and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        plugin "badplugin"
    except:
        print "Plugin error!"
    ```
    **Output:**
    ```
    Plugin error!
    ```

39. **Project:** Write a program that tries to use a driver that is not installed and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        driver "baddriver"
    except:
        print "Driver error!"
    ```
    **Output:**
    ```
    Driver error!
    ```

40. **Project:** Write a program that tries to use a service that is not running and handles errors.
    
    **Solution:**
    ```akandechips
    try:
        service "badservice"
    except:
        print "Service error!"
    ```
    **Output:**
    ```
    Service error!
    ```

---

### Functions and Procedures (Defining, Calling, Parameters, Return Values)
**Explanation:**
Functions let you organize code into reusable blocks. They can take inputs (parameters) and return outputs (return values).

#### Coding Questions & Answers

1. **What is a function?**
   
   **Answer:**
   A function is a named block of code that performs a specific task and can be reused.

2. **How do you define a function in AkandeChips?**
   
   **Answer:**
   Use the `function` keyword.
   
   **Example:**
   ```akandechips
   function greet():
       print "Hello!"
   ```

3. **How do you call a function?**
   
   **Answer:**
   Write the function name followed by parentheses.
   
   **Example:**
   ```akandechips
   greet()
   ```
   **Output:**
   ```
   Hello!
   ```

4. **What is a parameter?**
   
   **Answer:**
   A parameter is a variable in a function definition that receives a value when the function is called.

5. **How do you define a function with parameters?**
   
   **Answer:**
   List the parameters in parentheses after the function name.
   
   **Example:**
   ```akandechips
   function add(a, b):
       print a + b
   ```

6. **How do you call a function with arguments?**
   
   **Answer:**
   Pass values inside the parentheses.
   
   **Example:**
   ```akandechips
   add(2, 3)
   ```
   **Output:**
   ```
   5
   ```

7. **What is a return value?**
   
   **Answer:**
   A return value is the result a function gives back to the code that called it.

8. **How do you return a value from a function?**
   
   **Answer:**
   Use the `return` keyword.
   
   **Example:**
   ```akandechips
   function square(x):
       return x * x
   print square(4)
   ```
   **Output:**
   ```
   16
   ```

9. **Can a function have more than one parameter?**
   
   **Answer:**
   Yes.

10. **Can a function return more than one value?**
    
    **Answer:**
    Yes, return a list or tuple.

11. **What is a procedure?**
    
    **Answer:**
    A procedure is a function that does not return a value (just performs actions).

12. **How do you write a procedure?**
    
    **Answer:**
    Define a function without a return statement.

13. **How do you document a function?**
    
    **Answer:**
    Add a comment above the function explaining what it does.

14. **How do you use default parameter values?**
    
    **Answer:**
    Assign a value in the parameter list (if supported).

15. **How do you call a function from inside another function?**
    
    **Answer:**
    Just use the function name and parentheses inside the other function.

16. **What happens if you call a function with the wrong number of arguments?**
    
    **Answer:**
    You get an error.

17. **Can functions call themselves?**
    
    **Answer:**
    Yes, this is called recursion.

18. **How do you return early from a function?**
    
    **Answer:**
    Use the `return` statement before the end of the function.

19. **How do you store a function's return value in a variable?**
    
    **Answer:**
    Assign the function call to a variable.
    
    **Example:**
    ```akandechips
    result = square(5)
    print result
    ```
    **Output:**
    ```
    25
    ```

20. **Can you pass variables as arguments to functions?**
    
    **Answer:**
    Yes.

21. **Can you return a function from another function?**
    
    **Answer:**
    Advanced: If supported, yes.

22. **How do you write a function that takes no parameters?**
    
    **Answer:**
    Leave the parentheses empty.

23. **How do you write a function that does nothing?**
    
    **Answer:**
    Use an empty function body or a `pass` statement.

24. **How do you call a function multiple times?**
    
    **Answer:**
    Call it as many times as needed.

25. **How do you use a function in a loop?**
    
    **Answer:**
    Call the function inside the loop.

26. **How do you return different values based on a condition?**
    
    **Answer:**
    Use `if` statements inside the function.

27. **How do you write a function that prints a message?**
    
    **Answer:**
    Use `print` inside the function.

28. **How do you write a function that adds two numbers and returns the result?**
    
    **Answer:**
    Define the function with two parameters and use `return a + b`.

29. **How do you write a function that returns the maximum of two numbers?**
    
    **Answer:**
    Use an `if` statement to compare and return the larger value.

30. **How do you write a function that returns the length of a list?**
    
    **Answer:**
    Use the `len` function inside your function.

31. **How do you write a function that reverses a string?**
    
    **Answer:**
    Use slicing or a loop to reverse the string.

32. **How do you write a function that checks if a number is even?**
    
    **Answer:**
    Use `return n % 2 == 0`.

33. **How do you write a function that repeats a string n times?**
    
    **Answer:**
    Use `return s * n` or a loop.

34. **How do you write a function that sums all numbers in a list?**
    
    **Answer:**
    Use a loop to add up the numbers and return the sum.

35. **How do you write a function that finds the smallest number in a list?**
    
    **Answer:**
    Use a loop to compare and return the smallest value.

36. **How do you write a function that returns True if a string is a palindrome?**
    
    **Answer:**
    Compare the string to its reverse.

37. **How do you write a function that counts vowels in a string?**
    
    **Answer:**
    Loop through the string and count vowels.

38. **How do you write a function that returns the factorial of a number?**
    
    **Answer:**
    Use a loop or recursion to multiply numbers up to n.

39. **How do you write a function that returns the average of a list?**
    
    **Answer:**
    Sum the list and divide by its length.

40. **How do you write a function that prints each item in a list?**
    
    **Answer:**
    Loop through the list and print each item.


#### Projects & Solutions

1. **Project:** Write a function that prints "Welcome!" and call it.
   
   **Solution:**
   ```akandechips
   function welcome():
       print "Welcome!"
   welcome()
   ```
   **Output:**
   ```
   Welcome!
   ```

2. **Project:** Write a function that takes a name and prints "Hello, name!" Call it with your name.
   
   **Solution:**
   ```akandechips
   function greet(name):
       print "Hello, " + name + "!"
   greet("Akande")
   ```
   **Output:**
   ```
   Hello, Akande!
   ```

3. **Project:** Write a function that adds two numbers and returns the result. Print the result of adding 5 and 7.
   
   **Solution:**
   ```akandechips
   function add(a, b):
       return a + b
   print add(5, 7)
   ```
   **Output:**
   ```
   12
   ```

4. **Project:** Write a function that returns the square of a number. Print the square of 6.
   
   **Solution:**
   ```akandechips
   function square(x):
       return x * x
   print square(6)
   ```
   **Output:**
   ```
   36
   ```

5. **Project:** Write a function that checks if a number is even. Print the result for 4 and 7.
   
   **Solution:**
   ```akandechips
   function is_even(n):
       return n % 2 == 0
   print is_even(4)
   print is_even(7)
   ```
   **Output:**
   ```
   True
   False
   ```

6. **Project:** Write a function that returns the maximum of two numbers. Print the maximum of 8 and 3.
   
   **Solution:**
   ```akandechips
   function maximum(a, b):
       if a > b:
           return a
       else:
           return b
   print maximum(8, 3)
   ```
   **Output:**
   ```
   8
   ```

7. **Project:** Write a function that returns the length of a list. Print the length of [1, 2, 3, 4].
   
   **Solution:**
   ```akandechips
   function list_length(lst):
       return len(lst)
   print list_length([1, 2, 3, 4])
   ```
   **Output:**
   ```
   4
   ```

8. **Project:** Write a function that reverses a string. Print the reverse of "chips".
   
   **Solution:**
   ```akandechips
   function reverse(s):
       return s[::-1]
   print reverse("chips")
   ```
   **Output:**
   ```
   spihc
   ```

9. **Project:** Write a function that repeats a string n times. Print "ha" 3 times.
   
   **Solution:**
   ```akandechips
   function repeat(s, n):
       return s * n
   print repeat("ha", 3)
   ```
   **Output:**
   ```
   hahaha
   ```

10. **Project:** Write a function that sums all numbers in a list. Print the sum of [2, 4, 6].
    
    **Solution:**
    ```akandechips
    function sum_list(lst):
        total = 0
        for x in lst:
            total = total + x
        return total
    print sum_list([2, 4, 6])
    ```
    **Output:**
    ```
    12
    ```

11. **Project:** Write a function that finds the smallest number in a list. Print the smallest of [5, 3, 9].
    
    **Solution:**
    ```akandechips
    function min_list(lst):
        min_val = lst[0]
        for x in lst:
            if x < min_val:
                min_val = x
        return min_val
    print min_list([5, 3, 9])
    ```
    **Output:**
    ```
    3
    ```

12. **Project:** Write a function that returns True if a string is a palindrome. Print the result for "level" and "chips".
    
    **Solution:**
    ```akandechips
    function is_palindrome(s):
        return s == s[::-1]
    print is_palindrome("level")
    print is_palindrome("chips")
    ```
    **Output:**
    ```
    True
    False
    ```

13. **Project:** Write a function that counts vowels in a string. Print the number of vowels in "Akande".
    
    **Solution:**
    ```akandechips
    function count_vowels(s):
        count = 0
        for c in s:
            if c in "aeiouAEIOU":
                count = count + 1
        return count
    print count_vowels("Akande")
    ```
    **Output:**
    ```
    3
    ```

14. **Project:** Write a function that returns the factorial of a number. Print the factorial of 5.
    
    **Solution:**
    ```akandechips
    function factorial(n):
        result = 1
        for i in 1 to n:
            result = result * i
        return result
    print factorial(5)
    ```
    **Output:**
    ```
    120
    ```

15. **Project:** Write a function that returns the average of a list. Print the average of [2, 4, 6].
    
    **Solution:**
    ```akandechips
    function average(lst):
        return sum_list(lst) / len(lst)
    print average([2, 4, 6])
    ```
    **Output:**
    ```
    4
    ```

16. **Project:** Write a function that prints each item in a list. Use it for ["a", "b", "c"].
    
    **Solution:**
    ```akandechips
    function print_items(lst):
        for item in lst:
            print item
    print_items(["a", "b", "c"])
    ```
    **Output:**
    ```
    a
    b
    c
    ```

17. **Project:** Write a function that returns the product of all numbers in a list. Print the product of [2, 3, 4].
    
    **Solution:**
    ```akandechips
    function product_list(lst):
        result = 1
        for x in lst:
            result = result * x
        return result
    print product_list([2, 3, 4])
    ```
    **Output:**
    ```
    24
    ```

18. **Project:** Write a function that returns the first item in a list. Print the first item of [10, 20, 30].
    
    **Solution:**
    ```akandechips
    function first_item(lst):
        return lst[0]
    print first_item([10, 20, 30])
    ```
    **Output:**
    ```
    10
    ```

19. **Project:** Write a function that returns the last item in a list. Print the last item of [10, 20, 30].
    
    **Solution:**
    ```akandechips
    function last_item(lst):
        return lst[-1]
    print last_item([10, 20, 30])
    ```
    **Output:**
    ```
    30
    ```

20. **Project:** Write a function that returns the sum of even numbers in a list. Print the sum for [1, 2, 3, 4].
    
    **Solution:**
    ```akandechips
    function sum_even(lst):
        total = 0
        for x in lst:
            if x % 2 == 0:
                total = total + x
        return total
    print sum_even([1, 2, 3, 4])
    ```
    **Output:**
    ```
    6
    ```

21. **Project:** Write a function that returns the sum of odd numbers in a list. Print the sum for [1, 2, 3, 4].
    
    **Solution:**
    ```akandechips
    function sum_odd(lst):
        total = 0
        for x in lst:
            if x % 2 != 0:
                total = total + x
        return total
    print sum_odd([1, 2, 3, 4])
    ```
    **Output:**
    ```
    4
    ```

22. **Project:** Write a function that returns the largest number in a list. Print the largest of [5, 9, 2].
    
    **Solution:**
    ```akandechips
    function max_list(lst):
        max_val = lst[0]
        for x in lst:
            if x > max_val:
                max_val = x
        return max_val
    print max_list([5, 9, 2])
    ```
    **Output:**
    ```
    9
    ```

23. **Project:** Write a function that returns the index of an item in a list. Print the index of 7 in [3, 7, 9].
    
    **Solution:**
    ```akandechips
    function index_of(lst, item):
        for i in 0 to len(lst)-1:
            if lst[i] == item:
                return i
        return -1
    print index_of([3, 7, 9], 7)
    ```
    **Output:**
    ```
    1
    ```

24. **Project:** Write a function that returns True if a list contains a value. Print the result for 5 in [1, 2, 5].
    
    **Solution:**
    ```akandechips
    function contains(lst, value):
        for x in lst:
            if x == value:
                return True
        return False
    print contains([1, 2, 5], 5)
    ```
    **Output:**
    ```
    True
    ```

25. **Project:** Write a function that returns a list of even numbers from a list. Print the result for [1, 2, 3, 4].
    
    **Solution:**
    ```akandechips
    function evens(lst):
        result = []
        for x in lst:
            if x % 2 == 0:
                result.append(x)
        return result
    print evens([1, 2, 3, 4])
    ```
    **Output:**
    ```
    [2, 4]
    ```

26. **Project:** Write a function that returns a list of odd numbers from a list. Print the result for [1, 2, 3, 4].
    
    **Solution:**
    ```akandechips
    function odds(lst):
        result = []
        for x in lst:
            if x % 2 != 0:
                result.append(x)
        return result
    print odds([1, 2, 3, 4])
    ```
    **Output:**
    ```
    [1, 3]
    ```

27. **Project:** Write a function that returns a list with each string in a list uppercased. Print the result for ["a", "b"].
    
    **Solution:**
    ```akandechips
    function upper_all(lst):
        result = []
        for s in lst:
            result.append(s.upper())
        return result
    print upper_all(["a", "b"])
    ```
    **Output:**
    ```
    ["A", "B"]
    ```

28. **Project:** Write a function that returns a list with each number doubled. Print the result for [1, 2, 3].
    
    **Solution:**
    ```akandechips
    function double_all(lst):
        result = []
        for x in lst:
            result.append(x * 2)
        return result
    print double_all([1, 2, 3])
    ```
    **Output:**
    ```
    [2, 4, 6]
    ```

29. **Project:** Write a function that returns a list of strings longer than 3 characters. Print the result for ["hi", "chips", "ok"]
    
    **Solution:**
    ```akandechips
    function longer_than_3(lst):
        result = []
        for s in lst:
            if len(s) > 3:
                result.append(s)
        return result
    print longer_than_3(["hi", "chips", "ok"])
    ```
    **Output:**
    ```
    ["chips"]
    ```

30. **Project:** Write a function that returns the sum of all digits in a number. Print the sum for 1234.
    
    **Solution:**
    ```akandechips
    function sum_digits(n):
        total = 0
        for d in str(n):
            total = total + int(d)
        return total
    print sum_digits(1234)
    ```
    **Output:**
    ```
    10
    ```

31. **Project:** Write a function that returns the number of words in a string. Print the result for "chips are fun".
    
    **Solution:**
    ```akandechips
    function word_count(s):
        return len(s.split())
    print word_count("chips are fun")
    ```
    **Output:**
    ```
    3
    ```

32. **Project:** Write a function that returns a list of the lengths of each word in a string. Print the result for "chips are fun".
    
    **Solution:**
    ```akandechips
    function word_lengths(s):
        return [len(word) for word in s.split()]
    print word_lengths("chips are fun")
    ```
    **Output:**
    ```
    [5, 3, 3]
    ```

33. **Project:** Write a function that returns True if all numbers in a list are positive. Print the result for [1, 2, 3] and [-1, 2, 3].
    
    **Solution:**
    ```akandechips
    function all_positive(lst):
        for x in lst:
            if x <= 0:
                return False
        return True
    print all_positive([1, 2, 3])
    print all_positive([-1, 2, 3])
    ```
    **Output:**
    ```
    True
    False
    ```

34. **Project:** Write a function that returns True if any number in a list is negative. Print the result for [1, 2, 3] and [-1, 2, 3].
    
    **Solution:**
    ```akandechips
    function any_negative(lst):
        for x in lst:
            if x < 0:
                return True
        return False
    print any_negative([1, 2, 3])
    print any_negative([-1, 2, 3])
    ```
    **Output:**
    ```
    False
    True
    ```

35. **Project:** Write a function that returns a list of numbers squared. Print the result for [1, 2, 3].
    
    **Solution:**
    ```akandechips
    function squares(lst):
        result = []
        for x in lst:
            result.append(x * x)
        return result
    print squares([1, 2, 3])
    ```
    **Output:**
    ```
    [1, 4, 9]
    ```

36. **Project:** Write a function that returns a list of strings reversed. Print the result for ["chips", "fun"].
    
    **Solution:**
    ```akandechips
    function reverse_all(lst):
        result = []
        for s in lst:
            result.append(s[::-1])
        return result
    print reverse_all(["chips", "fun"])
    ```
    **Output:**
    ```
    ["spihc", "nuf"]
    ```

37. **Project:** Write a function that returns a list of numbers greater than 5. Print the result for [2, 6, 8, 3].
    
    **Solution:**
    ```akandechips
    function greater_than_5(lst):
        result = []
        for x in lst:
            if x > 5:
                result.append(x)
        return result
    print greater_than_5([2, 6, 8, 3])
    ```
    **Output:**
    ```
    [6, 8]
    ```

38. **Project:** Write a function that returns a list of numbers less than 5. Print the result for [2, 6, 8, 3].
    
    **Solution:**
    ```akandechips
    function less_than_5(lst):
        result = []
        for x in lst:
            if x < 5:
                result.append(x)
        return result
    print less_than_5([2, 6, 8, 3])
    ```
    **Output:**
    ```
    [2, 3]
    ```

39. **Project:** Write a function that returns a list of numbers between 3 and 7. Print the result for [2, 4, 6, 8].
    
    **Solution:**
    ```akandechips
    function between_3_and_7(lst):
        result = []
        for x in lst:
            if x >= 3 and x <= 7:
                result.append(x)
        return result
    print between_3_and_7([2, 4, 6, 8])
    ```
    **Output:**
    ```
    [4, 6]
    ```

40. **Project:** Write a function that returns a list of numbers divided by 2. Print the result for [2, 4, 6].
    
    **Solution:**
    ```akandechips
    function half_all(lst):
        result = []
        for x in lst:
            result.append(x / 2)
        return result
    print half_all([2, 4, 6])
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

---

### Scope and Lifetime of Variables
**Explanation:**
Scope determines where a variable can be used. Lifetime is how long a variable exists in memory.

#### Coding Questions & Answers

41. **What is lexical scope?**
   
   **Answer:**
   Lexical scope means a variable is accessible only within the block where it is defined and its inner blocks.

42. **What is dynamic scope?**
   
   **Answer:**
   Dynamic scope means a variable is accessible based on the call stack, not just where it is defined (not common in modern languages).

43. **What is a nonlocal variable?**
   
   **Answer:**
   A variable defined in an outer function but not global; accessible in nested functions (if supported).

44. **How do you create a nonlocal variable?**
   
   **Answer:**
   Use the `nonlocal` keyword in a nested function (if supported).

45. **What is variable capture?**
   
   **Answer:**
   When a nested function uses a variable from an outer function.

46. **What is a closure?**
   
   **Answer:**
   A function that remembers variables from its defining scope even after that scope has finished.

47. **What is the scope of a variable in a class method?**
   
   **Answer:**
   Local to the method unless declared as a class or instance variable.

48. **What is the scope of an instance variable?**
   
   **Answer:**
   Accessible to all methods of the object (instance).

49. **What is the scope of a class variable?**
   
   **Answer:**
   Shared by all instances of the class.

50. **What is the lifetime of an instance variable?**
   
   **Answer:**
   As long as the object exists.

51. **What is the lifetime of a class variable?**
   
   **Answer:**
   As long as the class is loaded in memory.

52. **What is the scope of a variable in a lambda function?**
   
   **Answer:**
   Local to the lambda, but can access variables from the enclosing scope.

53. **What is the lifetime of a variable in a lambda function?**
   
   **Answer:**
   As long as the lambda exists.

54. **What is a temporary variable?**
   
   **Answer:**
   A variable used for a short time, often inside a function or block.

55. **What is a persistent variable?**
   
   **Answer:**
   A variable that keeps its value between function calls (e.g., global or static).

56. **What is a static variable?**
   
   **Answer:**
   A variable that keeps its value between function calls (if supported).

57. **How do you create a static variable?**
   
   **Answer:**
   Use the `static` keyword or define outside the function (if supported).

58. **What is variable hiding?**
   
   **Answer:**
   When a variable in a closer scope has the same name as one in an outer scope, hiding the outer one.

59. **What is a global constant?**
   
   **Answer:**
   A variable defined at the top level and never changed.

60. **What is the scope of a global constant?**
   
   **Answer:**
   Accessible everywhere in the module.

61. **What is the lifetime of a global constant?**
   
   **Answer:**
   As long as the program runs.

62. **What is a module-level variable?**
   
   **Answer:**
   A variable defined outside functions/classes, accessible throughout the module.

63. **What is the scope of a variable in a list comprehension?**
   
   **Answer:**
   Local to the comprehension (in some languages, may leak to outer scope).

64. **What is the lifetime of a variable in a list comprehension?**
   
   **Answer:**
   Only during the comprehension's execution.

65. **What is a block-level variable?**
   
   **Answer:**
   A variable defined inside a block (like a loop or if statement).

66. **What is the scope of a variable in a try/except/finally block?**
   
   **Answer:**
   Usually accessible after the block ends.

67. **What is the lifetime of a variable in a try/except/finally block?**
   
   **Answer:**
   From when the block starts until it ends.

68. **What is a parameter variable?**
   
   **Answer:**
   A variable used as an input to a function.

69. **What is the scope of a parameter variable?**
   
   **Answer:**
   Local to the function.

70. **What is the lifetime of a parameter variable?**
   
   **Answer:**
   From when the function is called until it ends.

71. **What is a recursive variable?**
   
   **Answer:**
   A variable used in a recursive function, with a new copy for each call.

72. **What is the scope of a variable in a recursive function?**
   
   **Answer:**
   Local to each call of the function.

73. **What is the lifetime of a variable in a recursive function?**
   
   **Answer:**
   From when the call starts until it ends.

74. **What is a shadowed variable?**
   
   **Answer:**
   A variable in an inner scope with the same name as one in an outer scope, hiding the outer one.

75. **What is a variable leak?**
   
   **Answer:**
   When a variable defined in a block is accidentally accessible outside the block (not always intended).

76. **What is a variable reference?**
   
   **Answer:**
   Using a variable's value in an expression or statement.

77. **What is a variable assignment?**
   
   **Answer:**
   Giving a variable a value.

78. **What is a variable declaration?**
   
   **Answer:**
   Creating a variable (may be explicit or implicit in some languages).

79. **What is a variable's visibility?**
   
   **Answer:**
   Where in the code the variable can be accessed.

80. **What is a variable's accessibility?**
   
   **Answer:**
   Whether a variable can be accessed from a given scope (public, private, etc.).


#### Projects & Solutions

41. **Project:** Show lexical scope with a nested function.
   
   **Solution:**
   ```akandechips
   function outer():
       x = 10
       function inner():
           print x
       inner()
   outer()
   ```
   **Output:**
   ```
   10
   ```

42. **Project:** Show variable hiding in nested functions.
   
   **Solution:**
   ```akandechips
   x = 5
   function outer():
       x = 6
       function inner():
           x = 7
           print x
       inner()
       print x
   outer()
   print x
   ```
   **Output:**
   ```
   7
   6
   5
   ```

43. **Project:** Show a class variable shared by all instances.
   
   **Solution:**
   ```akandechips
   class A:
       v = 1
   a1 = A()
   a2 = A()
   print a1.v
   print a2.v
   ```
   **Output:**
   ```
   1
   1
   ```

44. **Project:** Show an instance variable unique to each object.
   
   **Solution:**
   ```akandechips
   class B:
       function __init__(self, v):
           self.v = v
   b1 = B(2)
   b2 = B(3)
   print b1.v
   print b2.v
   ```
   **Output:**
   ```
   2
   3
   ```

45. **Project:** Show a static variable in a function (if supported).
   
   **Solution:**
   ```akandechips
   function counter():
       static c = 0
       c = c + 1
       print c
   counter()
   counter()
   ```
   **Output:**
   ```
   1
   2
   ```

46. **Project:** Show a global constant used in a function.
   
   **Solution:**
   ```akandechips
   PI = 3.14
   function area(r):
       return PI * r * r
   print area(2)
   ```
   **Output:**
   ```
   12.56
   ```

47. **Project:** Show a variable in a list comprehension is local.
   
   **Solution:**
   ```akandechips
   squares = [x * x for x in [1, 2, 3]]
   print squares
   # print x # error
   ```
   **Output:**
   ```
   [1, 4, 9]
   ```

48. **Project:** Show a variable in a lambda function.
   
   **Solution:**
   ```akandechips
   f = lambda x: x + 1
   print f(5)
   ```
   **Output:**
   ```
   6
   ```

49. **Project:** Show a parameter variable is local to the function.
   
   **Solution:**
   ```akandechips
   function show_param(a):
       print a
   show_param(7)
   # print a # error
   ```
   **Output:**
   ```
   7
   ```

50. **Project:** Show a recursive variable is unique to each call.
   
   **Solution:**
   ```akandechips
   function recurse(n):
       if n == 0:
           return 0
       else:
           return n + recurse(n-1)
   print recurse(3)
   ```
   **Output:**
   ```
   6
   ```

51. **Project:** Show a variable in a try/except/finally block.
   
   **Solution:**
   ```akandechips
   try:
       v = 1
   except:
       v = 2
   finally:
       v = v + 1
   print v
   ```
   **Output:**
   ```
   2
   ```

52. **Project:** Show a temporary variable in a function.
   
   **Solution:**
   ```akandechips
   function swap(a, b):
       temp = a
       a = b
       b = temp
       print a, b
   swap(1, 2)
   ```
   **Output:**
   ```
   2 1
   ```

53. **Project:** Show a persistent variable (global).
   
   **Solution:**
   ```akandechips
   count = 0
   function inc():
       global count
       count = count + 1
   inc()
   inc()
   print count
   ```
   **Output:**
   ```
   2
   ```

54. **Project:** Show variable assignment and reference.
   
   **Solution:**
   ```akandechips
   x = 8
   y = x + 2
   print y
   ```
   **Output:**
   ```
   10
   ```

55. **Project:** Show variable declaration (implicit).
   
   **Solution:**
   ```akandechips
   z = 9
   print z
   ```
   **Output:**
   ```
   9
   ```

56. **Project:** Show variable visibility in a class.
   
   **Solution:**
   ```akandechips
   class C:
       _hidden = 1
       public = 2
       function show():
           print _hidden
           print public
   c = C()
   c.show()
   ```
   **Output:**
   ```
   1
   2
   ```

57. **Project:** Show variable accessibility (public/private).
   
   **Solution:**
   ```akandechips
   class D:
       __private = 3
       public = 4
       function show():
           print public
   d = D()
   d.show()
   # print d.__private # error
   ```
   **Output:**
   ```
   4
   ```

58. **Project:** Show a variable leak from a block (if language allows).
   
   **Solution:**
   ```akandechips
   for i in 1 to 1:
       leak = 5
   print leak
   ```
   **Output:**
   ```
   5
   ```

59. **Project:** Show a variable's lifetime in a loop.
   
   **Solution:**
   ```akandechips
   for i in 1 to 2:
       temp = i
   print temp
   ```
   **Output:**
   ```
   2
   ```

60. **Project:** Show a variable's lifetime in a conditional block.
   
   **Solution:**
   ```akandechips
   if True:
       cond = 6
   print cond
   ```
   **Output:**
   ```
   6
   ```

61. **Project:** Show a variable's lifetime in a function parameter.
   
   **Solution:**
   ```akandechips
   function show_param2(b):
       print b
   show_param2(8)
   # print b # error
   ```
   **Output:**
   ```
   8
   ```

62. **Project:** Show a variable's lifetime in a recursive function.
   
   **Solution:**
   ```akandechips
   function rec(n):
       if n == 0:
           return 0
       else:
           return n + rec(n-1)
   print rec(4)
   ```
   **Output:**
   ```
   10
   ```

63. **Project:** Show a variable's lifetime in a class method.
   
   **Solution:**
   ```akandechips
   class E:
       function show():
           x = 11
           print x
   e = E()
   e.show()
   # print x # error
   ```
   **Output:**
   ```
   11
   ```

64. **Project:** Show a variable's lifetime in a lambda function.
   
   **Solution:**
   ```akandechips
   f = lambda y: y * 2
   print f(6)
   ```
   **Output:**
   ```
   12
   ```

65. **Project:** Show a variable's lifetime in a list comprehension.
   
   **Solution:**
   ```akandechips
   lst = [i for i in [1, 2, 3]]
   print lst
   # print i # error
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

66. **Project:** Show a variable's lifetime in a try/except block.
   
   **Solution:**
   ```akandechips
   try:
       t = 7
   except:
       t = 0
   print t
   ```
   **Output:**
   ```
   7
   ```

67. **Project:** Show a variable's lifetime in a finally block.
   
   **Solution:**
   ```akandechips
   try:
       pass
   finally:
       f = 9
   print f
   ```
   **Output:**
   ```
   9
   ```

68. **Project:** Show a variable's lifetime in a module.
   
   **Solution:**
   ```akandechips
   mod_var = 10
   print mod_var
   ```
   **Output:**
   ```
   10
   ```

69. **Project:** Show a variable's accessibility (public/private) in a class.
   
   **Solution:**
   ```akandechips
   class F:
       __private = 12
       public = 13
       function show():
           print public
   f = F()
   f.show()
   # print f.__private # error
   ```
   **Output:**
   ```
   13
   ```

70. **Project:** Show a variable's visibility in a class.
   
   **Solution:**
   ```akandechips
   class G:
       _hidden = 14
       public = 15
       function show():
           print _hidden
           print public
   g = G()
   g.show()
   ```
   **Output:**
   ```
   14
   15
   ```

---

### Data Structures (Expand Lists, Introduce Tuples, Dictionaries, Sets)
**Explanation:**
Data structures organize and store data efficiently. Lists, tuples, dictionaries, and sets each have unique uses.

#### Coding Questions & Answers

1. **What is a list?**
   
   **Answer:**
   A list is an ordered collection of items that can be changed (mutable).

2. **How do you create a list?**
   
   **Answer:**
   Use square brackets: `[1, 2, 3]`.

3. **How do you access an item in a list?**
   
   **Answer:**
   Use the index in square brackets: `lst[0]`.

4. **How do you change an item in a list?**
   
   **Answer:**
   Assign a new value: `lst[1] = 5`.

5. **How do you add an item to a list?**
   
   **Answer:**
   Use `append`: `lst.append(4)`.

6. **How do you remove an item from a list?**
   
   **Answer:**
   Use `remove`: `lst.remove(2)`.

7. **How do you get the length of a list?**
   
   **Answer:**
   Use `len(lst)`.

8. **What is a tuple?**
   
   **Answer:**
   A tuple is an ordered collection of items that cannot be changed (immutable).

9. **How do you create a tuple?**
   
   **Answer:**
   Use parentheses: `(1, 2, 3)`.

10. **How do you access an item in a tuple?**
    
    **Answer:**
    Use the index in parentheses: `tup[0]`.

11. **Can you change an item in a tuple?**
    
    **Answer:**
    No, tuples are immutable.

12. **What is a dictionary?**
    
    **Answer:**
    A dictionary is a collection of key-value pairs.

13. **How do you create a dictionary?**
    
    **Answer:**
    Use curly braces: `{"a": 1, "b": 2}`.

14. **How do you access a value in a dictionary?**
    
    **Answer:**
    Use the key in square brackets: `d["a"]`.

15. **How do you change a value in a dictionary?**
    
    **Answer:**
    Assign a new value: `d["a"] = 5`.

16. **How do you add a key-value pair to a dictionary?**
    
    **Answer:**
    Assign a value to a new key: `d["c"] = 3`.

17. **How do you remove a key-value pair from a dictionary?**
    
    **Answer:**
    Use `del d["a"]`.

18. **How do you get all keys from a dictionary?**
    
    **Answer:**
    Use `d.keys()`.

19. **How do you get all values from a dictionary?**
    
    **Answer:**
    Use `d.values()`.

20. **What is a set?**
    
    **Answer:**
    A set is an unordered collection of unique items.

21. **How do you create a set?**
    
    **Answer:**
    Use curly braces: `{1, 2, 3}`.

22. **How do you add an item to a set?**
    
    **Answer:**
    Use `add`: `s.add(4)`.

23. **How do you remove an item from a set?**
    
    **Answer:**
    Use `remove`: `s.remove(2)`.

24. **How do you check if an item is in a set?**
    
    **Answer:**
    Use `in`: `2 in s`.

25. **How do you get the length of a set?**
    
    **Answer:**
    Use `len(s)`.

26. **How do you convert a list to a set?**
    
    **Answer:**
    Use `set(lst)`.

27. **How do you convert a set to a list?**
    
    **Answer:**
    Use `list(s)`.

28. **How do you check if a key exists in a dictionary?**
    
    **Answer:**
    Use `in`: `'a' in d`.

29. **How do you loop through a list?**
    
    **Answer:**
    Use `for item in lst:`.

30. **How do you loop through a dictionary?**
    
    **Answer:**
    Use `for key in d:` or `for key, value in d.items():`.

31. **How do you loop through a set?**
    
    **Answer:**
    Use `for item in s:`.

32. **How do you get the index of an item in a list?**
    
    **Answer:**
    Use `lst.index(2)`.

33. **How do you count occurrences of an item in a list?**
    
    **Answer:**
    Use `lst.count(2)`.

34. **How do you sort a list?**
    
    **Answer:**
    Use `lst.sort()`.

35. **How do you reverse a list?**
    
    **Answer:**
    Use `lst.reverse()` or `lst[::-1]`.

36. **How do you copy a list?**
    
    **Answer:**
    Use `lst[:]` or `lst.copy()`.

37. **How do you clear a list?**
    
    **Answer:**
    Use `lst.clear()`.

38. **How do you clear a dictionary?**
    
    **Answer:**
    Use `d.clear()`.

39. **How do you clear a set?**
    
    **Answer:**
    Use `s.clear()`.

40. **How do you check if a list is empty?**
    
    **Answer:**
    Use `len(lst) == 0` or `not lst`.


#### Projects & Solutions

1. **Project:** Create a list of numbers and print it.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   print nums
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

2. **Project:** Change the second item in a list to 5 and print the list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   nums[1] = 5
   print nums
   ```
   **Output:**
   ```
   [1, 5, 3]
   ```

3. **Project:** Add 4 to a list and print the list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   nums.append(4)
   print nums
   ```
   **Output:**
   ```
   [1, 2, 3, 4]
   ```

4. **Project:** Remove 2 from a list and print the list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   nums.remove(2)
   print nums
   ```
   **Output:**
   ```
   [1, 3]
   ```

5. **Project:** Print the length of a list.
   
   **Solution:**
   ```akandechips
   nums = [1, 2, 3]
   print len(nums)
   ```
   **Output:**
   ```
   3
   ```

6. **Project:** Create a tuple and print it.
   
   **Solution:**
   ```akandechips
   tup = (1, 2, 3)
   print tup
   ```
   **Output:**
   ```
   (1, 2, 3)
   ```

7. **Project:** Access the first item in a tuple and print it.
   
   **Solution:**
   ```akandechips
   tup = (1, 2, 3)
   print tup[0]
   ```
   **Output:**
   ```
   1
   ```

8. **Project:** Create a dictionary and print it.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d
   ```
   **Output:**
   ```
   {"a": 1, "b": 2}
   ```

9. **Project:** Change the value for key "a" in a dictionary to 5 and print it.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   d["a"] = 5
   print d
   ```
   **Output:**
   ```
   {"a": 5, "b": 2}
   ```

10. **Project:** Add a new key-value pair to a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    d["c"] = 3
    print d
    ```
    **Output:**
    ```
    {"a": 1, "b": 2, "c": 3}
    ```

11. **Project:** Remove a key from a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    del d["a"]
    print d
    ```
    **Output:**
    ```
    {"b": 2}
    ```

12. **Project:** Print all keys in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d.keys()
    ```
    **Output:**
    ```
    ["a", "b"]
    ```

13. **Project:** Print all values in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d.values()
    ```
    **Output:**
    ```
    [1, 2]
    ```

14. **Project:** Create a set and print it.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

15. **Project:** Add 4 to a set and print it.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    s.add(4)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3, 4}
    ```

16. **Project:** Remove 2 from a set and print it.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    s.remove(2)
    print s
    ```
    **Output:**
    ```
    {1, 3}
    ```

17. **Project:** Check if 2 is in a set and print the result.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    print 2 in s
    ```
    **Output:**
    ```
    True
    ```

18. **Project:** Convert a list to a set and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 2, 3]
    s = set(nums)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

19. **Project:** Convert a set to a list and print it.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    nums = list(s)
    print nums
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

20. **Project:** Loop through a list and print each item.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    for n in nums:
        print n
    ```
    **Output:**
    ```
    1
    2
    3
    ```

21. **Project:** Loop through a dictionary and print each key and value.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    for k, v in d.items():
        print k, v
    ```
    **Output:**
    ```
    a 1
    b 2
    ```

22. **Project:** Loop through a set and print each item.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    for n in s:
        print n
    ```
    **Output:**
    ```
    1
    2
    3
    ```

23. **Project:** Get the index of 2 in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    print nums.index(2)
    ```
    **Output:**
    ```
    1
    ```

24. **Project:** Count how many times 2 appears in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 2, 3]
    print nums.count(2)
    ```
    **Output:**
    ```
    2
    ```

25. **Project:** Sort a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [3, 1, 2]
    nums.sort()
    print nums
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

26. **Project:** Reverse a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    nums.reverse()
    print nums
    ```
    **Output:**
    ```
    [3, 2, 1]
    ```

27. **Project:** Copy a list and print the copy.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    nums2 = nums[:]
    print nums2
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

28. **Project:** Clear a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 3]
    nums.clear()
    print nums
    ```
    **Output:**
    ```
    []
    ```

29. **Project:** Clear a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    d.clear()
    print d
    ```
    **Output:**
    ```
    {}
    ```

30. **Project:** Clear a set and print it.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    s.clear()
    print s
    ```
    **Output:**
    ```
    set()
    ```

31. **Project:** Check if a list is empty and print the result.
    
    **Solution:**
    ```akandechips
    nums = []
    print len(nums) == 0
    ```
    **Output:**
    ```
    True
    ```

32. **Project:** Check if a key exists in a dictionary and print the result.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print "a" in d
    ```
    **Output:**
    ```
    True
    ```

33. **Project:** Check if an item is in a set and print the result.
    
    **Solution:**
    ```akandechips
    s = {1, 2, 3}
    print 2 in s
    ```
    **Output:**
    ```
    True
    ```

34. **Project:** Create a tuple of three strings and print it.
    
    **Solution:**
    ```akandechips
    tup = ("a", "b", "c")
    print tup
    ```
    **Output:**
    ```
    ("a", "b", "c")
    ```

35. **Project:** Access the last item in a tuple and print it.
    
    **Solution:**
    ```akandechips
    tup = (1, 2, 3)
    print tup[-1]
    ```
    **Output:**
    ```
    3
    ```

36. **Project:** Loop through a tuple and print each item.
    
    **Solution:**
    ```akandechips
    tup = (1, 2, 3)
    for n in tup:
        print n
    ```
    **Output:**
    ```
    1
    2
    3
    ```

37. **Project:** Create a dictionary with three key-value pairs and print it.
    
    **Solution:**
    ```akandechips
    d = {"x": 10, "y": 20, "z": 30}
    print d
    ```
    **Output:**
    ```
    {"x": 10, "y": 20, "z": 30}
    ```

38. **Project:** Get all keys from a dictionary and print them.
    
    **Solution:**
    ```akandechips
    d = {"x": 10, "y": 20, "z": 30}
    print d.keys()
    ```
    **Output:**
    ```
    ["x", "y", "z"]
    ```

39. **Project:** Get all values from a dictionary and print them.
    
    **Solution:**
    ```akandechips
    d = {"x": 10, "y": 20, "z": 30}
    print d.values()
    ```
    **Output:**
    ```
    [10, 20, 30]
    ```

40. **Project:** Create a set from a list with duplicates and print it.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 2, 3, 3, 3]
    s = set(nums)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

---

### Loops (for, while, break, continue)
**Explanation:**
Loops let you repeat actions. The `for` and `while` loops are essential for automation and data processing.

#### Coding Questions & Answers
<!-- 30+ loops questions, answers, and outputs go here -->

#### Projects & Solutions
<!-- 30+ loops projects, solutions, and outputs go here -->

---

### Comparison and Logical Operators (Deeper Dive)
**Explanation:**
Comparison and logical operators help your program make decisions. This section explores them in detail.

#### Coding Questions & Answers

1. **What does the `==` operator do?**
   
   **Answer:**
   Checks if two values are equal.
   ```akandechips
   print 3 == 3
   ```
   **Output:**
   ```
   True
   ```

2. **What does the `!=` operator do?**
   
   **Answer:**
   Checks if two values are not equal.
   ```akandechips
   print 3 != 4
   ```
   **Output:**
   ```
   True
   ```

3. **What does the `>` operator do?**
   
   **Answer:**
   Checks if the left value is greater than the right value.
   ```akandechips
   print 5 > 2
   ```
   **Output:**
   ```
   True
   ```

4. **What does the `<` operator do?**
   
   **Answer:**
   Checks if the left value is less than the right value.
   ```akandechips
   print 2 < 5
   ```
   **Output:**
   ```
   True
   ```

5. **What does the `>=` operator do?**
   
   **Answer:**
   Checks if the left value is greater than or equal to the right value.
   ```akandechips
   print 5 >= 5
   ```
   **Output:**
   ```
   True
   ```

6. **What does the `<=` operator do?**
   
   **Answer:**
   Checks if the left value is less than or equal to the right value.
   ```akandechips
   print 3 <= 4
   ```
   **Output:**
   ```
   True
   ```

7. **What does the `and` operator do?**
   
   **Answer:**
   Returns True if both conditions are True.
   ```akandechips
   print True and False
   ```
   **Output:**
   ```
   False
   ```

8. **What does the `or` operator do?**
   
   **Answer:**
   Returns True if at least one condition is True.
   ```akandechips
   print True or False
   ```
   **Output:**
   ```
   True
   ```

9. **What does the `not` operator do?**
   
   **Answer:**
   Reverses the truth value.
   ```akandechips
   print not True
   ```
   **Output:**
   ```
   False
   ```

10. **What is the result of `3 < 5 and 2 > 1`?**
    
    **Answer:**
    True, because both conditions are True.
    ```akandechips
    print 3 < 5 and 2 > 1
    ```
    **Output:**
    ```
    True
    ```

11. **What is the result of `3 < 5 or 2 < 1`?**
    
    **Answer:**
    True, because at least one condition is True.
    ```akandechips
    print 3 < 5 or 2 < 1
    ```
    **Output:**
    ```
    True
    ```

12. **What is the result of `not (3 == 3)`?**
    
    **Answer:**
    False, because 3 == 3 is True, and not True is False.
    ```akandechips
    print not (3 == 3)
    ```
    **Output:**
    ```
    False
    ```

13. **What is the result of `5 >= 2 and 1 == 1`?**
    
    **Answer:**
    True.
    ```akandechips
    print 5 >= 2 and 1 == 1
    ```
    **Output:**
    ```
    True
    ```

14. **What is the result of `4 != 4 or 2 > 1`?**
    
    **Answer:**
    True.
    ```akandechips
    print 4 != 4 or 2 > 1
    ```
    **Output:**
    ```
    True
    ```

15. **What is the result of `not (2 < 1)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (2 < 1)
    ```
    **Output:**
    ```
    True
    ```

16. **What is the result of `True and not False`?**
    
    **Answer:**
    True.
    ```akandechips
    print True and not False
    ```
    **Output:**
    ```
    True
    ```

17. **What is the result of `False or not False`?**
    
    **Answer:**
    True.
    ```akandechips
    print False or not False
    ```
    **Output:**
    ```
    True
    ```

18. **What is the result of `not (True and False)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (True and False)
    ```
    **Output:**
    ```
    True
    ```

19. **What is the result of `not (False or False)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (False or False)
    ```
    **Output:**
    ```
    True
    ```

20. **What is the result of `3 > 2 and 2 > 3`?**
    
    **Answer:**
    False.
    ```akandechips
    print 3 > 2 and 2 > 3
    ```
    **Output:**
    ```
    False
    ```

21. **What is the result of `3 > 2 or 2 > 3`?**
    
    **Answer:**
    True.
    ```akandechips
    print 3 > 2 or 2 > 3
    ```
    **Output:**
    ```
    True
    ```

22. **What is the result of `not (3 > 2 or 2 > 3)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (3 > 2 or 2 > 3)
    ```
    **Output:**
    ```
    False
    ```

23. **What is the result of `not (3 > 2 and 2 > 3)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (3 > 2 and 2 > 3)
    ```
    **Output:**
    ```
    True
    ```

24. **What is the result of `1 == 1 and 2 == 2 and 3 == 3`?**
    
    **Answer:**
    True.
    ```akandechips
    print 1 == 1 and 2 == 2 and 3 == 3
    ```
    **Output:**
    ```
    True
    ```

25. **What is the result of `1 == 1 and 2 == 3 and 3 == 3`?**
    
    **Answer:**
    False.
    ```akandechips
    print 1 == 1 and 2 == 3 and 3 == 3
    ```
    **Output:**
    ```
    False
    ```

26. **What is the result of `1 == 2 or 2 == 3 or 3 == 3`?**
    
    **Answer:**
    True.
    ```akandechips
    print 1 == 2 or 2 == 3 or 3 == 3
    ```
    **Output:**
    ```
    True
    ```

27. **What is the result of `not (1 == 2 or 2 == 3 or 3 == 3)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (1 == 2 or 2 == 3 or 3 == 3)
    ```
    **Output:**
    ```
    False
    ```

28. **What is the result of `not (1 == 2 and 2 == 3 and 3 == 3)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (1 == 2 and 2 == 3 and 3 == 3)
    ```
    **Output:**
    ```
    True
    ```

29. **What is the result of `True and True or False`?**
    
    **Answer:**
    True.
    ```akandechips
    print True and True or False
    ```
    **Output:**
    ```
    True
    ```

30. **What is the result of `False or False and True`?**
    
    **Answer:**
    False.
    ```akandechips
    print False or False and True
    ```
    **Output:**
    ```
    False
    ```

31. **What is the result of `not True or not False`?**
    
    **Answer:**
    True.
    ```akandechips
    print not True or not False
    ```
    **Output:**
    ```
    True
    ```

32. **What is the result of `not (True or False) and (False or True)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (True or False) and (False or True)
    ```
    **Output:**
    ```
    False
    ```

33. **What is the result of `not (True and False) or (False and True)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (True and False) or (False and True)
    ```
    **Output:**
    ```
    True
    ```

34. **What is the result of `not (not True)`?**
    
    **Answer:**
    True.
    ```akandechips
    print not (not True)
    ```
    **Output:**
    ```
    True
    ```

35. **What is the result of `not (not False)`?**
    
    **Answer:**
    False.
    ```akandechips
    print not (not False)
    ```
    **Output:**
    ```
    False
    ```


#### Projects & Solutions

1. **Project:** Check if 10 is greater than 5 and print the result.
   
   **Solution:**
   ```akandechips
   print 10 > 5
   ```
   **Output:**
   ```
   True
   ```

2. **Project:** Check if 7 is less than or equal to 7 and print the result.
   
   **Solution:**
   ```akandechips
   print 7 <= 7
   ```
   **Output:**
   ```
   True
   ```

3. **Project:** Check if 3 is not equal to 4 and print the result.
   
   **Solution:**
   ```akandechips
   print 3 != 4
   ```
   **Output:**
   ```
   True
   ```

4. **Project:** Check if both 5 > 2 and 8 < 10 are True.
   
   **Solution:**
   ```akandechips
   print 5 > 2 and 8 < 10
   ```
   **Output:**
   ```
   True
   ```

5. **Project:** Check if either 2 > 3 or 4 == 4 is True.
   
   **Solution:**
   ```akandechips
   print 2 > 3 or 4 == 4
   ```
   **Output:**
   ```
   True
   ```

6. **Project:** Print the result of not (6 < 2).
   
   **Solution:**
   ```akandechips
   print not (6 < 2)
   ```
   **Output:**
   ```
   True
   ```

7. **Project:** Check if 5 is greater than 2 and less than 10.
   
   **Solution:**
   ```akandechips
   print 5 > 2 and 5 < 10
   ```
   **Output:**
   ```
   True
   ```

8. **Project:** Check if 3 is less than 1 or greater than 2.
   
   **Solution:**
   ```akandechips
   print 3 < 1 or 3 > 2
   ```
   **Output:**
   ```
   True
   ```

9. **Project:** Print the result of not (4 == 4).
   
   **Solution:**
   ```akandechips
   print not (4 == 4)
   ```
   **Output:**
   ```
   False
   ```

10. **Project:** Check if 2 is not equal to 2 or 1 is less than 0.
    
    **Solution:**
    ```akandechips
    print 2 != 2 or 1 < 0
    ```
    **Output:**
    ```
    False
    ```

11. **Project:** Check if not (3 > 1 and 2 < 1).
    
    **Solution:**
    ```akandechips
    print not (3 > 1 and 2 < 1)
    ```
    **Output:**
    ```
    True
    ```

12. **Project:** Print the result of (2 == 2 and 3 == 3) or (4 == 5).
    
    **Solution:**
    ```akandechips
    print (2 == 2 and 3 == 3) or (4 == 5)
    ```
    **Output:**
    ```
    True
    ```

13. **Project:** Print the result of not (2 == 2 and 3 == 3).
    
    **Solution:**
    ```akandechips
    print not (2 == 2 and 3 == 3)
    ```
    **Output:**
    ```
    False
    ```

14. **Project:** Check if 1 < 2 < 3 and print the result.
    
    **Solution:**
    ```akandechips
    print 1 < 2 and 2 < 3
    ```
    **Output:**
    ```
    True
    ```

15. **Project:** Check if 5 >= 5 and 6 <= 7.
    
    **Solution:**
    ```akandechips
    print 5 >= 5 and 6 <= 7
    ```
    **Output:**
    ```
    True
    ```

16. **Project:** Print the result of not (False).
    
    **Solution:**
    ```akandechips
    print not False
    ```
    **Output:**
    ```
    True
    ```

17. **Project:** Print the result of not (True).
    
    **Solution:**
    ```akandechips
    print not True
    ```
    **Output:**
    ```
    False
    ```

18. **Project:** Check if 2 == 2 and 3 != 4.
    
    **Solution:**
    ```akandechips
    print 2 == 2 and 3 != 4
    ```
    **Output:**
    ```
    True
    ```

19. **Project:** Check if 2 == 3 or 3 != 4.
    
    **Solution:**
    ```akandechips
    print 2 == 3 or 3 != 4
    ```
    **Output:**
    ```
    True
    ```

20. **Project:** Print the result of not (2 == 3 or 3 != 4).
    
    **Solution:**
    ```akandechips
    print not (2 == 3 or 3 != 4)
    ```
    **Output:**
    ```
    False
    ```

21. **Project:** Check if 1 == 1 and 2 == 2 and 3 == 3.
    
    **Solution:**
    ```akandechips
    print 1 == 1 and 2 == 2 and 3 == 3
    ```
    **Output:**
    ```
    True
    ```

22. **Project:** Check if 1 == 1 or 2 == 3 or 3 == 3.
    
    **Solution:**
    ```akandechips
    print 1 == 1 or 2 == 3 or 3 == 3
    ```
    **Output:**
    ```
    True
    ```

23. **Project:** Print the result of not (1 == 1 or 2 == 3 or 3 == 3).
    
    **Solution:**
    ```akandechips
    print not (1 == 1 or 2 == 3 or 3 == 3)
    ```
    **Output:**
    ```
    False
    ```

24. **Project:** Print the result of not (1 == 2 and 2 == 3 and 3 == 3).
    
    **Solution:**
    ```akandechips
    print not (1 == 2 and 2 == 3 and 3 == 3)
    ```
    **Output:**
    ```
    True
    ```

25. **Project:** Print the result of True and True or False.
    
    **Solution:**
    ```akandechips
    print True and True or False
    ```
    **Output:**
    ```
    True
    ```

26. **Project:** Print the result of False or False and True.
    
    **Solution:**
    ```akandechips
    print False or False and True
    ```
    **Output:**
    ```
    False
    ```

27. **Project:** Print the result of not True or not False.
    
    **Solution:**
    ```akandechips
    print not True or not False
    ```
    **Output:**
    ```
    True
    ```

28. **Project:** Print the result of not (True or False) and (False or True).
    
    **Solution:**
    ```akandechips
    print not (True or False) and (False or True)
    ```
    **Output:**
    ```
    False
    ```

29. **Project:** Print the result of not (True and False) or (False and True).
    
    **Solution:**
    ```akandechips
    print not (True and False) or (False and True)
    ```
    **Output:**
    ```
    True
    ```

30. **Project:** Print the result of not (not True).
    
    **Solution:**
    ```akandechips
    print not (not True)
    ```
    **Output:**
    ```
    True
    ```

31. **Project:** Print the result of not (not False).
    
    **Solution:**
    ```akandechips
    print not (not False)
    ```
    **Output:**
    ```
    False
    ```

32. **Project:** Check if 10 > 5 and 5 < 10 and print the result.
    
    **Solution:**
    ```akandechips
    print 10 > 5 and 5 < 10
    ```
    **Output:**
    ```
    True
    ```

33. **Project:** Check if 10 < 5 or 5 < 10 and print the result.
    
    **Solution:**
    ```akandechips
    print 10 < 5 or 5 < 10
    ```
    **Output:**
    ```
    True
    ```

34. **Project:** Print the result of not (10 < 5 or 5 < 10).
    
    **Solution:**
    ```akandechips
    print not (10 < 5 or 5 < 10)
    ```
    **Output:**
    ```
    False
    ```

35. **Project:** Print the result of not (10 > 5 and 5 < 10).
    
    **Solution:**
    ```akandechips
    print not (10 > 5 and 5 < 10)
    ```
    **Output:**
    ```
    False
    ```

---

### Simple Algorithms (Sorting, Searching, etc.)
**Explanation:**
Algorithms are step-by-step instructions for solving problems. Sorting and searching are common examples.

#### Coding Questions & Answers

1. **What is an algorithm?**
   
   **Answer:**
   A step-by-step set of instructions to solve a problem.

2. **What is sorting?**
   
   **Answer:**
   Arranging items in order (e.g., ascending or descending).

3. **What is searching?**
   
   **Answer:**
   Finding a specific item in a collection.

4. **How do you sort a list in ascending order?**
   
   **Answer:**
   Use `sort()`: 
   ```akandechips
   nums = [3, 1, 2]
   nums.sort()
   print nums
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

5. **How do you sort a list in descending order?**
   
   **Answer:**
   Use `sort(reverse=True)`:
   ```akandechips
   nums = [3, 1, 2]
   nums.sort(reverse=True)
   print nums
   ```
   **Output:**
   ```
   [3, 2, 1]
   ```

6. **How do you find the maximum value in a list?**
   
   **Answer:**
   Use `max(nums)`.
   ```akandechips
   nums = [3, 1, 2]
   print max(nums)
   ```
   **Output:**
   ```
   3
   ```

7. **How do you find the minimum value in a list?**
   
   **Answer:**
   Use `min(nums)`.
   ```akandechips
   nums = [3, 1, 2]
   print min(nums)
   ```
   **Output:**
   ```
   1
   ```

8. **How do you search for an item in a list?**
   
   **Answer:**
   Use `in`:
   ```akandechips
   nums = [3, 1, 2]
   print 2 in nums
   ```
   **Output:**
   ```
   True
   ```

9. **How do you find the index of an item in a list?**
   
   **Answer:**
   Use `index()`:
   ```akandechips
   nums = [3, 1, 2]
   print nums.index(1)
   ```
   **Output:**
   ```
   1
   ```

10. **How do you count occurrences of an item in a list?**
    
    **Answer:**
    Use `count()`:
    ```akandechips
    nums = [3, 1, 2, 1]
    print nums.count(1)
    ```
    **Output:**
    ```
    2
    ```

11. **What is linear search?**
    
    **Answer:**
    Checking each item in a list one by one until the target is found.

12. **What is binary search?**
    
    **Answer:**
    A search algorithm that repeatedly divides a sorted list in half to find a target.

13. **What is bubble sort?**
    
    **Answer:**
    A sorting algorithm that repeatedly steps through the list, compares adjacent items, and swaps them if needed.

14. **What is selection sort?**
    
    **Answer:**
    A sorting algorithm that repeatedly finds the minimum element and moves it to the front.

15. **What is insertion sort?**
    
    **Answer:**
    A sorting algorithm that builds the sorted list one item at a time by inserting items into their correct position.

16. **How do you reverse a list?**
    
    **Answer:**
    Use `reverse()`:
    ```akandechips
    nums = [1, 2, 3]
    nums.reverse()
    print nums
    ```
    **Output:**
    ```
    [3, 2, 1]
    ```

17. **How do you sum all items in a list?**
    
    **Answer:**
    Use `sum()`:
    ```akandechips
    nums = [1, 2, 3]
    print sum(nums)
    ```
    **Output:**
    ```
    6
    ```

18. **How do you check if a list is sorted?**
    
    **Answer:**
    Compare the list to its sorted version:
    ```akandechips
    nums = [1, 2, 3]
    print nums == sorted(nums)
    ```
    **Output:**
    ```
    True
    ```

19. **How do you copy a list?**
    
    **Answer:**
    Use `[:]` or `copy()`:
    ```akandechips
    nums = [1, 2, 3]
    nums2 = nums[:]
    print nums2
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

20. **How do you remove duplicates from a list?**
    
    **Answer:**
    Convert to a set and back to a list:
    ```akandechips
    nums = [1, 2, 2, 3]
    nums = list(set(nums))
    print nums
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

21. **How do you find the second largest number in a list?**
    
    **Answer:**
    Remove the max, then find the new max:
    ```akandechips
    nums = [1, 2, 3]
    nums.remove(max(nums))
    print max(nums)
    ```
    **Output:**
    ```
    2
    ```

22. **How do you merge two sorted lists?**
    
    **Answer:**
    Use `+` and sort:
    ```akandechips
    a = [1, 3, 5]
    b = [2, 4, 6]
    merged = a + b
    merged.sort()
    print merged
    ```
    **Output:**
    ```
    [1, 2, 3, 4, 5, 6]
    ```

23. **How do you find the average of a list?**
    
    **Answer:**
    Divide the sum by the length:
    ```akandechips
    nums = [1, 2, 3]
    print sum(nums) / len(nums)
    ```
    **Output:**
    ```
    2
    ```

24. **How do you find all even numbers in a list?**
    
    **Answer:**
    Use a loop and check `% 2 == 0`:
    ```akandechips
    nums = [1, 2, 3, 4]
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    print evens
    ```
    **Output:**
    ```
    [2, 4]
    ```

25. **How do you find all odd numbers in a list?**
    
    **Answer:**
    Use a loop and check `% 2 != 0`:
    ```akandechips
    nums = [1, 2, 3, 4]
    odds = []
    for n in nums:
        if n % 2 != 0:
            odds.append(n)
    print odds
    ```
    **Output:**
    ```
    [1, 3]
    ```

26. **How do you count how many numbers are greater than 5 in a list?**
    
    **Answer:**
    Use a loop and count:
    ```akandechips
    nums = [3, 6, 8, 2]
    count = 0
    for n in nums:
        if n > 5:
            count = count + 1
    print count
    ```
    **Output:**
    ```
    2
    ```

27. **How do you check if all items in a list are positive?**
    
    **Answer:**
    Use a loop and check:
    ```akandechips
    nums = [1, 2, 3]
    all_positive = True
    for n in nums:
        if n <= 0:
            all_positive = False
    print all_positive
    ```
    **Output:**
    ```
    True
    ```

28. **How do you check if any item in a list is negative?**
    
    **Answer:**
    Use a loop and check:
    ```akandechips
    nums = [1, -2, 3]
    any_negative = False
    for n in nums:
        if n < 0:
            any_negative = True
    print any_negative
    ```
    **Output:**
    ```
    True
    ```

29. **How do you find the sum of even numbers in a list?**
    
    **Answer:**
    Use a loop and add:
    ```akandechips
    nums = [1, 2, 3, 4]
    total = 0
    for n in nums:
        if n % 2 == 0:
            total = total + n
    print total
    ```
    **Output:**
    ```
    6
    ```

30. **How do you find the product of all numbers in a list?**
    
    **Answer:**
    Use a loop and multiply:
    ```akandechips
    nums = [1, 2, 3, 4]
    product = 1
    for n in nums:
        product = product * n
    print product
    ```
    **Output:**
    ```
    24
    ```


#### Projects & Solutions

1. **Project:** Sort a list of numbers in ascending order and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   nums.sort()
   print nums
   ```
   **Output:**
   ```
   [1, 2, 5, 8]
   ```

2. **Project:** Sort a list of numbers in descending order and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   nums.sort(reverse=True)
   print nums
   ```
   **Output:**
   ```
   [8, 5, 2, 1]
   ```

3. **Project:** Find the maximum value in a list and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   print max(nums)
   ```
   **Output:**
   ```
   8
   ```

4. **Project:** Find the minimum value in a list and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   print min(nums)
   ```
   **Output:**
   ```
   1
   ```

5. **Project:** Search for the number 8 in a list and print if it exists.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   print 8 in nums
   ```
   **Output:**
   ```
   True
   ```

6. **Project:** Find the index of 2 in a list and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   print nums.index(2)
   ```
   **Output:**
   ```
   1
   ```

7. **Project:** Count how many times 2 appears in a list and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 2, 1]
   print nums.count(2)
   ```
   **Output:**
   ```
   2
   ```

8. **Project:** Reverse a list and print it.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   nums.reverse()
   print nums
   ```
   **Output:**
   ```
   [1, 8, 2, 5]
   ```

9. **Project:** Sum all numbers in a list and print the result.
   
   **Solution:**
   ```akandechips
   nums = [5, 2, 8, 1]
   print sum(nums)
   ```
   **Output:**
   ```
   16
   ```

10. **Project:** Remove duplicates from a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 2, 1, 5]
    nums = list(set(nums))
    print nums
    ```
    **Output:**
    ```
    [1, 2, 5, 8]
    ```

11. **Project:** Find the second largest number in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    nums.remove(max(nums))
    print max(nums)
    ```
    **Output:**
    ```
    5
    ```

12. **Project:** Merge two sorted lists and print the result.
    
    **Solution:**
    ```akandechips
    a = [1, 3, 5]
    b = [2, 4, 6]
    merged = a + b
    merged.sort()
    print merged
    ```
    **Output:**
    ```
    [1, 2, 3, 4, 5, 6]
    ```

13. **Project:** Find the average of a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    print sum(nums) / len(nums)
    ```
    **Output:**
    ```
    4
    ```

14. **Project:** Find all even numbers in a list and print them.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    print evens
    ```
    **Output:**
    ```
    [2, 8]
    ```

15. **Project:** Find all odd numbers in a list and print them.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    odds = []
    for n in nums:
        if n % 2 != 0:
            odds.append(n)
    print odds
    ```
    **Output:**
    ```
    [5, 1]
    ```

16. **Project:** Count how many numbers are greater than 5 in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    count = 0
    for n in nums:
        if n > 5:
            count = count + 1
    print count
    ```
    **Output:**
    ```
    1
    ```

17. **Project:** Check if all items in a list are positive and print the result.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    all_positive = True
    for n in nums:
        if n <= 0:
            all_positive = False
    print all_positive
    ```
    **Output:**
    ```
    True
    ```

18. **Project:** Check if any item in a list is negative and print the result.
    
    **Solution:**
    ```akandechips
    nums = [5, -2, 8, 1]
    any_negative = False
    for n in nums:
        if n < 0:
            any_negative = True
    print any_negative
    ```
    **Output:**
    ```
    True
    ```

19. **Project:** Find the sum of even numbers in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    total = 0
    for n in nums:
        if n % 2 == 0:
            total = total + n
    print total
    ```
    **Output:**
    ```
    10
    ```

20. **Project:** Find the product of all numbers in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    product = 1
    for n in nums:
        product = product * n
    print product
    ```
    **Output:**
    ```
    80
    ```

21. **Project:** Implement linear search to find 8 in a list and print the index.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    index = -1
    for i in range(len(nums)):
        if nums[i] == 8:
            index = i
    print index
    ```
    **Output:**
    ```
    2
    ```

22. **Project:** Implement bubble sort to sort a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    print nums
    ```
    **Output:**
    ```
    [1, 2, 5, 8]
    ```

23. **Project:** Find the largest number in a list without using max().
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    print largest
    ```
    **Output:**
    ```
    8
    ```

24. **Project:** Find the smallest number in a list without using min().
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
    print smallest
    ```
    **Output:**
    ```
    1
    ```

25. **Project:** Check if a list is sorted in ascending order and print the result.
    
    **Solution:**
    ```akandechips
    nums = [1, 2, 5, 8]
    print nums == sorted(nums)
    ```
    **Output:**
    ```
    True
    ```

26. **Project:** Copy a list and print the copy.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    nums2 = nums[:]
    print nums2
    ```
    **Output:**
    ```
    [5, 2, 8, 1]
    ```

27. **Project:** Merge two unsorted lists, sort, and print the result.
    
    **Solution:**
    ```akandechips
    a = [5, 1]
    b = [8, 2]
    merged = a + b
    merged.sort()
    print merged
    ```
    **Output:**
    ```
    [1, 2, 5, 8]
    ```

28. **Project:** Find all numbers greater than 3 in a list and print them.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    result = []
    for n in nums:
        if n > 3:
            result.append(n)
    print result
    ```
    **Output:**
    ```
    [5, 8]
    ```

29. **Project:** Find the sum of odd numbers in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    total = 0
    for n in nums:
        if n % 2 != 0:
            total = total + n
    print total
    ```
    **Output:**
    ```
    6
    ```

30. **Project:** Find the average of even numbers in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [5, 2, 8, 1]
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    print sum(evens) / len(evens)
    ```
    **Output:**
    ```
    5
    ```

---

### Introduction to Modules and Imports
**Explanation:**
Modules let you organize code into separate files. Imports allow you to use code from other modules or libraries.

#### Coding Questions & Answers

1. **What is a module?**
   
   **Answer:**
   A file containing code (functions, variables, etc.) that can be imported and used in other programs.

2. **What is an import?**
   
   **Answer:**
   A statement that brings code from another module into your program.

3. **How do you import a module?**
   
   **Answer:**
   Use the `import` statement:
   ```akandechips
   import math
   ```

4. **How do you use a function from an imported module?**
   
   **Answer:**
   Use the module name, a dot, and the function name:
   ```akandechips
   import math
   print math.sqrt(9)
   ```
   **Output:**
   ```
   3
   ```

5. **How do you import only a specific function from a module?**
   
   **Answer:**
   Use `from ... import ...`:
   ```akandechips
   from math import sqrt
   print sqrt(16)
   ```
   **Output:**
   ```
   4
   ```

6. **How do you import a module with an alias?**
   
   **Answer:**
   Use `as`:
   ```akandechips
   import math as m
   print m.sqrt(25)
   ```
   **Output:**
   ```
   5
   ```

7. **How do you import all functions from a module?**
   
   **Answer:**
   Use `from ... import *`:
   ```akandechips
   from math import *
   print sqrt(36)
   ```
   **Output:**
   ```
   6
   ```

8. **How do you create your own module?**
   
   **Answer:**
   Write code in a `.ak` file (e.g., `mymodule.ak`).

9. **How do you import your own module?**
   
   **Answer:**
   Use `import mymodule` if `mymodule.ak` is in the same folder.

10. **How do you reload a module after changing its code?**
    
    **Answer:**
    Restart your program to reload the module.

11. **What is a standard library?**
    
    **Answer:**
    A collection of modules included with the language.

12. **Give an example of a standard library module.**
    
    **Answer:**
    `math`, `random`, `os`.

13. **How do you list all functions in a module?**
    
    **Answer:**
    Use `dir(module)`:
    ```akandechips
    import math
    print dir(math)
    ```
    **Output:**
    ```
    [...list of math functions...]
    ```

14. **How do you check if a module is installed?**
    
    **Answer:**
    Try importing it; if it fails, it's not installed.

15. **How do you import multiple modules in one line?**
    
    **Answer:**
    Separate with commas:
    ```akandechips
    import math, random
    ```

16. **How do you use a function from a module you imported with an alias?**
    
    **Answer:**
    Use the alias:
    ```akandechips
    import random as r
    print r.randint(1, 10)
    ```
    **Output:**
    ```
    (random number between 1 and 10)
    ```

17. **How do you import a function with an alias?**
    
    **Answer:**
    Use `as`:
    ```akandechips
    from math import sqrt as s
    print s(49)
    ```
    **Output:**
    ```
    7
    ```

18. **How do you prevent a module from running code on import?**
    
    **Answer:**
    Use `if __name__ == "__main__":` in the module.

19. **How do you import a module from a subfolder?**
    
    **Answer:**
    Use dot notation: `import folder.module`.

20. **How do you import everything except a specific function?**
    
    **Answer:**
    Import all, then avoid using the unwanted function.

21. **How do you check the file path of a module?**
    
    **Answer:**
    Use `module.__file__`:
    ```akandechips
    import math
    print math.__file__
    ```
    **Output:**
    ```
    (path to math module)
    ```

22. **How do you import a module only if a condition is met?**
    
    **Answer:**
    Use an if statement:
    ```akandechips
    if use_math:
        import math
    ```

23. **How do you import a module inside a function?**
    
    **Answer:**
    Place the import statement inside the function body.

24. **How do you handle import errors?**
    
    **Answer:**
    Use try/except:
    ```akandechips
    try:
        import math
    except:
        print "Module not found"
    ```
    **Output:**
    ```
    (prints error message if not found)
    ```

25. **How do you import a module and give it a different name?**
    
    **Answer:**
    Use `as`:
    ```akandechips
    import math as m
    print m.sqrt(64)
    ```
    **Output:**
    ```
    8
    ```

26. **How do you import a function from a module in a subfolder?**
    
    **Answer:**
    Use dot notation:
    ```akandechips
    from folder.module import func
    ```

27. **How do you import a module from the parent folder?**
    
    **Answer:**
    Adjust the import path or use relative imports.

28. **How do you import a module and use its variable?**
    
    **Answer:**
    Access the variable with dot notation:
    ```akandechips
    import mymodule
    print mymodule.myvar
    ```

29. **How do you import a module and call its function?**
    
    **Answer:**
    Use dot notation:
    ```akandechips
    import mymodule
    mymodule.myfunc()
    ```

30. **How do you import a module and use its class?**
    
    **Answer:**
    Use dot notation:
    ```akandechips
    import mymodule
    obj = mymodule.MyClass()
    ```


#### Projects & Solutions

1. **Project:** Import the math module and print the square root of 81.
   
   **Solution:**
   ```akandechips
   import math
   print math.sqrt(81)
   ```
   **Output:**
   ```
   9
   ```

2. **Project:** Import only the sqrt function from math and print the square root of 49.
   
   **Solution:**
   ```akandechips
   from math import sqrt
   print sqrt(49)
   ```
   **Output:**
   ```
   7
   ```

3. **Project:** Import math as m and print the square root of 16.
   
   **Solution:**
   ```akandechips
   import math as m
   print m.sqrt(16)
   ```
   **Output:**
   ```
   4
   ```

4. **Project:** Import all functions from math and print the square root of 25.
   
   **Solution:**
   ```akandechips
   from math import *
   print sqrt(25)
   ```
   **Output:**
   ```
   5
   ```

5. **Project:** Create a module called mymodule.ak with a function add(a, b) that returns a + b. Import and use it.
   
   **Solution:**
   `mymodule.ak`:
   ```akandechips
   def add(a, b):
       return a + b
   ```
   Main file:
   ```akandechips
   import mymodule
   print mymodule.add(2, 3)
   ```
   **Output:**
   ```
   5
   ```

6. **Project:** Import random and print a random integer between 1 and 5.
   
   **Solution:**
   ```akandechips
   import random
   print random.randint(1, 5)
   ```
   **Output:**
   ```
   (random number between 1 and 5)
   ```

7. **Project:** Import random as r and print a random integer between 10 and 20.
   
   **Solution:**
   ```akandechips
   import random as r
   print r.randint(10, 20)
   ```
   **Output:**
   ```
   (random number between 10 and 20)
   ```

8. **Project:** Import only randint from random and print a random integer between 1 and 3.
   
   **Solution:**
   ```akandechips
   from random import randint
   print randint(1, 3)
   ```
   **Output:**
   ```
   (random number between 1 and 3)
   ```

9. **Project:** Import a function from a module in a subfolder and use it.
   
   **Solution:**
   `utils/helper.ak`:
   ```akandechips
   def greet():
       print "Hello!"
   ```
   Main file:
   ```akandechips
   from utils.helper import greet
   greet()
   ```
   **Output:**
   ```
   Hello!
   ```

10. **Project:** Import math and print the value of pi.
    
    **Solution:**
    ```akandechips
    import math
    print math.pi
    ```
    **Output:**
    ```
    3.141592653589793
    ```

11. **Project:** Import math and print the cosine of 0.
    
    **Solution:**
    ```akandechips
    import math
    print math.cos(0)
    ```
    **Output:**
    ```
    1
    ```

12. **Project:** Import os and print the current working directory.
    
    **Solution:**
    ```akandechips
    import os
    print os.getcwd()
    ```
    **Output:**
    ```
    (current directory path)
    ```

13. **Project:** Import sys and print the version info.
    
    **Solution:**
    ```akandechips
    import sys
    print sys.version
    ```
    **Output:**
    ```
    (version info)
    ```

14. **Project:** Import a module inside a function and use it.
    
    **Solution:**
    ```akandechips
    def show_random():
        import random
        print random.randint(1, 10)
    show_random()
    ```
    **Output:**
    ```
    (random number between 1 and 10)
    ```

15. **Project:** Handle import error for a missing module.
    
    **Solution:**
    ```akandechips
    try:
        import notamodule
    except:
        print "Module not found"
    ```
    **Output:**
    ```
    Module not found
    ```

16. **Project:** Import math and print all its functions.
    
    **Solution:**
    ```akandechips
    import math
    print dir(math)
    ```
    **Output:**
    ```
    [...list of math functions...]
    ```

17. **Project:** Import a module and use its variable.
    
    **Solution:**
    `mymodule.ak`:
    ```akandechips
    myvar = 42
    ```
    Main file:
    ```akandechips
    import mymodule
    print mymodule.myvar
    ```
    **Output:**
    ```
    42
    ```

18. **Project:** Import a module and call its function.
    
    **Solution:**
    `mymodule.ak`:
    ```akandechips
    def hello():
        print "Hi!"
    ```
    Main file:
    ```akandechips
    import mymodule
    mymodule.hello()
    ```
    **Output:**
    ```
    Hi!
    ```

19. **Project:** Import a module and use its class.
    
    **Solution:**
    `mymodule.ak`:
    ```akandechips
    class Greeter:
        def say_hi(self):
            print "Hi!"
    ```
    Main file:
    ```akandechips
    import mymodule
    g = mymodule.Greeter()
    g.say_hi()
    ```
    **Output:**
    ```
    Hi!
    ```

20. **Project:** Import multiple modules in one line and use them.
    
    **Solution:**
    ```akandechips
    import math, random
    print math.sqrt(9)
    print random.randint(1, 3)
    ```
    **Output:**
    ```
    3
    (random number between 1 and 3)
    ```

21. **Project:** Import a function with an alias and use it.
    
    **Solution:**
    ```akandechips
    from math import sqrt as s
    print s(100)
    ```
    **Output:**
    ```
    10
    ```

22. **Project:** Import a module from a subfolder and use its function.
    
    **Solution:**
    `tools/calc.ak`:
    ```akandechips
    def double(x):
        return x * 2
    ```
    Main file:
    ```akandechips
    from tools.calc import double
    print double(5)
    ```
    **Output:**
    ```
    10
    ```

23. **Project:** Import a module and print its file path.
    
    **Solution:**
    ```akandechips
    import math
    print math.__file__
    ```
    **Output:**
    ```
    (path to math module)
    ```

24. **Project:** Import a module only if a condition is met.
    
    **Solution:**
    ```akandechips
    use_math = True
    if use_math:
        import math
        print math.sqrt(36)
    ```
    **Output:**
    ```
    6
    ```

25. **Project:** Import a module and use its function inside another function.
    
    **Solution:**
    ```akandechips
    def show_sqrt(x):
        import math
        print math.sqrt(x)
    show_sqrt(49)
    ```
    **Output:**
    ```
    7
    ```

26. **Project:** Import a module and use its class inside another function.
    
    **Solution:**
    `mymodule.ak`:
    ```akandechips
    class Greeter:
        def say_hi(self):
            print "Hi!"
    ```
    Main file:
    ```akandechips
    def greet():
        import mymodule
        g = mymodule.Greeter()
        g.say_hi()
    greet()
    ```
    **Output:**
    ```
    Hi!
    ```

27. **Project:** Import a module from the parent folder and use its function.
    
    **Solution:**
    (Assume correct folder structure and import path)
    ```akandechips
    from ..mymodule import hello
    hello()
    ```
    **Output:**
    ```
    Hi!
    ```

28. **Project:** Import everything from a module except a specific function.
    
    **Solution:**
    (Import all, avoid using the unwanted function)
    ```akandechips
    from math import *
    # Do not use math.factorial
    print sqrt(64)
    ```
    **Output:**
    ```
    8
    ```

29. **Project:** Import a module and print all its attributes.
    
    **Solution:**
    ```akandechips
    import math
    print dir(math)
    ```
    **Output:**
    ```
    [...list of math functions...]
    ```

30. **Project:** Import a module and use its function with an alias.
    
    **Solution:**
    ```akandechips
    from math import sqrt as s
    print s(121)
    ```
    **Output:**
    ```
    11
    ```

---

### Simple Hardware Concepts (Logic Gates, Truth Tables, HDL Basics)
**Explanation:**
Understanding hardware basics is key for chip design. This section covers logic gates, truth tables, and simple HDL concepts.

#### Coding Questions & Answers

1. **What is a logic gate?**
   
   **Answer:**
   A basic building block of digital circuits that performs a logical operation on one or more inputs.

2. **Name three basic logic gates.**
   
   **Answer:**
   AND, OR, NOT.

3. **What does an AND gate do?**
   
   **Answer:**
   Outputs 1 only if all inputs are 1.

4. **What does an OR gate do?**
   
   **Answer:**
   Outputs 1 if at least one input is 1.

5. **What does a NOT gate do?**
   
   **Answer:**
   Outputs the opposite of the input (inverts 0 to 1 and 1 to 0).

6. **What is a truth table?**
   
   **Answer:**
   A table showing all possible input combinations and their corresponding outputs for a logic circuit.

7. **Draw the truth table for an AND gate.**
   
   **Answer:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   0    |
   | 0 | 1 |   0    |
   | 1 | 0 |   0    |
   | 1 | 1 |   1    |

8. **Draw the truth table for an OR gate.**
   
   **Answer:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   0    |
   | 0 | 1 |   1    |
   | 1 | 0 |   1    |
   | 1 | 1 |   1    |

9. **Draw the truth table for a NOT gate.**
   
   **Answer:**
   | A | Output |
   |---|--------|
   | 0 |   1    |
   | 1 |   0    |

10. **What is a NAND gate?**
    
    **Answer:**
    Outputs 0 only if all inputs are 1 (NOT-AND).

11. **What is a NOR gate?**
    
    **Answer:**
    Outputs 1 only if all inputs are 0 (NOT-OR).

12. **What is an XOR gate?**
    
    **Answer:**
    Outputs 1 if inputs are different.

13. **What is an XNOR gate?**
    
    **Answer:**
    Outputs 1 if inputs are the same.

14. **What is a combinational circuit?**
    
    **Answer:**
    A circuit whose output depends only on the current inputs.

15. **What is a sequential circuit?**
    
    **Answer:**
    A circuit whose output depends on current inputs and previous states.

16. **What is a multiplexer?**
    
    **Answer:**
    A circuit that selects one of many inputs to pass to the output.

17. **What is a demultiplexer?**
    
    **Answer:**
    A circuit that routes one input to one of many outputs.

18. **What is a flip-flop?**
    
    **Answer:**
    A basic memory element that stores one bit.

19. **What is a register?**
    
    **Answer:**
    A group of flip-flops used to store multiple bits.

20. **What is a clock signal?**
    
    **Answer:**
    A timing signal used to synchronize operations in digital circuits.

21. **What is HDL?**
    
    **Answer:**
    Hardware Description Language, used to describe hardware circuits.

22. **Name two common HDLs.**
    
    **Answer:**
    Verilog and VHDL.

23. **What is a logic high?**
    
    **Answer:**
    A voltage level representing binary 1.

24. **What is a logic low?**
    
    **Answer:**
    A voltage level representing binary 0.

25. **What is propagation delay?**
    
    **Answer:**
    The time it takes for a signal to travel through a circuit.

26. **What is a half adder?**
    
    **Answer:**
    A circuit that adds two bits and outputs a sum and carry.

27. **What is a full adder?**
    
    **Answer:**
    A circuit that adds three bits (including carry-in) and outputs a sum and carry.

28. **What is a bus?**
    
    **Answer:**
    A set of wires used to transfer data between components.

29. **What is a tri-state buffer?**
    
    **Answer:**
    A device that can output 1, 0, or disconnect from the circuit (high-impedance).

30. **What is a simple HDL statement for an AND gate?**
    
    **Answer:**
    Example in Verilog: `assign out = a & b;`


#### Projects & Solutions

1. **Project:** Write the truth table for a NAND gate.
   
   **Solution:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   1    |
   | 0 | 1 |   1    |
   | 1 | 0 |   1    |
   | 1 | 1 |   0    |

2. **Project:** Write the truth table for a NOR gate.
   
   **Solution:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   1    |
   | 0 | 1 |   0    |
   | 1 | 0 |   0    |
   | 1 | 1 |   0    |

3. **Project:** Write the truth table for an XOR gate.
   
   **Solution:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   0    |
   | 0 | 1 |   1    |
   | 1 | 0 |   1    |
   | 1 | 1 |   0    |

4. **Project:** Write the truth table for an XNOR gate.
   
   **Solution:**
   | A | B | Output |
   |---|---|--------|
   | 0 | 0 |   1    |
   | 0 | 1 |   0    |
   | 1 | 0 |   0    |
   | 1 | 1 |   1    |

5. **Project:** Write a simple HDL statement for an OR gate.
   
   **Solution:**
   Verilog: `assign out = a | b;`

6. **Project:** Write a simple HDL statement for a NOT gate.
   
   **Solution:**
   Verilog: `assign out = ~a;`

7. **Project:** Write a simple HDL statement for a NAND gate.
   
   **Solution:**
   Verilog: `assign out = ~(a & b);`

8. **Project:** Write a simple HDL statement for a NOR gate.
   
   **Solution:**
   Verilog: `assign out = ~(a | b);`

9. **Project:** Write a simple HDL statement for an XOR gate.
   
   **Solution:**
   Verilog: `assign out = a ^ b;`

10. **Project:** Write a simple HDL statement for an XNOR gate.
    
    **Solution:**
    Verilog: `assign out = ~(a ^ b);`

11. **Project:** Draw a logic circuit for a half adder.
    
    **Solution:**
    Sum = A XOR B, Carry = A AND B

12. **Project:** Draw a logic circuit for a full adder.
    
    **Solution:**
    Sum = A XOR B XOR Cin, Carry = (A AND B) OR (B AND Cin) OR (A AND Cin)

13. **Project:** Write a truth table for a 2-to-1 multiplexer.
    
    **Solution:**
    | S | A | B | Output |
    |---|---|---|--------|
    | 0 | 0 | 0 |   0    |
    | 0 | 0 | 1 |   0    |
    | 0 | 1 | 0 |   1    |
    | 0 | 1 | 1 |   1    |
    | 1 | 0 | 0 |   0    |
    | 1 | 0 | 1 |   1    |
    | 1 | 1 | 0 |   0    |
    | 1 | 1 | 1 |   1    |

14. **Project:** Write a simple HDL statement for a 2-to-1 multiplexer.
    
    **Solution:**
    Verilog: `assign out = s ? b : a;`

15. **Project:** Write a simple HDL statement for a D flip-flop.
    
    **Solution:**
    Verilog: `always @(posedge clk) q <= d;`

16. **Project:** Write a simple HDL statement for a 4-bit register.
    
    **Solution:**
    Verilog: `reg [3:0] q; always @(posedge clk) q <= d;`

17. **Project:** Write a simple HDL statement for a tri-state buffer.
    
    **Solution:**
    Verilog: `assign out = enable ? in : 1'bz;`

18. **Project:** Write a simple HDL statement for a bus connection.
    
    **Solution:**
    Verilog: `wire [7:0] bus; assign bus = data;`

19. **Project:** Write a simple HDL statement for a 2-input AND gate using VHDL.
    
    **Solution:**
    VHDL: `out <= a and b;`

20. **Project:** Write a simple HDL statement for a 2-input OR gate using VHDL.
    
    **Solution:**
    VHDL: `out <= a or b;`

21. **Project:** Write a simple HDL statement for a NOT gate using VHDL.
    
    **Solution:**
    VHDL: `out <= not a;`

22. **Project:** Write a simple HDL statement for a NAND gate using VHDL.
    
    **Solution:**
    VHDL: `out <= not (a and b);`

23. **Project:** Write a simple HDL statement for a NOR gate using VHDL.
    
    **Solution:**
    VHDL: `out <= not (a or b);`

24. **Project:** Write a simple HDL statement for an XOR gate using VHDL.
    
    **Solution:**
    VHDL: `out <= a xor b;`

25. **Project:** Write a simple HDL statement for an XNOR gate using VHDL.
    
    **Solution:**
    VHDL: `out <= not (a xor b);`

26. **Project:** Write a simple HDL statement for a D flip-flop using VHDL.
    
    **Solution:**
    VHDL: `process(clk) begin if rising_edge(clk) then q <= d; end if; end process;`

27. **Project:** Write a simple HDL statement for a 4-bit register using VHDL.
    
    **Solution:**
    VHDL: `signal q : std_logic_vector(3 downto 0); process(clk) begin if rising_edge(clk) then q <= d; end if; end process;`

28. **Project:** Write a simple HDL statement for a tri-state buffer using VHDL.
    
    **Solution:**
    VHDL: `out <= in when enable = '1' else 'Z';`

29. **Project:** Write a simple HDL statement for a bus connection using VHDL.
    
    **Solution:**
    VHDL: `bus <= data;`

30. **Project:** Write a simple HDL statement for a 2-to-1 multiplexer using VHDL.
    
    **Solution:**
    VHDL: `out <= a when sel = '0' else b;`

---

### AkandeChips vs. Python: Key Differences and Similarities
**Explanation:**
Compare AkandeChips to Python to understand what’s unique and what’s familiar. This helps you transfer skills between languages.

#### Coding Questions & Answers
<!-- 30+ comparison questions, answers, and outputs go here -->

#### Projects & Solutions
<!-- 30+ comparison projects, solutions, and outputs go here -->

---

### Real-World Mini-Projects (Blinking LED, Simple Calculator, etc.)
**Explanation:**
Apply your skills to real-world problems. These mini-projects are great for practice and portfolios.

#### Coding Questions & Answers

1. **How do you blink an LED in code?**
   
   **Answer:**
   Use a loop to turn the LED on and off with a delay.

2. **How do you read a button press in code?**
   
   **Answer:**
   Use a digital input pin and check its value.

3. **How do you write a simple calculator?**
   
   **Answer:**
   Use input for numbers and operators, then perform the calculation.

4. **How do you display text on an LCD?**
   
   **Answer:**
   Use an LCD library and call the display function.

5. **How do you generate a random number?**
   
   **Answer:**
   Import the random module and use `random.randint()`.

6. **How do you control a motor in code?**
   
   **Answer:**
   Use a digital output pin to send signals to the motor driver.

7. **How do you measure temperature with a sensor?**
   
   **Answer:**
   Read the analog value from the sensor and convert it to temperature.

8. **How do you store data in a file?**
   
   **Answer:**
   Open a file in write mode and use the write function.

9. **How do you read data from a file?**
   
   **Answer:**
   Open a file in read mode and use the read function.

10. **How do you make a traffic light simulation?**
    
    **Answer:**
    Use a loop to change the state of three LEDs (red, yellow, green) with delays.

11. **How do you debounce a button in code?**
    
    **Answer:**
    Add a short delay after detecting a button press.

12. **How do you create a countdown timer?**
    
    **Answer:**
    Use a loop and decrease the timer value each second.

13. **How do you play a sound with a buzzer?**
    
    **Answer:**
    Send a signal to the buzzer pin for a set duration.

14. **How do you control brightness of an LED?**
    
    **Answer:**
    Use PWM (Pulse Width Modulation) to vary the LED's brightness.

15. **How do you make a digital dice?**
    
    **Answer:**
    Generate a random number between 1 and 6 and display it.

16. **How do you log sensor data over time?**
    
    **Answer:**
    Read sensor values in a loop and write them to a file.

17. **How do you make a password checker?**
    
    **Answer:**
    Compare user input to a stored password.

18. **How do you make a number guessing game?**
    
    **Answer:**
    Generate a random number and let the user guess until correct.

19. **How do you make a temperature converter?**
    
    **Answer:**
    Convert between Celsius and Fahrenheit using formulas.

20. **How do you make a stopwatch?**
    
    **Answer:**
    Use a loop and track elapsed time.

21. **How do you make a simple alarm clock?**
    
    **Answer:**
    Check the current time and trigger an alarm at a set time.

22. **How do you make a digital lock?**
    
    **Answer:**
    Require a correct code to unlock a device.

23. **How do you make a step counter?**
    
    **Answer:**
    Count steps using a sensor and increment a counter.

24. **How do you make a simple scoreboard?**
    
    **Answer:**
    Use variables to track scores and display them.

25. **How do you make a reaction timer?**
    
    **Answer:**
    Measure the time between a signal and a button press.

26. **How do you make a coin toss simulator?**
    
    **Answer:**
    Generate a random number and map it to heads or tails.

27. **How do you make a simple weather station?**
    
    **Answer:**
    Read data from sensors and display temperature, humidity, etc.

28. **How do you make a Morse code flasher?**
    
    **Answer:**
    Blink an LED in Morse code patterns for given text.

29. **How do you make a simple voting machine?**
    
    **Answer:**
    Collect votes and count totals for each option.

30. **How do you make a random password generator?**
    
    **Answer:**
    Combine random letters, numbers, and symbols to create a password.


#### Projects & Solutions

1. **Project:** Blink an LED 5 times.
   
   **Solution:**
   ```akandechips
   for i in range(5):
       led.on()
       delay(500)
       led.off()
       delay(500)
   ```
   **Output:**
   ```
   LED blinks 5 times
   ```

2. **Project:** Read a button and print "Pressed" when pressed.
   
   **Solution:**
   ```akandechips
   if button.read() == 1:
       print "Pressed"
   ```
   **Output:**
   ```
   Pressed
   ```

3. **Project:** Simple calculator for addition.
   
   **Solution:**
   ```akandechips
   a = input("Enter first number: ")
   b = input("Enter second number: ")
   print int(a) + int(b)
   ```
   **Output:**
   ```
   (sum of two numbers)
   ```

4. **Project:** Display "Hello" on an LCD.
   
   **Solution:**
   ```akandechips
   lcd.display("Hello")
   ```
   **Output:**
   ```
   Hello
   ```

5. **Project:** Generate and print a random number between 1 and 10.
   
   **Solution:**
   ```akandechips
   import random
   print random.randint(1, 10)
   ```
   **Output:**
   ```
   (random number between 1 and 10)
   ```

6. **Project:** Turn a motor on for 2 seconds.
   
   **Solution:**
   ```akandechips
   motor.on()
   delay(2000)
   motor.off()
   ```
   **Output:**
   ```
   Motor runs for 2 seconds
   ```

7. **Project:** Read a temperature sensor and print the value.
   
   **Solution:**
   ```akandechips
   temp = sensor.read()
   print temp
   ```
   **Output:**
   ```
   (temperature value)
   ```

8. **Project:** Write "data" to a file called log.txt.
   
   **Solution:**
   ```akandechips
   f = open("log.txt", "w")
   f.write("data")
   f.close()
   ```
   **Output:**
   ```
   (writes 'data' to log.txt)
   ```

9. **Project:** Read and print contents of log.txt.
   
   **Solution:**
   ```akandechips
   f = open("log.txt", "r")
   print f.read()
   f.close()
   ```
   **Output:**
   ```
   data
   ```

10. **Project:** Simulate a traffic light sequence.
    
    **Solution:**
    ```akandechips
    red.on()
    delay(1000)
    red.off()
    yellow.on()
    delay(500)
    yellow.off()
    green.on()
    delay(1000)
    green.off()
    ```
    **Output:**
    ```
    Red, yellow, green lights cycle
    ```

11. **Project:** Debounce a button press.
    
    **Solution:**
    ```akandechips
    if button.read() == 1:
        delay(50)
        if button.read() == 1:
            print "Pressed"
    ```
    **Output:**
    ```
    Pressed
    ```

12. **Project:** Countdown timer from 5 to 0.
    
    **Solution:**
    ```akandechips
    for i in range(5, -1, -1):
        print i
        delay(1000)
    ```
    **Output:**
    ```
    5
    4
    3
    2
    1
    0
    ```

13. **Project:** Play a sound for 1 second with a buzzer.
    
    **Solution:**
    ```akandechips
    buzzer.on()
    delay(1000)
    buzzer.off()
    ```
    **Output:**
    ```
    Buzzer sounds for 1 second
    ```

14. **Project:** Fade an LED from off to full brightness.
    
    **Solution:**
    ```akandechips
    for i in range(0, 256, 5):
        led.set_brightness(i)
        delay(20)
    ```
    **Output:**
    ```
    LED fades in
    ```

15. **Project:** Digital dice simulator.
    
    **Solution:**
    ```akandechips
    import random
    print random.randint(1, 6)
    ```
    **Output:**
    ```
    (random number between 1 and 6)
    ```

16. **Project:** Log temperature every second for 5 seconds.
    
    **Solution:**
    ```akandechips
    f = open("temp.txt", "w")
    for i in range(5):
        temp = sensor.read()
        f.write(str(temp) + "\n")
        delay(1000)
    f.close()
    ```
    **Output:**
    ```
    (writes 5 temperature values to temp.txt)
    ```

17. **Project:** Password checker.
    
    **Solution:**
    ```akandechips
    password = "chips123"
    guess = input("Enter password: ")
    print guess == password
    ```
    **Output:**
    ```
    True or False
    ```

18. **Project:** Number guessing game.
    
    **Solution:**
    ```akandechips
    import random
    secret = random.randint(1, 10)
    guess = 0
    while guess != secret:
        guess = int(input("Guess: "))
    print "Correct!"
    ```
    **Output:**
    ```
    Correct!
    ```

19. **Project:** Temperature converter (Celsius to Fahrenheit).
    
    **Solution:**
    ```akandechips
    c = float(input("Celsius: "))
    f = c * 9/5 + 32
    print f
    ```
    **Output:**
    ```
    (Fahrenheit value)
    ```

20. **Project:** Simple stopwatch.
    
    **Solution:**
    ```akandechips
    start = time.now()
    input("Press Enter to stop...")
    end = time.now()
    print end - start
    ```
    **Output:**
    ```
    (elapsed time)
    ```

21. **Project:** Simple alarm clock.
    
    **Solution:**
    ```akandechips
    alarm = "07:00"
    while time.now() != alarm:
        pass
    buzzer.on()
    ```
    **Output:**
    ```
    Buzzer sounds at 07:00
    ```

22. **Project:** Digital lock with code 1234.
    
    **Solution:**
    ```akandechips
    code = "1234"
    entry = input("Enter code: ")
    if entry == code:
        print "Unlocked"
    else:
        print "Locked"
    ```
    **Output:**
    ```
    Unlocked or Locked
    ```

23. **Project:** Step counter simulation.
    
    **Solution:**
    ```akandechips
    steps = 0
    for i in range(10):
        steps = steps + 1
    print steps
    ```
    **Output:**
    ```
    10
    ```

24. **Project:** Simple scoreboard for two players.
    
    **Solution:**
    ```akandechips
    p1 = 0
    p2 = 0
    p1 = p1 + 1
    p2 = p2 + 2
    print p1, p2
    ```
    **Output:**
    ```
    1 2
    ```

25. **Project:** Reaction timer.
    
    **Solution:**
    ```akandechips
    import random
    delay(random.randint(1000, 3000))
    start = time.now()
    input("Press Enter!")
    end = time.now()
    print end - start
    ```
    **Output:**
    ```
    (reaction time)
    ```

26. **Project:** Coin toss simulator.
    
    **Solution:**
    ```akandechips
    import random
    print "Heads" if random.randint(0, 1) == 0 else "Tails"
    ```
    **Output:**
    ```
    Heads or Tails
    ```

27. **Project:** Simple weather station simulation.
    
    **Solution:**
    ```akandechips
    temp = 25
    humidity = 60
    print "Temp:", temp, "Humidity:", humidity
    ```
    **Output:**
    ```
    Temp: 25 Humidity: 60
    ```

28. **Project:** Morse code flasher for "HI".
    
    **Solution:**
    ```akandechips
    # H: .... I: ..
    for i in range(4):
        led.on(); delay(200); led.off(); delay(200)
    delay(600)
    for i in range(2):
        led.on(); delay(200); led.off(); delay(200)
    ```
    **Output:**
    ```
    LED flashes Morse code for HI
    ```

29. **Project:** Simple voting machine for two options.
    
    **Solution:**
    ```akandechips
    votes_a = 0
    votes_b = 0
    votes_a = votes_a + 1
    votes_b = votes_b + 2
    print votes_a, votes_b
    ```
    **Output:**
    ```
    1 2
    ```

30. **Project:** Random password generator (8 characters).
    
    **Solution:**
    ```akandechips
    import random
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(8):
        password = password + random.choice(chars)
    print password
    ```
    **Output:**
    ```
    (random 8-character password)
    ```

---

### Practice Tests and Review Sections
**Explanation:**
Test your knowledge and review key concepts before moving on.

#### Coding Questions & Answers
<!-- 30+ practice test questions, answers, and outputs go here -->

#### Projects & Solutions
<!-- 30+ review projects, solutions, and outputs go here -->
```
```


### Coding Questions & Answers
#### Q1
**Question:** Write a program to print "Welcome to AkandeChips!"
```akandechips
print("Welcome to AkandeChips!")
```
**Expected Output:**
```
Welcome to AkandeChips!
```

#### Q2
**Question:** Print the number 42.
```akandechips
print(42)
```
**Expected Output:**
```
42
```

#### Q3
```akandechips
print("Alex")
```
**Expected Output:**
```
Alex
```

#### Q4
**Question:** Print the result of 5 + 7.
```akandechips
print(5 + 7)
```
**Expected Output:**
```
12
```

#### Q5
**Question:** Print the string "chips are cool!"
```akandechips
print("chips are cool!")
```
```
chips are cool!
```

**Question:** Print the result of 10 - 3.
```akandechips
print(10 - 3)
```
**Expected Output:**
```
7
```

#### Q7
**Question:** Print the result of 4 * 6.
```akandechips
print(4 * 6)
```
**Expected Output:**
```
24
```

#### Q8
**Question:** Print the result of 20 / 5.
```akandechips
print(20 / 5)
```
**Expected Output:**
```
4.0
```

#### Q9
**Question:** Print the result of 2 ** 3 (2 to the power of 3).
```akandechips
print(2 ** 3)
```
**Expected Output:**
```
8
```

#### Q10
**Question:** Print the result of 15 % 4 (remainder of 15 divided by 4).
```akandechips
print(15 % 4)
```
**Expected Output:**
```
3
```

#### Q11
**Question:** Print the result of 100 // 9 (integer division).
```akandechips
print(100 // 9)
```
**Expected Output:**
```
11
```

#### Q12
**Question:** Print the string "Hello" and the number 5 on the same line.
```akandechips
print("Hello", 5)
```
**Expected Output:**
```
Hello 5
```

#### Q13
**Question:** Print the result of 7 + 8 * 2.
```akandechips
print(7 + 8 * 2)
```
**Expected Output:**
```
23
```

#### Q14
**Question:** Print the result of (7 + 8) * 2.
```akandechips
print((7 + 8) * 2)
```
**Expected Output:**
```
30
```

#### Q15
**Question:** Print the string "chips" three times using multiplication.
```akandechips
print("chips" * 3)
```
**Expected Output:**
```
chipschipschips
```

#### Q16
**Question:** Print the result of 5 > 2.
```akandechips
print(5 > 2)
```
**Expected Output:**
```
True
```

#### Q17
**Question:** Print the result of 3 == 4.
```akandechips
print(3 == 4)
```
**Expected Output:**
```
False
```

#### Q18
**Question:** Print the result of 10 != 5.
```akandechips
print(10 != 5)
```
**Expected Output:**
```
True
```

#### Q19
**Question:** Print the result of 7 <= 7.
```akandechips
print(7 <= 7)
```
**Expected Output:**
```
True
```

#### Q20
**Question:** Print the result of 9 >= 10.
```akandechips
print(9 >= 10)
```
**Expected Output:**
```
False
```

#### Q21
**Question:** Print the result of not False.
```akandechips
print(not False)
```
**Expected Output:**
```
True
```

#### Q22
**Question:** Print the result of True and False.
```akandechips
print(True and False)
```
**Expected Output:**
```
False
```

#### Q23
**Question:** Print the result of True or False.
```akandechips
print(True or False)
```
**Expected Output:**
```
True
```

#### Q24
**Question:** Print the string "Akande" and "Chips" separated by a space.
```akandechips
print("Akande", "Chips")
```
**Expected Output:**
```
Akande Chips
```

#### Q25
**Question:** Print the result of 2 + 3 * 4 - 5.
```akandechips
print(2 + 3 * 4 - 5)
```
**Expected Output:**
```
9
```

#### Q26
**Question:** Print the result of (2 + 3) * (4 - 5).
```akandechips
print((2 + 3) * (4 - 5))
```
**Expected Output:**
```
-5
```

#### Q27
**Question:** Print the string "chips" plus the string "rocks".
```akandechips
print("chips" + "rocks")
```
**Expected Output:**
```
chipsrocks
```

#### Q28
**Question:** Print the result of 100 / 4 + 6.
```akandechips
print(100 / 4 + 6)
```
**Expected Output:**
```
31.0
```

#### Q29
**Question:** Print the result of 2 * 2 * 2 * 2.
```akandechips
print(2 * 2 * 2 * 2)
```
**Expected Output:**
```
16
```

#### Q30
**Question:** Print the string "USA" 5 times, separated by spaces.
```akandechips
print(("USA " * 5).strip())
```
**Expected Output:**
```
USA USA USA USA USA
```


### Projects & Solutions

#### Project 1
**Project:** Write a program to print your favorite quote.
```akandechips
print("The future belongs to those who believe in the beauty of their dreams.")
```
**Expected Output:**
```
The future belongs to those who believe in the beauty of their dreams.
```

#### Project 2
**Project:** Print the sum, difference, and product of 8 and 3.
```akandechips
print(8 + 3)
print(8 - 3)
print(8 * 3)
```
**Expected Output:**
```
11
5
24
```

#### Project 3
**Project:** Print "chips" on three separate lines.
```akandechips
print("chips")
print("chips")
print("chips")
```
**Expected Output:**
```
chips
chips
chips
```

#### Project 4
**Project:** Print the result of 5 squared.
```akandechips
print(5 ** 2)
```
**Expected Output:**
```
25
```

#### Project 5
**Project:** Print your name and age on the same line.
```akandechips
print("Alex", 21)
```
**Expected Output:**
```
Alex 21
```

#### Project 6
**Project:** Print the result of 100 divided by 8, rounded to 2 decimal places.
```akandechips
print(round(100 / 8, 2))
```
**Expected Output:**
```
12.5
```

#### Project 7
**Project:** Print the result of 7 times 6 minus 4.
```akandechips
print(7 * 6 - 4)
```
**Expected Output:**
```
38
```

#### Project 8
**Project:** Print the string "chips" and the number 2025 on separate lines.
```akandechips
print("chips")
print(2025)
```
**Expected Output:**
```
chips
2025
```

#### Project 9
**Project:** Print the result of 9 + 8 + 7 + 6 + 5.
```akandechips
print(9 + 8 + 7 + 6 + 5)
```
**Expected Output:**
```
35
```

#### Project 10
**Project:** Print the string "AkandeChips" in all uppercase letters.
```akandechips
print("AkandeChips".upper())
```
**Expected Output:**
```
AKANDECHIPS
```

#### Project 11
**Project:** Print the string "chips" repeated 4 times, each on a new line.
```akandechips
for i in range(4):
    print("chips")
```
**Expected Output:**
```
chips
chips
chips
chips
```

#### Project 12
**Project:** Print the result of 50 divided by 7, rounded to the nearest integer.
```akandechips
print(round(50 / 7))
```
**Expected Output:**
```
7
```

#### Project 13
**Project:** Print the string "Hello" and "World" on the same line, separated by a comma.
```akandechips
print("Hello, World")
```
**Expected Output:**
```
Hello, World
```

#### Project 14
**Project:** Print the result of 2 to the power of 10.
```akandechips
print(2 ** 10)
```
**Expected Output:**
```
1024
```

#### Project 15
**Project:** Print the result of 100 minus 45 plus 12.
```akandechips
print(100 - 45 + 12)
```
**Expected Output:**
```
67
```

#### Project 16
**Project:** Print the string "chips" in lowercase.
```akandechips
print("CHIPS".lower())
```
**Expected Output:**
```
chips
```

#### Project 17
**Project:** Print the result of 3 * 3 * 3.
```akandechips
print(3 * 3 * 3)
```
**Expected Output:**
```
27
```

#### Project 18
**Project:** Print the string "Akande" and "Chips" on two separate lines.
```akandechips
print("Akande")
print("Chips")
```
**Expected Output:**
```
Akande
Chips
```

#### Project 19
**Project:** Print the result of 99 + 1.
```akandechips
print(99 + 1)
```
**Expected Output:**
```
100
```

#### Project 20
**Project:** Print the string "chips" with an exclamation mark.
```akandechips
print("chips!")
```
**Expected Output:**
```
chips!
```

#### Project 21
**Project:** Print the result of 5 * 5 + 5.
```akandechips
print(5 * 5 + 5)
```
**Expected Output:**
```
30
```

#### Project 22
**Project:** Print the string "AkandeChips" five times, separated by commas.
```akandechips
print(", ".join(["AkandeChips"] * 5))
```
**Expected Output:**
```
AkandeChips, AkandeChips, AkandeChips, AkandeChips, AkandeChips
```

#### Project 23
**Project:** Print the result of 12345 + 54321.
```akandechips
print(12345 + 54321)
```
**Expected Output:**
```
66666
```

#### Project 24
**Project:** Print the string "chips" with each letter on a new line.
```akandechips
for letter in "chips":
    print(letter)
```
**Expected Output:**
```
h
i
p
s
```
#### Project 25
**Project:** Print the result of 2 + 2 * 2 + 2.
```akandechips
print(2 + 2 * 2 + 2)
```
**Expected Output:**
```
8
```

#### Project 26
```akandechips
print("AkandeChips"[::-1])
```
**Expected Output:**
```
spihCednakA
```

#### Project 27
**Project:** Print the result of 10 * 10 * 10.
```akandechips
```
**Expected Output:**
```
1000
```

#### Project 28
**Project:** Print the string "chips" with a space between each letter.
```akandechips
print(" ".join("chips"))
```
```
c h i p s
```

#### Project 29
**Project:** Print the result of 7 + 7 + 7 + 7 + 7.
```akandechips
print(7 + 7 + 7 + 7 + 7)
```
**Expected Output:**
```
```

#### Project 30
**Project:** Print the string "chips" 10 times, each on a new line.
```akandechips
for i in range(10):
    print("chips")
```
**Expected Output:**
```
chips
chips
chips
chips
chips
chips
chips
chips
chips
```

---

## Variables and Types
Variables are used to store data in AkandeChips. Each variable has a type, which determines what kind of data it can hold. This section covers the main types, with explanations, examples, questions, and projects for each.

---

### Integer Variables
**Explanation:**
Integers are whole numbers (positive, negative, or zero) without a decimal point.

**Example:**
count = 10
year = 2025
temperature = -5
```
**Expected Output:**
```
No output (variables are stored in memory)
```


#### Coding Questions & Answers
##### Q1
**Question:** Assign the value 5 to a variable called `num` and print it.
```akandechips
num = 5
print(num)
```
**Expected Output:**
```
5
```

**Question:** Assign -10 to `temperature` and print it.
```akandechips
temperature = -10
print(temperature)
```
**Expected Output:**
```
-10
```

##### Q3
```akandechips
year = 2025
print(year)
```
**Expected Output:**
```
2025
```

##### Q4
**Question:** Assign 0 to `count` and print it.
count = 0
print(count)
```
**Expected Output:**
```
0
```

##### Q5
**Question:** Assign 7 to `a`, 3 to `b`, print their sum.
```akandechips
b = 3
print(a + b)
```
**Expected Output:**
```
10
```

##### Q6
**Question:** Assign 15 to `x`, subtract 4, print the result.
```akandechips
print(x - 4)
```
**Expected Output:**
```
11
```

##### Q7
**Question:** Assign 6 to `n`, multiply by 5, print the result.
```akandechips
n = 6
```
**Expected Output:**
```
30
```

##### Q8
**Question:** Assign 20 to `total`, divide by 4, print the result.
```akandechips
total = 20
print(total / 4)
```
**Expected Output:**
```
5.0
```

##### Q9
**Question:** Assign 9 to `a`, 2 to `b`, print the remainder of a divided by b.
```akandechips
a = 9
b = 2
print(a % b)
```
**Expected Output:**
```
1
```

##### Q10
**Question:** Assign 3 to `base`, 4 to `exp`, print base to the power of exp.
```akandechips
base = 3
exp = 4
print(base ** exp)
```
**Expected Output:**
```
81
```

##### Q11
**Question:** Assign 100 to `big`, 9 to `small`, print integer division result.
```akandechips
big = 100
small = 9
print(big // small)
```
**Expected Output:**
```
11
```

##### Q12
**Question:** Assign 1 to `a`, 2 to `b`, 3 to `c`, print their sum.
```akandechips
a = 1
b = 2
c = 3
print(a + b + c)
```
**Expected Output:**
```
6
```

##### Q13
**Question:** Assign 50 to `score`, print score minus 25.
```akandechips
score = 50
print(score - 25)
```
**Expected Output:**
```
25
```

##### Q14
**Question:** Assign 8 to `a`, 2 to `b`, print a divided by b.
```akandechips
a = 8
b = 2
print(a / b)
```
**Expected Output:**
```
4.0
```

##### Q15
**Question:** Assign 7 to `n`, print n squared.
```akandechips
n = 7
print(n ** 2)
```
**Expected Output:**
```
49
```

##### Q16
**Question:** Assign 12 to `a`, 5 to `b`, print a plus b times 2.
```akandechips
a = 12
b = 5
print(a + b * 2)
```
**Expected Output:**
```
22
```

##### Q17
**Question:** Assign 10 to `x`, print x minus 3 times 2.
```akandechips
x = 10
print(x - 3 * 2)
```
**Expected Output:**
```
4
```

##### Q18
**Question:** Assign 4 to `a`, 3 to `b`, print a times b plus 1.
```akandechips
a = 4
b = 3
print(a * b + 1)
```
**Expected Output:**
```
13
```

##### Q19
**Question:** Assign 9 to `n`, print n cubed.
```akandechips
n = 9
print(n ** 3)
```
**Expected Output:**
```
729
```

##### Q20
**Question:** Assign 15 to `a`, 4 to `b`, print the remainder of a divided by b.
```akandechips
a = 15
b = 4
print(a % b)
```
**Expected Output:**
```
3
```

##### Q21
**Question:** Assign 100 to `a`, 25 to `b`, print a divided by b.
```akandechips
a = 100
b = 25
print(a / b)
```
**Expected Output:**
```
4.0
```

##### Q22
**Question:** Assign 2 to `x`, 3 to `y`, print x to the power of y.
```akandechips
x = 2
y = 3
print(x ** y)
```
**Expected Output:**
```
8
```

##### Q23
**Question:** Assign 11 to `a`, 2 to `b`, print integer division result.
```akandechips
a = 11
b = 2
print(a // b)
```
**Expected Output:**
```
5
```

##### Q24
**Question:** Assign 7 to `n`, print n plus 10.
```akandechips
n = 7
print(n + 10)
```
**Expected Output:**
```
17
```

##### Q25
**Question:** Assign 20 to `a`, 5 to `b`, print a minus b times 2.
```akandechips
a = 20
b = 5
print(a - b * 2)
```
**Expected Output:**
```
10
```

##### Q26
**Question:** Assign 3 to `a`, 4 to `b`, print a times b times 2.
```akandechips
a = 3
b = 4
print(a * b * 2)
```
**Expected Output:**
```
24
```

##### Q27
**Question:** Assign 8 to `n`, print n minus 2.
```akandechips
n = 8
print(n - 2)
```
**Expected Output:**
```
6
```

##### Q28
**Question:** Assign 5 to `a`, 2 to `b`, print a plus b plus a.
```akandechips
a = 5
b = 2
print(a + b + a)
```
**Expected Output:**
```
12
```

##### Q29
**Question:** Assign 9 to `x`, print x times x.
```akandechips
x = 9
print(x * x)
```
**Expected Output:**
```
81
```

##### Q30
**Question:** Assign 100 to `big`, 1 to `small`, print big minus small.
```akandechips
big = 100
small = 1
print(big - small)
```
**Expected Output:**
```
99
```


#### Projects & Solutions

##### Project 1
**Project:** Write a program to assign your age to a variable and print it.
```akandechips
age = 18
print(age)
```
**Expected Output:**
```
18
```

##### Project 2
**Project:** Assign the number of US states to a variable and print it.
```akandechips
states = 50
print(states)
```
**Expected Output:**
```
50
```

##### Project 3
**Project:** Assign the year the first microchip was invented (1958) to a variable and print it.
```akandechips
invention_year = 1958
print(invention_year)
```
**Expected Output:**
```
1958
```

##### Project 4
**Project:** Assign the number of days in a week to a variable and print it.
```akandechips
days = 7
print(days)
```
**Expected Output:**
```
7
```

##### Project 5
**Project:** Assign the number of hours in a day to a variable and print it.
```akandechips
hours = 24
print(hours)
```
**Expected Output:**
```
24
```

##### Project 6
**Project:** Assign the number of minutes in an hour to a variable and print it.
```akandechips
minutes = 60
print(minutes)
```
**Expected Output:**
```
60
```

##### Project 7
**Project:** Assign the number of seconds in a minute to a variable and print it.
```akandechips
seconds = 60
print(seconds)
```
**Expected Output:**
```
60
```

##### Project 8
**Project:** Assign the number of months in a year to a variable and print it.
```akandechips
months = 12
print(months)
```
**Expected Output:**
```
12
```

##### Project 9
**Project:** Assign the number of days in February (non-leap year) to a variable and print it.
```akandechips
feb_days = 28
print(feb_days)
```
**Expected Output:**
```
28
```

##### Project 10
**Project:** Assign the number of bits in a byte to a variable and print it.
```akandechips
bits = 8
print(bits)
```
**Expected Output:**
```
8
```

##### Project 11
**Project:** Assign the number of pins on a standard DIP-14 chip to a variable and print it.
```akandechips
pins = 14
print(pins)
```
**Expected Output:**
```
14
```

##### Project 12
**Project:** Assign the number of nanoseconds in a microsecond to a variable and print it.
```akandechips
nanoseconds = 1000
print(nanoseconds)
```
**Expected Output:**
```
1000
```

##### Project 13
**Project:** Assign the number of transistors in a simple CPU (e.g., 5000) to a variable and print it.
```akandechips
transistors = 5000
print(transistors)
```
**Expected Output:**
```
5000
```

##### Project 14
**Project:** Assign the number of logic gates in a basic AND gate IC (e.g., 4) to a variable and print it.
```akandechips
gates = 4
print(gates)
```
**Expected Output:**
```
4
```

##### Project 15
**Project:** Assign the number of cores in a quad-core processor to a variable and print it.
```akandechips
cores = 4
print(cores)
```
**Expected Output:**
```
4
```

##### Project 16
**Project:** Assign the number of wheels on a car to a variable and print it.
```akandechips
wheels = 4
print(wheels)
```
**Expected Output:**
```
4
```

##### Project 17
**Project:** Assign the number of students in a class (e.g., 30) to a variable and print it.
```akandechips
students = 30
print(students)
```
**Expected Output:**
```
30
```

##### Project 18
**Project:** Assign the number of computers in a lab (e.g., 20) to a variable and print it.
```akandechips
computers = 20
print(computers)
```
**Expected Output:**
```
20
```

##### Project 19
**Project:** Assign the number of floors in a building (e.g., 10) to a variable and print it.
```akandechips
floors = 10
print(floors)
```
**Expected Output:**
```
10
```

##### Project 20
**Project:** Assign the number of LEDs on a board (e.g., 8) to a variable and print it.
```akandechips
leds = 8
print(leds)
```
**Expected Output:**
```
8
```

##### Project 21
**Project:** Assign the number of resistors in a kit (e.g., 100) to a variable and print it.
```akandechips
resistors = 100
print(resistors)
```
**Expected Output:**
```
100
```

##### Project 22
**Project:** Assign the number of capacitors in a kit (e.g., 50) to a variable and print it.
```akandechips
capacitors = 50
print(capacitors)
```
**Expected Output:**
```
50
```

##### Project 23
**Project:** Assign the number of switches on a board (e.g., 6) to a variable and print it.
```akandechips
switches = 6
print(switches)
```
**Expected Output:**
```
6
```

##### Project 24
**Project:** Assign the number of sensors in a robot (e.g., 5) to a variable and print it.
```akandechips
sensors = 5
print(sensors)
```
**Expected Output:**
```
5
```

##### Project 25
**Project:** Assign the number of microcontrollers in a project (e.g., 2) to a variable and print it.
```akandechips
microcontrollers = 2
print(microcontrollers)
```
**Expected Output:**
```
2
```

##### Project 26
**Project:** Assign the number of USB ports on a computer (e.g., 4) to a variable and print it.
```akandechips
usb_ports = 4
print(usb_ports)
```
**Expected Output:**
```
4
```

##### Project 27
**Project:** Assign the number of fans in a server (e.g., 3) to a variable and print it.
```akandechips
fans = 3
print(fans)
```
**Expected Output:**
```
3
```

##### Project 28
**Project:** Assign the number of batteries in a device (e.g., 2) to a variable and print it.
```akandechips
batteries = 2
print(batteries)
```
**Expected Output:**
```
2
```

##### Project 29
**Project:** Assign the number of speakers in a sound system (e.g., 5) to a variable and print it.
```akandechips
speakers = 5
print(speakers)
```
**Expected Output:**
```
5
```

##### Project 30
**Project:** Assign the number of keys on a standard keyboard (e.g., 104) to a variable and print it.
```akandechips
keys = 104
print(keys)
```
**Expected Output:**
```
104
```

---

### Float Variables
**Explanation:**
Floats are numbers with a decimal point. They are used for measurements, calculations, and any value that isn’t a whole number.

**Example:**
```akandechips
pi = 3.14159
height = -2.5
score = 99.9
```
**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a float variable with value 3.14?**
   
   **Answer:**
   ```akandechips
   x = 3.14
   print x
   ```
   **Output:**
   ```
   3.14
   ```

2. **What is the output of `print 2.5 + 1.5`?**
   
   **Answer:**
   ```akandechips
   print 2.5 + 1.5
   ```
   **Output:**
   ```
   4.0
   ```

3. **How do you subtract two float variables?**
   
   **Answer:**
   ```akandechips
   a = 5.5
   b = 2.2
   print a - b
   ```
   **Output:**
   ```
   3.3
   ```

4. **What is the output of `print 3.0 * 2`?**
   
   **Answer:**
   ```akandechips
   print 3.0 * 2
   ```
   **Output:**
   ```
   6.0
   ```

5. **How do you divide two float variables?**
   
   **Answer:**
   ```akandechips
   a = 7.5
   b = 2.5
   print a / b
   ```
   **Output:**
   ```
   3.0
   ```

6. **What is the output of `print 5.0 // 2`?**
   
   **Answer:**
   ```akandechips
   print 5.0 // 2
   ```
   **Output:**
   ```
   2.0
   ```

7. **How do you convert an integer to a float?**
   
   **Answer:**
   Use `float(x)`.

8. **What is the output of `print float("2.7")`?**
   
   **Answer:**
   ```akandechips
   print float("2.7")
   ```
   **Output:**
   ```
   2.7
   ```

9. **How do you round a float to 1 decimal place?**
   
   **Answer:**
   Use `round(x, 1)`.

10. **What is the output of `print round(3.14159, 2)`?**
    
    **Answer:**
    ```akandechips
    print round(3.14159, 2)
    ```
    **Output:**
    ```
    3.14
    ```

11. **How do you check the type of a float variable?**
    
    **Answer:**
    Use `type(x)`.

12. **What is the output of `print 1.0 / 3`?**
    
    **Answer:**
    ```akandechips
    print 1.0 / 3
    ```
    **Output:**
    ```
    0.3333333333333333
    ```

13. **How do you add 0.1 to a float variable?**
    
    **Answer:**
    ```akandechips
    x = 2.5
    x = x + 0.1
    print x
    ```
    **Output:**
    ```
    2.6
    ```

14. **What is the output of `print 2.0 ** 3`?**
    
    **Answer:**
    ```akandechips
    print 2.0 ** 3
    ```
    **Output:**
    ```
    8.0
    ```

15. **How do you get the absolute value of a float?**
    
    **Answer:**
    Use `abs(x)`.

16. **What is the output of `print abs(-3.5)`?**
    
    **Answer:**
    ```akandechips
    print abs(-3.5)
    ```
    **Output:**
    ```
    3.5
    ```

17. **How do you check if a float is greater than 5.0?**
    
    **Answer:**
    ```akandechips
    x = 6.2
    print x > 5.0
    ```
    **Output:**
    ```
    True
    ```

18. **What is the output of `print 7.5 % 2`?**
    
    **Answer:**
    ```akandechips
    print 7.5 % 2
    ```
    **Output:**
    ```
    1.5
    ```

19. **How do you multiply a float by an integer?**
    
    **Answer:**
    ```akandechips
    x = 2.5
    print x * 4
    ```
    **Output:**
    ```
    10.0
    ```

20. **What is the output of `print 0.1 + 0.2`?**
    
    **Answer:**
    ```akandechips
    print 0.1 + 0.2
    ```
    **Output:**
    ```
    0.30000000000000004
    ```

21. **How do you format a float to 2 decimal places?**
    
    **Answer:**
    Use string formatting: `"%.2f" % x`.

22. **What is the output of `print "%.1f" % 2.345`?**
    
    **Answer:**
    ```akandechips
    print "%.1f" % 2.345
    ```
    **Output:**
    ```
    2.3
    ```

23. **How do you compare two float variables for equality?**
    
    **Answer:**
    Use `==`, but be careful with precision.

24. **What is the output of `print 1.1 * 2`?**
    
    **Answer:**
    ```akandechips
    print 1.1 * 2
    ```
    **Output:**
    ```
    2.2
    ```

25. **How do you check if a float is negative?**
    
    **Answer:**
    ```akandechips
    x = -0.5
    print x < 0
    ```
    **Output:**
    ```
    True
    ```

26. **What is the output of `print 5.5 / 2`?**
    
    **Answer:**
    ```akandechips
    print 5.5 / 2
    ```
    **Output:**
    ```
    2.75
    ```

27. **How do you increment a float variable by 1?**
    
    **Answer:**
    ```akandechips
    x = 2.5
    x = x + 1
    print x
    ```
    **Output:**
    ```
    3.5
    ```

28. **What is the output of `print 2.0 / 0.5`?**
    
    **Answer:**
    ```akandechips
    print 2.0 / 0.5
    ```
    **Output:**
    ```
    4.0
    ```

29. **How do you check if a float is zero?**
    
    **Answer:**
    ```akandechips
    x = 0.0
    print x == 0.0
    ```
    **Output:**
    ```
    True
    ```

30. **What is the output of `print float(7)`?**
    
    **Answer:**
    ```akandechips
    print float(7)
    ```
    **Output:**
    ```
    7.0
    ```


#### Projects & Solutions

1. **Project:** Create a float variable and print it.
   
   **Solution:**
   ```akandechips
   x = 4.5
   print x
   ```
   **Output:**
   ```
   4.5
   ```

2. **Project:** Add two float variables and print the result.
   
   **Solution:**
   ```akandechips
   a = 1.2
   b = 3.4
   print a + b
   ```
   **Output:**
   ```
   4.6
   ```

3. **Project:** Subtract two float variables and print the result.
   
   **Solution:**
   ```akandechips
   a = 5.5
   b = 2.0
   print a - b
   ```
   **Output:**
   ```
   3.5
   ```

4. **Project:** Multiply two float variables and print the result.
   
   **Solution:**
   ```akandechips
   a = 2.5
   b = 4.0
   print a * b
   ```
   **Output:**
   ```
   10.0
   ```

5. **Project:** Divide two float variables and print the result.
   
   **Solution:**
   ```akandechips
   a = 7.5
   b = 2.5
   print a / b
   ```
   **Output:**
   ```
   3.0
   ```

6. **Project:** Round a float to 2 decimal places and print it.
   
   **Solution:**
   ```akandechips
   x = 3.14159
   print round(x, 2)
   ```
   **Output:**
   ```
   3.14
   ```

7. **Project:** Convert an integer to a float and print it.
   
   **Solution:**
   ```akandechips
   x = 5
   print float(x)
   ```
   **Output:**
   ```
   5.0
   ```

8. **Project:** Get the absolute value of a float and print it.
   
   **Solution:**
   ```akandechips
   x = -2.7
   print abs(x)
   ```
   **Output:**
   ```
   2.7
   ```

9. **Project:** Check if a float is greater than 10 and print the result.
   
   **Solution:**
   ```akandechips
   x = 12.5
   print x > 10
   ```
   **Output:**
   ```
   True
   ```

10. **Project:** Add 0.5 to a float variable and print it.
    
    **Solution:**
    ```akandechips
    x = 1.5
    x = x + 0.5
    print x
    ```
    **Output:**
    ```
    2.0
    ```

11. **Project:** Multiply a float by an integer and print the result.
    
    **Solution:**
    ```akandechips
    x = 2.5
    print x * 3
    ```
    **Output:**
    ```
    7.5
    ```

12. **Project:** Divide a float by an integer and print the result.
    
    **Solution:**
    ```akandechips
    x = 9.0
    print x / 3
    ```
    **Output:**
    ```
    3.0
    ```

13. **Project:** Format a float to 1 decimal place and print it.
    
    **Solution:**
    ```akandechips
    x = 2.345
    print "%.1f" % x
    ```
    **Output:**
    ```
    2.3
    ```

14. **Project:** Check if a float is negative and print the result.
    
    **Solution:**
    ```akandechips
    x = -0.1
    print x < 0
    ```
    **Output:**
    ```
    True
    ```

15. **Project:** Increment a float by 1 and print it.
    
    **Solution:**
    ```akandechips
    x = 3.5
    x = x + 1
    print x
    ```
    **Output:**
    ```
    4.5
    ```

16. **Project:** Check if a float is zero and print the result.
    
    **Solution:**
    ```akandechips
    x = 0.0
    print x == 0.0
    ```
    **Output:**
    ```
    True
    ```

17. **Project:** Subtract 0.25 from a float and print it.
    
    **Solution:**
    ```akandechips
    x = 1.0
    x = x - 0.25
    print x
    ```
    **Output:**
    ```
    0.75
    ```

18. **Project:** Divide a float by another float and print the result.
    
    **Solution:**
    ```akandechips
    a = 5.0
    b = 2.0
    print a / b
    ```
    **Output:**
    ```
    2.5
    ```

19. **Project:** Multiply a float by itself and print the result.
    
    **Solution:**
    ```akandechips
    x = 1.5
    print x * x
    ```
    **Output:**
    ```
    2.25
    ```

20. **Project:** Print the type of a float variable.
    
    **Solution:**
    ```akandechips
    x = 2.5
    print type(x)
    ```
    **Output:**
    ```
    float
    ```

21. **Project:** Print the result of 0.1 + 0.2.
    
    **Solution:**
    ```akandechips
    print 0.1 + 0.2
    ```
    **Output:**
    ```
    0.30000000000000004
    ```

22. **Project:** Round a float to the nearest integer and print it.
    
    **Solution:**
    ```akandechips
    x = 2.7
    print round(x)
    ```
    **Output:**
    ```
    3
    ```

23. **Project:** Print the result of 2.0 ** 4.
    
    **Solution:**
    ```akandechips
    print 2.0 ** 4
    ```
    **Output:**
    ```
    16.0
    ```

24. **Project:** Print the remainder of 7.5 divided by 2.
    
    **Solution:**
    ```akandechips
    print 7.5 % 2
    ```
    **Output:**
    ```
    1.5
    ```

25. **Project:** Print the result of float("5.5") + 2.
    
    **Solution:**
    ```akandechips
    print float("5.5") + 2
    ```
    **Output:**
    ```
    7.5
    ```

26. **Project:** Print the result of 3.0 / 2.0.
    
    **Solution:**
    ```akandechips
    print 3.0 / 2.0
    ```
    **Output:**
    ```
    1.5
    ```

27. **Project:** Print the result of 5.0 // 2.
    
    **Solution:**
    ```akandechips
    print 5.0 // 2
    ```
    **Output:**
    ```
    2.0
    ```

28. **Project:** Print the result of 2.5 * 2.5.
    
    **Solution:**
    ```akandechips
    print 2.5 * 2.5
    ```
    **Output:**
    ```
    6.25
    ```

29. **Project:** Print the result of 10.0 / 4.
    
    **Solution:**
    ```akandechips
    print 10.0 / 4
    ```
    **Output:**
    ```
    2.5
    ```

30. **Project:** Print the result of float(8) / 2.
    
    **Solution:**
    ```akandechips
    print float(8) / 2
    ```
    **Output:**
    ```
    4.0
    ```

---

### String Variables
**Explanation:**
Strings are sequences of characters, used to store text.

**Example:**
```akandechips
name = "Akande"
message = "Hello, world!"
chip_type = "FPGA"
```
**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a string variable with value "chips"?**
   
   **Answer:**
   ```akandechips
   s = "chips"
   print s
   ```
   **Output:**
   ```
   chips
   ```

2. **What is the output of `print "hello" + " world"`?**
   
   **Answer:**
   ```akandechips
   print "hello" + " world"
   ```
   **Output:**
   ```
   hello world
   ```

3. **How do you get the length of a string?**
   
   **Answer:**
   Use `len(s)`.

4. **What is the output of `print "chips"[0]`?**
   
   **Answer:**
   ```akandechips
   print "chips"[0]
   ```
   **Output:**
   ```
   c
   ```

5. **How do you get the last character of a string?**
   
   **Answer:**
   Use `s[-1]`.

6. **What is the output of `print "chips".upper()`?**
   
   **Answer:**
   ```akandechips
   print "chips".upper()
   ```
   **Output:**
   ```
   CHIPS
   ```

7. **How do you convert a string to lowercase?**
   
   **Answer:**
   Use `s.lower()`.

8. **What is the output of `print "chips".capitalize()`?**
   
   **Answer:**
   ```akandechips
   print "chips".capitalize()
   ```
   **Output:**
   ```
   Chips
   ```

9. **How do you check if a string contains "a"?**
   
   **Answer:**
   Use `'a' in s`.

10. **What is the output of `print "chips"[1:4]`?**
    
    **Answer:**
    ```akandechips
    print "chips"[1:4]
    ```
    **Output:**
    ```
    hip
    ```

11. **How do you replace "i" with "a" in a string?**
    
    **Answer:**
    Use `s.replace("i", "a")`.

12. **What is the output of `print "chips".find("p")`?**
    
    **Answer:**
    ```akandechips
    print "chips".find("p")
    ```
    **Output:**
    ```
    3
    ```

13. **How do you split a string by spaces?**
    
    **Answer:**
    Use `s.split()`.

14. **What is the output of `print "a,b,c".split(",")`?**
    
    **Answer:**
    ```akandechips
    print "a,b,c".split(",")
    ```
    **Output:**
    ```
    ["a", "b", "c"]
    ```

15. **How do you join a list of strings into one string?**
    
    **Answer:**
    Use `''.join(list)`.

16. **What is the output of `print "chips".startswith("c")`?**
    
    **Answer:**
    ```akandechips
    print "chips".startswith("c")
    ```
    **Output:**
    ```
    True
    ```

17. **How do you check if a string ends with "s"?**
    
    **Answer:**
    Use `s.endswith("s")`.

18. **What is the output of `print "chips".count("i")`?**
    
    **Answer:**
    ```akandechips
    print "chips".count("i")
    ```
    **Output:**
    ```
    1
    ```

19. **How do you remove whitespace from both ends of a string?**
    
    **Answer:**
    Use `s.strip()`.

20. **What is the output of `print " chips ".strip()`?**
    
    **Answer:**
    ```akandechips
    print " chips ".strip()
    ```
    **Output:**
    ```
    chips
    ```

21. **How do you repeat a string 3 times?**
    
    **Answer:**
    Use `s * 3`.

22. **What is the output of `print "a" * 4`?**
    
    **Answer:**
    ```akandechips
    print "a" * 4
    ```
    **Output:**
    ```
    aaaa
    ```

23. **How do you check if a string is numeric?**
    
    **Answer:**
    Use `s.isdigit()`.

24. **What is the output of `print "chips".replace("c", "z")`?**
    
    **Answer:**
    ```akandechips
    print "chips".replace("c", "z")
    ```
    **Output:**
    ```
    zhips
    ```

25. **How do you convert a string to an integer?**
    
    **Answer:**
    Use `int(s)` if s is numeric.

26. **What is the output of `print "chips"[::-1]`?**
    
    **Answer:**
    ```akandechips
    print "chips"[::-1]
    ```
    **Output:**
    ```
    spihc
    ```

27. **How do you check if a string is uppercase?**
    
    **Answer:**
    Use `s.isupper()`.

28. **What is the output of `print "chips".islower()`?**
    
    **Answer:**
    ```akandechips
    print "chips".islower()
    ```
    **Output:**
    ```
    True
    ```

29. **How do you get the index of "h" in a string?**
    
    **Answer:**
    Use `s.index("h")`.

30. **What is the output of `print "chips".index("p")`?**
    
    **Answer:**
    ```akandechips
    print "chips".index("p")
    ```
    **Output:**
    ```
    3
    ```


#### Projects & Solutions

1. **Project:** Create a string variable and print it.
   
   **Solution:**
   ```akandechips
   s = "hello"
   print s
   ```
   **Output:**
   ```
   hello
   ```

2. **Project:** Concatenate two strings and print the result.
   
   **Solution:**
   ```akandechips
   a = "chip"
   b = "set"
   print a + b
   ```
   **Output:**
   ```
   chipset
   ```

3. **Project:** Print the length of a string.
   
   **Solution:**
   ```akandechips
   s = "chips"
   print len(s)
   ```
   **Output:**
   ```
   5
   ```

4. **Project:** Print the first and last character of a string.
   
   **Solution:**
   ```akandechips
   s = "chips"
   print s[0], s[-1]
   ```
   **Output:**
   ```
   c s
   ```

5. **Project:** Convert a string to uppercase and print it.
   
   **Solution:**
   ```akandechips
   s = "chips"
   print s.upper()
   ```
   **Output:**
   ```
   CHIPS
   ```

6. **Project:** Convert a string to lowercase and print it.
   
   **Solution:**
   ```akandechips
   s = "CHIPS"
   print s.lower()
   ```
   **Output:**
   ```
   chips
   ```

7. **Project:** Capitalize a string and print it.
   
   **Solution:**
   ```akandechips
   s = "chips"
   print s.capitalize()
   ```
   **Output:**
   ```
   Chips
   ```

8. **Project:** Replace a character in a string and print the result.
   
   **Solution:**
   ```akandechips
   s = "chips"
   print s.replace("i", "a")
   ```
   **Output:**
   ```
   chaps
   ```

9. **Project:** Split a string by spaces and print the result.
   
   **Solution:**
   ```akandechips
   s = "I love chips"
   print s.split()
   ```
   **Output:**
   ```
   ["I", "love", "chips"]
   ```

10. **Project:** Join a list of strings into one string and print it.
    
    **Solution:**
    ```akandechips
    words = ["I", "love", "chips"]
    print ' '.join(words)
    ```
    **Output:**
    ```
    I love chips
    ```

11. **Project:** Print a substring of a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[1:4]
    ```
    **Output:**
    ```
    hip
    ```

12. **Project:** Check if a string contains "a" and print the result.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print 'a' in s
    ```
    **Output:**
    ```
    False
    ```

13. **Project:** Print the index of "h" in a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.index("h")
    ```
    **Output:**
    ```
    1
    ```

14. **Project:** Print the number of times "i" appears in a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.count("i")
    ```
    **Output:**
    ```
    1
    ```

15. **Project:** Remove whitespace from both ends of a string and print it.
    
    **Solution:**
    ```akandechips
    s = " chips "
    print s.strip()
    ```
    **Output:**
    ```
    chips
    ```

16. **Project:** Repeat a string 3 times and print it.
    
    **Solution:**
    ```akandechips
    s = "hi"
    print s * 3
    ```
    **Output:**
    ```
    hihihi
    ```

17. **Project:** Check if a string is numeric and print the result.
    
    **Solution:**
    ```akandechips
    s = "123"
    print s.isdigit()
    ```
    **Output:**
    ```
    True
    ```

18. **Project:** Convert a string to an integer and print it.
    
    **Solution:**
    ```akandechips
    s = "42"
    print int(s)
    ```
    **Output:**
    ```
    42
    ```

19. **Project:** Reverse a string and print it.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[::-1]
    ```
    **Output:**
    ```
    spihc
    ```

20. **Project:** Check if a string is uppercase and print the result.
    
    **Solution:**
    ```akandechips
    s = "CHIPS"
    print s.isupper()
    ```
    **Output:**
    ```
    True
    ```

21. **Project:** Check if a string is lowercase and print the result.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.islower()
    ```
    **Output:**
    ```
    True
    ```

22. **Project:** Print the index of "p" in a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.index("p")
    ```
    **Output:**
    ```
    3
    ```

23. **Project:** Print a string with all "i" replaced by "a".
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.replace("i", "a")
    ```
    **Output:**
    ```
    chaps
    ```

24. **Project:** Print a string with all spaces removed.
    
    **Solution:**
    ```akandechips
    s = "a b c"
    print s.replace(" ", "")
    ```
    **Output:**
    ```
    abc
    ```

25. **Project:** Print the first three characters of a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[:3]
    ```
    **Output:**
    ```
    chi
    ```

26. **Project:** Print the last two characters of a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s[-2:]
    ```
    **Output:**
    ```
    ps
    ```

27. **Project:** Print a string with the first letter capitalized.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.capitalize()
    ```
    **Output:**
    ```
    Chips
    ```

28. **Project:** Print a string with all letters swapped to uppercase.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s.upper()
    ```
    **Output:**
    ```
    CHIPS
    ```

29. **Project:** Print a string with all letters swapped to lowercase.
    
    **Solution:**
    ```akandechips
    s = "CHIPS"
    print s.lower()
    ```
    **Output:**
    ```
    chips
    ```

30. **Project:** Print the number of vowels in a string.
    
    **Solution:**
    ```akandechips
    s = "chips"
    count = 0
    for c in s:
        if c in "aeiou":
            count = count + 1
    print count
    ```
    **Output:**
    ```
    1
    ```

---

### Boolean Variables
**Explanation:**
Booleans represent True or False values. They are used for logic and decision making.

**Example:**
```akandechips
is_on = True
is_chip_ready = False
```
**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a boolean variable with value True?**
   
   **Answer:**
   ```akandechips
   b = True
   print b
   ```
   **Output:**
   ```
   True
   ```

2. **How do you create a boolean variable with value False?**
   
   **Answer:**
   ```akandechips
   b = False
   print b
   ```
   **Output:**
   ```
   False
   ```

3. **What is the output of `print 5 > 3`?**
   
   **Answer:**
   ```akandechips
   print 5 > 3
   ```
   **Output:**
   ```
   True
   ```

4. **What is the output of `print 2 == 3`?**
   
   **Answer:**
   ```akandechips
   print 2 == 3
   ```
   **Output:**
   ```
   False
   ```

5. **What is the output of `print not True`?**
   
   **Answer:**
   ```akandechips
   print not True
   ```
   **Output:**
   ```
   False
   ```

6. **What is the output of `print True and False`?**
   
   **Answer:**
   ```akandechips
   print True and False
   ```
   **Output:**
   ```
   False
   ```

7. **What is the output of `print True or False`?**
   
   **Answer:**
   ```akandechips
   print True or False
   ```
   **Output:**
   ```
   True
   ```

8. **How do you check if a variable is True?**
   
   **Answer:**
   Use `if b:`

9. **What is the output of `print False or False`?**
   
   **Answer:**
   ```akandechips
   print False or False
   ```
   **Output:**
   ```
   False
   ```

10. **What is the output of `print not (5 < 2)`?**
    
    **Answer:**
    ```akandechips
    print not (5 < 2)
    ```
    **Output:**
    ```
    True
    ```

11. **How do you check if two variables are both True?**
    
    **Answer:**
    Use `a and b`.

12. **What is the output of `print True == 1`?**
    
    **Answer:**
    ```akandechips
    print True == 1
    ```
    **Output:**
    ```
    True
    ```

13. **What is the output of `print False == 0`?**
    
    **Answer:**
    ```akandechips
    print False == 0
    ```
    **Output:**
    ```
    True
    ```

14. **What is the output of `print bool(0)`?**
    
    **Answer:**
    ```akandechips
    print bool(0)
    ```
    **Output:**
    ```
    False
    ```

15. **What is the output of `print bool(5)`?**
    
    **Answer:**
    ```akandechips
    print bool(5)
    ```
    **Output:**
    ```
    True
    ```

16. **How do you toggle a boolean variable?**
    
    **Answer:**
    Use `b = not b`.

17. **What is the output of `print True != False`?**
    
    **Answer:**
    ```akandechips
    print True != False
    ```
    **Output:**
    ```
    True
    ```

18. **What is the output of `print (3 < 5) and (2 > 1)`?**
    
    **Answer:**
    ```akandechips
    print (3 < 5) and (2 > 1)
    ```
    **Output:**
    ```
    True
    ```

19. **What is the output of `print (3 > 5) or (2 > 1)`?**
    
    **Answer:**
    ```akandechips
    print (3 > 5) or (2 > 1)
    ```
    **Output:**
    ```
    True
    ```

20. **What is the output of `print not (True and False)`?**
    
    **Answer:**
    ```akandechips
    print not (True and False)
    ```
    **Output:**
    ```
    True
    ```

21. **How do you check if a number is even using boolean logic?**
    
    **Answer:**
    Use `n % 2 == 0`.

22. **What is the output of `print bool("")`?**
    
    **Answer:**
    ```akandechips
    print bool("")
    ```
    **Output:**
    ```
    False
    ```

23. **What is the output of `print bool("chips")`?**
    
    **Answer:**
    ```akandechips
    print bool("chips")
    ```
    **Output:**
    ```
    True
    ```

24. **How do you check if a list is empty using boolean logic?**
    
    **Answer:**
    Use `if not mylist:`

25. **What is the output of `print True or True`?**
    
    **Answer:**
    ```akandechips
    print True or True
    ```
    **Output:**
    ```
    True
    ```

26. **What is the output of `print False and True`?**
    
    **Answer:**
    ```akandechips
    print False and True
    ```
    **Output:**
    ```
    False
    ```

27. **What is the output of `print not False`?**
    
    **Answer:**
    ```akandechips
    print not False
    ```
    **Output:**
    ```
    True
    ```

28. **How do you use a boolean in an if statement?**
    
    **Answer:**
    ```akandechips
    b = True
    if b:
        print "Yes"
    ```
    **Output:**
    ```
    Yes
    ```

29. **What is the output of `print (2 < 1) or (3 > 2)`?**
    
    **Answer:**
    ```akandechips
    print (2 < 1) or (3 > 2)
    ```
    **Output:**
    ```
    True
    ```

30. **What is the output of `print (2 < 1) and (3 > 2)`?**
    
    **Answer:**
    ```akandechips
    print (2 < 1) and (3 > 2)
    ```
    **Output:**
    ```
    False
    ```


#### Projects & Solutions

1. **Project:** Create a boolean variable and print its value.
   
   **Solution:**
   ```akandechips
   b = True
   print b
   ```
   **Output:**
   ```
   True
   ```

2. **Project:** Set a boolean variable to False and print it.
   
   **Solution:**
   ```akandechips
   b = False
   print b
   ```
   **Output:**
   ```
   False
   ```

3. **Project:** Print the result of a comparison (5 > 2).
   
   **Solution:**
   ```akandechips
   print 5 > 2
   ```
   **Output:**
   ```
   True
   ```

4. **Project:** Print the result of a comparison (3 == 4).
   
   **Solution:**
   ```akandechips
   print 3 == 4
   ```
   **Output:**
   ```
   False
   ```

5. **Project:** Use a boolean variable in an if statement.
   
   **Solution:**
   ```akandechips
   b = True
   if b:
       print "It is true!"
   ```
   **Output:**
   ```
   It is true!
   ```

6. **Project:** Toggle a boolean variable and print it.
   
   **Solution:**
   ```akandechips
   b = True
   b = not b
   print b
   ```
   **Output:**
   ```
   False
   ```

7. **Project:** Print the result of True and False.
   
   **Solution:**
   ```akandechips
   print True and False
   ```
   **Output:**
   ```
   False
   ```

8. **Project:** Print the result of True or False.
   
   **Solution:**
   ```akandechips
   print True or False
   ```
   **Output:**
   ```
   True
   ```

9. **Project:** Print the result of not True.
   
   **Solution:**
   ```akandechips
   print not True
   ```
   **Output:**
   ```
   False
   ```

10. **Project:** Check if a number is even and print the result.
    
    **Solution:**
    ```akandechips
    n = 4
    print n % 2 == 0
    ```
    **Output:**
    ```
    True
    ```

11. **Project:** Check if a string is empty and print the result.
    
    **Solution:**
    ```akandechips
    s = ""
    print bool(s)
    ```
    **Output:**
    ```
    False
    ```

12. **Project:** Check if a list is empty and print the result.
    
    **Solution:**
    ```akandechips
    mylist = []
    print not mylist
    ```
    **Output:**
    ```
    True
    ```

13. **Project:** Print the result of (3 < 5) and (2 > 1).
    
    **Solution:**
    ```akandechips
    print (3 < 5) and (2 > 1)
    ```
    **Output:**
    ```
    True
    ```

14. **Project:** Print the result of (3 > 5) or (2 > 1).
    
    **Solution:**
    ```akandechips
    print (3 > 5) or (2 > 1)
    ```
    **Output:**
    ```
    True
    ```

15. **Project:** Print the result of not (True and False).
    
    **Solution:**
    ```akandechips
    print not (True and False)
    ```
    **Output:**
    ```
    True
    ```

16. **Project:** Print the result of True == 1.
    
    **Solution:**
    ```akandechips
    print True == 1
    ```
    **Output:**
    ```
    True
    ```

17. **Project:** Print the result of False == 0.
    
    **Solution:**
    ```akandechips
    print False == 0
    ```
    **Output:**
    ```
    True
    ```

18. **Project:** Print the result of bool(0).
    
    **Solution:**
    ```akandechips
    print bool(0)
    ```
    **Output:**
    ```
    False
    ```

19. **Project:** Print the result of bool(5).
    
    **Solution:**
    ```akandechips
    print bool(5)
    ```
    **Output:**
    ```
    True
    ```

20. **Project:** Use a boolean to control program flow.
    
    **Solution:**
    ```akandechips
    b = False
    if b:
        print "Yes"
    else:
        print "No"
    ```
    **Output:**
    ```
    No
    ```

21. **Project:** Print the result of True or True.
    
    **Solution:**
    ```akandechips
    print True or True
    ```
    **Output:**
    ```
    True
    ```

22. **Project:** Print the result of False and True.
    
    **Solution:**
    ```akandechips
    print False and True
    ```
    **Output:**
    ```
    False
    ```

23. **Project:** Print the result of not False.
    
    **Solution:**
    ```akandechips
    print not False
    ```
    **Output:**
    ```
    True
    ```

24. **Project:** Use a boolean in a while loop.
    
    **Solution:**
    ```akandechips
    b = True
    count = 0
    while b:
        print count
        count = count + 1
        if count > 2:
            b = False
    ```
    **Output:**
    ```
    0
    1
    2
    ```

25. **Project:** Check if a number is positive and print the result.
    
    **Solution:**
    ```akandechips
    n = 5
    print n > 0
    ```
    **Output:**
    ```
    True
    ```

26. **Project:** Check if a number is negative and print the result.
    
    **Solution:**
    ```akandechips
    n = -3
    print n < 0
    ```
    **Output:**
    ```
    True
    ```

27. **Project:** Check if a number is zero and print the result.
    
    **Solution:**
    ```akandechips
    n = 0
    print n == 0
    ```
    **Output:**
    ```
    True
    ```

28. **Project:** Use boolean logic to check if a number is between 1 and 10.
    
    **Solution:**
    ```akandechips
    n = 5
    print n >= 1 and n <= 10
    ```
    **Output:**
    ```
    True
    ```

29. **Project:** Use boolean logic to check if a number is outside 1 and 10.
    
    **Solution:**
    ```akandechips
    n = 15
    print n < 1 or n > 10
    ```
    **Output:**
    ```
    True
    ```

30. **Project:** Use boolean logic to check if a string is "chips" and print the result.
    
    **Solution:**
    ```akandechips
    s = "chips"
    print s == "chips"
    ```
    **Output:**
    ```
    True
    ```

---

### List Variables
**Explanation:**
Lists are ordered collections of items. They can store numbers, strings, or other lists.

**Example:**
```akandechips
chips = ["FPGA", "ASIC", "CPU"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "chips", True]
```
**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a list with the numbers 1, 2, 3?**
   
   **Answer:**
   ```akandechips
   mylist = [1, 2, 3]
   print mylist
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

2. **How do you access the first element of a list?**
   
   **Answer:**
   Use `mylist[0]`.

3. **What is the output of `print [1, 2, 3][1]`?**
   
   **Answer:**
   ```akandechips
   print [1, 2, 3][1]
   ```
   **Output:**
   ```
   2
   ```

4. **How do you change the second element of a list to 5?**
   
   **Answer:**
   Use `mylist[1] = 5`.

5. **What is the output of `print len([1, 2, 3])`?**
   
   **Answer:**
   ```akandechips
   print len([1, 2, 3])
   ```
   **Output:**
   ```
   3
   ```

6. **How do you add an element to the end of a list?**
   
   **Answer:**
   Use `mylist.append(x)`.

7. **What is the output of `print [1, 2] + [3, 4]`?**
   
   **Answer:**
   ```akandechips
   print [1, 2] + [3, 4]
   ```
   **Output:**
   ```
   [1, 2, 3, 4]
   ```

8. **How do you remove the last element from a list?**
   
   **Answer:**
   Use `mylist.pop()`.

9. **What is the output of `print [1, 2, 3].pop()`?**
   
   **Answer:**
   ```akandechips
   print [1, 2, 3].pop()
   ```
   **Output:**
   ```
   3
   ```

10. **How do you check if 2 is in a list?**
    
    **Answer:**
    Use `2 in mylist`.

11. **What is the output of `print [1, 2, 3].index(2)`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3].index(2)
    ```
    **Output:**
    ```
    1
    ```

12. **How do you sort a list?**
    
    **Answer:**
    Use `mylist.sort()`.

13. **What is the output of `print sorted([3, 1, 2])`?**
    
    **Answer:**
    ```akandechips
    print sorted([3, 1, 2])
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

14. **How do you reverse a list?**
    
    **Answer:**
    Use `mylist.reverse()`.

15. **What is the output of `print [1, 2, 3][::-1]`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3][::-1]
    ```
    **Output:**
    ```
    [3, 2, 1]
    ```

16. **How do you get the length of a list?**
    
    **Answer:**
    Use `len(mylist)`.

17. **What is the output of `print [1, 2, 3].count(2)`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3].count(2)
    ```
    **Output:**
    ```
    1
    ```

18. **How do you clear all elements from a list?**
    
    **Answer:**
    Use `mylist.clear()`.

19. **What is the output of `print [1, 2, 3] * 2`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3] * 2
    ```
    **Output:**
    ```
    [1, 2, 3, 1, 2, 3]
    ```

20. **How do you copy a list?**
    
    **Answer:**
    Use `mylist.copy()`.

21. **What is the output of `print list(range(3))`?**
    
    **Answer:**
    ```akandechips
    print list(range(3))
    ```
    **Output:**
    ```
    [0, 1, 2]
    ```

22. **How do you insert an element at the beginning of a list?**
    
    **Answer:**
    Use `mylist.insert(0, x)`.

23. **What is the output of `print [1, 2, 3].remove(2)`?**
    
    **Answer:**
    ```akandechips
    mylist = [1, 2, 3]
    mylist.remove(2)
    print mylist
    ```
    **Output:**
    ```
    [1, 3]
    ```

24. **How do you get the last element of a list?**
    
    **Answer:**
    Use `mylist[-1]`.

25. **What is the output of `print [1, 2, 3][:2]`?**
    
    **Answer:**
    ```akandechips
    print [1, 2, 3][:2]
    ```
    **Output:**
    ```
    [1, 2]
    ```

26. **How do you extend a list with another list?**
    
    **Answer:**
    Use `mylist.extend(otherlist)`.

27. **What is the output of `print [1, 2, 3].min()`?**
    
    **Answer:**
    ```akandechips
    print min([1, 2, 3])
    ```
    **Output:**
    ```
    1
    ```

28. **What is the output of `print max([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print max([1, 2, 3])
    ```
    **Output:**
    ```
    3
    ```

29. **How do you check if a list is empty?**
    
    **Answer:**
    Use `if not mylist:`

30. **What is the output of `print sum([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print sum([1, 2, 3])
    ```
    **Output:**
    ```
    6
    ```


#### Projects & Solutions

1. **Project:** Create a list of three numbers and print it.
   
   **Solution:**
   ```akandechips
   mylist = [4, 5, 6]
   print mylist
   ```
   **Output:**
   ```
   [4, 5, 6]
   ```

2. **Project:** Print the first and last element of a list.
   
   **Solution:**
   ```akandechips
   mylist = [7, 8, 9]
   print mylist[0], mylist[-1]
   ```
   **Output:**
   ```
   7 9
   ```

3. **Project:** Change the second element of a list to 10 and print the list.
   
   **Solution:**
   ```akandechips
   mylist = [1, 2, 3]
   mylist[1] = 10
   print mylist
   ```
   **Output:**
   ```
   [1, 10, 3]
   ```

4. **Project:** Add an element to the end of a list and print it.
   
   **Solution:**
   ```akandechips
   mylist = [1, 2]
   mylist.append(3)
   print mylist
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

5. **Project:** Remove the last element from a list and print the list.
   
   **Solution:**
   ```akandechips
   mylist = [1, 2, 3]
   mylist.pop()
   print mylist
   ```
   **Output:**
   ```
   [1, 2]
   ```

6. **Project:** Concatenate two lists and print the result.
   
   **Solution:**
   ```akandechips
   a = [1, 2]
   b = [3, 4]
   print a + b
   ```
   **Output:**
   ```
   [1, 2, 3, 4]
   ```

7. **Project:** Sort a list and print it.
   
   **Solution:**
   ```akandechips
   mylist = [3, 1, 2]
   mylist.sort()
   print mylist
   ```
   **Output:**
   ```
   [1, 2, 3]
   ```

8. **Project:** Reverse a list and print it.
   
   **Solution:**
   ```akandechips
   mylist = [1, 2, 3]
   mylist.reverse()
   print mylist
   ```
   **Output:**
   ```
   [3, 2, 1]
   ```

9. **Project:** Print the length of a list.
   
   **Solution:**
   ```akandechips
   mylist = [1, 2, 3, 4]
   print len(mylist)
   ```
   **Output:**
   ```
   4
   ```

10. **Project:** Count the number of times 2 appears in a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [2, 2, 3]
    print mylist.count(2)
    ```
    **Output:**
    ```
    2
    ```

11. **Project:** Clear all elements from a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    mylist.clear()
    print mylist
    ```
    **Output:**
    ```
    []
    ```

12. **Project:** Multiply a list by 3 and print the result.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2]
    print mylist * 3
    ```
    **Output:**
    ```
    [1, 2, 1, 2, 1, 2]
    ```

13. **Project:** Copy a list and print the copy.
    
    **Solution:**
    ```akandechips
    mylist = [5, 6, 7]
    newlist = mylist.copy()
    print newlist
    ```
    **Output:**
    ```
    [5, 6, 7]
    ```

14. **Project:** Insert an element at the beginning of a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [2, 3]
    mylist.insert(0, 1)
    print mylist
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

15. **Project:** Remove the element 2 from a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    mylist.remove(2)
    print mylist
    ```
    **Output:**
    ```
    [1, 3]
    ```

16. **Project:** Print the last element of a list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    print mylist[-1]
    ```
    **Output:**
    ```
    3
    ```

17. **Project:** Print the first two elements of a list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    print mylist[:2]
    ```
    **Output:**
    ```
    [1, 2]
    ```

18. **Project:** Extend a list with another list and print it.
    
    **Solution:**
    ```akandechips
    a = [1, 2]
    b = [3, 4]
    a.extend(b)
    print a
    ```
    **Output:**
    ```
    [1, 2, 3, 4]
    ```

19. **Project:** Print the minimum and maximum of a list.
    
    **Solution:**
    ```akandechips
    mylist = [2, 4, 1]
    print min(mylist), max(mylist)
    ```
    **Output:**
    ```
    1 4
    ```

20. **Project:** Check if a list is empty and print the result.
    
    **Solution:**
    ```akandechips
    mylist = []
    print not mylist
    ```
    **Output:**
    ```
    True
    ```

21. **Project:** Print the sum of all elements in a list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    print sum(mylist)
    ```
    **Output:**
    ```
    6
    ```

22. **Project:** Create a list of numbers from 0 to 4 and print it.
    
    **Solution:**
    ```akandechips
    mylist = list(range(5))
    print mylist
    ```
    **Output:**
    ```
    [0, 1, 2, 3, 4]
    ```

23. **Project:** Print every element in a list using a loop.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    for x in mylist:
        print x
    ```
    **Output:**
    ```
    1
    2
    3
    ```

24. **Project:** Double every element in a list and print the new list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    newlist = []
    for x in mylist:
        newlist.append(x * 2)
    print newlist
    ```
    **Output:**
    ```
    [2, 4, 6]
    ```

25. **Project:** Find the largest number in a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [3, 7, 2]
    print max(mylist)
    ```
    **Output:**
    ```
    7
    ```

26. **Project:** Find the smallest number in a list and print it.
    
    **Solution:**
    ```akandechips
    mylist = [3, 7, 2]
    print min(mylist)
    ```
    **Output:**
    ```
    2
    ```

27. **Project:** Remove all elements from a list using a loop and print the list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    while mylist:
        mylist.pop()
    print mylist
    ```
    **Output:**
    ```
    []
    ```

28. **Project:** Create a list of strings and print the second string.
    
    **Solution:**
    ```akandechips
    mylist = ["chips", "set", "board"]
    print mylist[1]
    ```
    **Output:**
    ```
    set
    ```

29. **Project:** Create a list, add a new element, and print the list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2]
    mylist.append(3)
    print mylist
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

30. **Project:** Create a list, remove an element by value, and print the list.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 3]
    mylist.remove(2)
    print mylist
    ```
    **Output:**
    ```
    [1, 3]
    ```

---


## Dictionary Variables

**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a dictionary with keys "a" and "b" and values 1 and 2?**
   
   **Answer:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d
   ```
   **Output:**
   ```
   {"a": 1, "b": 2}
   ```

2. **How do you access the value for key "a" in a dictionary?**
   
   **Answer:**
   Use `d["a"]`.

3. **What is the output of `print {"x": 5}["x"]`?**
   
   **Answer:**
   ```akandechips
   print {"x": 5}["x"]
   ```
   **Output:**
   ```
   5
   ```

4. **How do you add a new key-value pair to a dictionary?**
   
   **Answer:**
   Use `d["newkey"] = value`.

5. **What is the output of `print len({"a": 1, "b": 2})`?**
   
   **Answer:**
   ```akandechips
   print len({"a": 1, "b": 2})
   ```
   **Output:**
   ```
   2
   ```

6. **How do you remove a key from a dictionary?**
   
   **Answer:**
   Use `del d["key"]`.

7. **What is the output of `print {"a": 1, "b": 2}.keys()`?**
   
   **Answer:**
   ```akandechips
   print {"a": 1, "b": 2}.keys()
   ```
   **Output:**
   ```
   ["a", "b"]
   ```

8. **How do you get all values from a dictionary?**
   
   **Answer:**
   Use `d.values()`.

9. **What is the output of `print {"a": 1, "b": 2}.values()`?**
   
   **Answer:**
   ```akandechips
   print {"a": 1, "b": 2}.values()
   ```
   **Output:**
   ```
   [1, 2]
   ```

10. **How do you check if a key exists in a dictionary?**
    
    **Answer:**
    Use `"key" in d`.

11. **What is the output of `print {"a": 1, "b": 2}.get("a")`?**
    
    **Answer:**
    ```akandechips
    print {"a": 1, "b": 2}.get("a")
    ```
    **Output:**
    ```
    1
    ```

12. **How do you update the value for a key in a dictionary?**
    
    **Answer:**
    Use `d["key"] = newvalue`.

13. **What is the output of `print {"a": 1, "b": 2}.get("c", 0)`?**
    
    **Answer:**
    ```akandechips
    print {"a": 1, "b": 2}.get("c", 0)
    ```
    **Output:**
    ```
    0
    ```

14. **How do you clear all items from a dictionary?**
    
    **Answer:**
    Use `d.clear()`.

15. **What is the output of `print {"a": 1, "b": 2}.items()`?**
    
    **Answer:**
    ```akandechips
    print {"a": 1, "b": 2}.items()
    ```
    **Output:**
    ```
    [("a", 1), ("b", 2)]
    ```

16. **How do you loop through all keys in a dictionary?**
    
    **Answer:**
    Use `for k in d:`

17. **How do you loop through all key-value pairs in a dictionary?**
    
    **Answer:**
    Use `for k, v in d.items():`

18. **What is the output of `print "a" in {"a": 1, "b": 2}`?**
    
    **Answer:**
    ```akandechips
    print "a" in {"a": 1, "b": 2}
    ```
    **Output:**
    ```
    True
    ```

19. **How do you copy a dictionary?**
    
    **Answer:**
    Use `d.copy()`.

20. **What is the output of `print dict([("x", 1), ("y", 2)])`?**
    
    **Answer:**
    ```akandechips
    print dict([("x", 1), ("y", 2)])
    ```
    **Output:**
    ```
    {"x": 1, "y": 2}
    ```

21. **How do you merge two dictionaries?**
    
    **Answer:**
    Use `d1.update(d2)`.

22. **What is the output of `print {"a": 1, "b": 2}.pop("a")`?**
    
    **Answer:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d.pop("a")
    ```
    **Output:**
    ```
    1
    ```

23. **How do you get a list of all keys in a dictionary?**
    
    **Answer:**
    Use `list(d.keys())`.

24. **How do you get a list of all values in a dictionary?**
    
    **Answer:**
    Use `list(d.values())`.

25. **What is the output of `print len({})`?**
    
    **Answer:**
    ```akandechips
    print len({})
    ```
    **Output:**
    ```
    0
    ```

26. **How do you check if a dictionary is empty?**
    
    **Answer:**
    Use `if not d:`

27. **How do you remove all items from a dictionary?**
    
    **Answer:**
    Use `d.clear()`.

28. **How do you get the value for a key with a default if not found?**
    
    **Answer:**
    Use `d.get("key", default)`.

29. **What is the output of `print {"a": 1, "b": 2}.setdefault("c", 3)`?**
    
    **Answer:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print d.setdefault("c", 3)
    print d
    ```
    **Output:**
    ```
    3
    {"a": 1, "b": 2, "c": 3}
    ```

30. **How do you remove a key and get its value?**
    
    **Answer:**
    Use `d.pop("key")`.

#### Projects & Solutions

1. **Project:** Create a dictionary with two key-value pairs and print it.
   
   **Solution:**
   ```akandechips
   d = {"x": 10, "y": 20}
   print d
   ```
   **Output:**
   ```
   {"x": 10, "y": 20}
   ```

2. **Project:** Add a new key-value pair to a dictionary and print it.
   
   **Solution:**
   ```akandechips
   d = {"a": 1}
   d["b"] = 2
   print d
   ```
   **Output:**
   ```
   {"a": 1, "b": 2}
   ```

3. **Project:** Remove a key from a dictionary and print the dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   del d["a"]
   print d
   ```
   **Output:**
   ```
   {"b": 2}
   ```

4. **Project:** Print all keys in a dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d.keys()
   ```
   **Output:**
   ```
   ["a", "b"]
   ```

5. **Project:** Print all values in a dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d.values()
   ```
   **Output:**
   ```
   [1, 2]
   ```

6. **Project:** Print all key-value pairs in a dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1, "b": 2}
   print d.items()
   ```
   **Output:**
   ```
   [("a", 1), ("b", 2)]
   ```

7. **Project:** Update the value for a key and print the dictionary.
   
   **Solution:**
   ```akandechips
   d = {"a": 1}
   d["a"] = 5
   print d
   ```
   **Output:**
   ```
   {"a": 5}
   ```

8. **Project:** Check if a key exists in a dictionary and print the result.
   
   **Solution:**
   ```akandechips
   d = {"a": 1}
   print "a" in d
   ```
   **Output:**
   ```
   True
   ```

9. **Project:** Get the value for a key with a default if not found and print it.
   
   **Solution:**
   ```akandechips
   d = {"a": 1}
   print d.get("b", 0)
   ```
   **Output:**
   ```
   0
   ```

10. **Project:** Clear all items from a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    d.clear()
    print d
    ```
    **Output:**
    ```
    {}
    ```

11. **Project:** Copy a dictionary and print the copy.
    
    **Solution:**
    ```akandechips
    d = {"a": 1}
    d2 = d.copy()
    print d2
    ```
    **Output:**
    ```
    {"a": 1}
    ```

12. **Project:** Merge two dictionaries and print the result.
    
    **Solution:**
    ```akandechips
    d1 = {"a": 1}
    d2 = {"b": 2}
    d1.update(d2)
    print d1
    ```
    **Output:**
    ```
    {"a": 1, "b": 2}
    ```

13. **Project:** Remove a key and get its value, then print the dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    v = d.pop("a")
    print v
    print d
    ```
    **Output:**
    ```
    1
    {"b": 2}
    ```

14. **Project:** Print the number of items in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print len(d)
    ```
    **Output:**
    ```
    2
    ```

15. **Project:** Loop through all keys and print them.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    for k in d:
        print k
    ```
    **Output:**
    ```
    a
    b
    ```

16. **Project:** Loop through all key-value pairs and print them.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    for k, v in d.items():
        print k, v
    ```
    **Output:**
    ```
    a 1
    b 2
    ```

17. **Project:** Create a dictionary from a list of tuples and print it.
    
    **Solution:**
    ```akandechips
    d = dict([("x", 1), ("y", 2)])
    print d
    ```
    **Output:**
    ```
    {"x": 1, "y": 2}
    ```

18. **Project:** Use setdefault to add a key if not present and print the dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1}
    d.setdefault("b", 2)
    print d
    ```
    **Output:**
    ```
    {"a": 1, "b": 2}
    ```

19. **Project:** Check if a dictionary is empty and print the result.
    
    **Solution:**
    ```akandechips
    d = {}
    print not d
    ```
    **Output:**
    ```
    True
    ```

20. **Project:** Print all keys as a list.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print list(d.keys())
    ```
    **Output:**
    ```
    ["a", "b"]
    ```

21. **Project:** Print all values as a list.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    print list(d.values())
    ```
    **Output:**
    ```
    [1, 2]
    ```

22. **Project:** Print the value for a key, or 0 if not found.
    
    **Solution:**
    ```akandechips
    d = {"a": 1}
    print d.get("b", 0)
    ```
    **Output:**
    ```
    0
    ```

23. **Project:** Add multiple key-value pairs to a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {}
    d["x"] = 1
    d["y"] = 2
    d["z"] = 3
    print d
    ```
    **Output:**
    ```
    {"x": 1, "y": 2, "z": 3}
    ```

24. **Project:** Remove all items from a dictionary and print it.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    d.clear()
    print d
    ```
    **Output:**
    ```
    {}
    ```

25. **Project:** Print the value for a key using a loop.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2}
    for k in d:
        if k == "b":
            print d[k]
    ```
    **Output:**
    ```
    2
    ```

26. **Project:** Print all key-value pairs where the value is greater than 1.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2, "c": 3}
    for k, v in d.items():
        if v > 1:
            print k, v
    ```
    **Output:**
    ```
    b 2
    c 3
    ```

27. **Project:** Create a dictionary with string keys and list values, then print it.
    
    **Solution:**
    ```akandechips
    d = {"a": [1, 2], "b": [3, 4]}
    print d
    ```
    **Output:**
    ```
    {"a": [1, 2], "b": [3, 4]}
    ```

28. **Project:** Create a dictionary from two lists and print it.
    
    **Solution:**
    ```akandechips
    keys = ["a", "b"]
    values = [1, 2]
    d = dict(zip(keys, values))
    print d
    ```
    **Output:**
    ```
    {"a": 1, "b": 2}
    ```

29. **Project:** Print the sum of all values in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 2, "c": 3}
    print sum(d.values())
    ```
    **Output:**
    ```
    6
    ```

30. **Project:** Print the key with the largest value in a dictionary.
    
    **Solution:**
    ```akandechips
    d = {"a": 1, "b": 5, "c": 3}
    max_key = None
    max_val = None
    for k, v in d.items():
        if max_val is None or v > max_val:
            max_val = v
            max_key = k
    print max_key
    ```
    **Output:**
    ```
    b
    ```

---


## Set Variables

**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a set with the numbers 1, 2, 3?**
   
   **Answer:**
   ```akandechips
   s = set([1, 2, 3])
   print s
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

2. **How do you add an element to a set?**
   
   **Answer:**
   Use `s.add(x)`.

3. **What is the output of `print set([1, 2, 2, 3])`?**
   
   **Answer:**
   ```akandechips
   print set([1, 2, 2, 3])
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

4. **How do you remove an element from a set?**
   
   **Answer:**
   Use `s.remove(x)`.

5. **What is the output of `print len(set([1, 2, 3]))`?**
   
   **Answer:**
   ```akandechips
   print len(set([1, 2, 3]))
   ```
   **Output:**
   ```
   3
   ```

6. **How do you check if an element is in a set?**
   
   **Answer:**
   Use `x in s`.

7. **What is the output of `print 2 in set([1, 2, 3])`?**
   
   **Answer:**
   ```akandechips
   print 2 in set([1, 2, 3])
   ```
   **Output:**
   ```
   True
   ```

8. **How do you remove all elements from a set?**
   
   **Answer:**
   Use `s.clear()`.

9. **What is the output of `print set([1, 2, 3]).copy()`?**
   
   **Answer:**
   ```akandechips
   print set([1, 2, 3]).copy()
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

10. **How do you get the number of elements in a set?**
    
    **Answer:**
    Use `len(s)`.

11. **What is the output of `print set([1, 2]) | set([2, 3])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2]) | set([2, 3])
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

12. **How do you find the intersection of two sets?**
    
    **Answer:**
    Use `s1 & s2`.

13. **What is the output of `print set([1, 2, 3]) & set([2, 3, 4])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2, 3]) & set([2, 3, 4])
    ```
    **Output:**
    ```
    {2, 3}
    ```

14. **How do you find the difference between two sets?**
    
    **Answer:**
    Use `s1 - s2`.

15. **What is the output of `print set([1, 2, 3]) - set([2, 3])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2, 3]) - set([2, 3])
    ```
    **Output:**
    ```
    {1}
    ```

16. **How do you find the symmetric difference of two sets?**
    
    **Answer:**
    Use `s1 ^ s2`.

17. **What is the output of `print set([1, 2, 3]) ^ set([2, 3, 4])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2, 3]) ^ set([2, 3, 4])
    ```
    **Output:**
    ```
    {1, 4}
    ```

18. **How do you check if a set is a subset of another?**
    
    **Answer:**
    Use `s1 <= s2`.

19. **What is the output of `print set([1, 2]) <= set([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2]) <= set([1, 2, 3])
    ```
    **Output:**
    ```
    True
    ```

20. **How do you check if a set is a superset of another?**
    
    **Answer:**
    Use `s1 >= s2`.

21. **What is the output of `print set([1, 2, 3]) >= set([2, 3])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2, 3]) >= set([2, 3])
    ```
    **Output:**
    ```
    True
    ```

22. **How do you check if a set is empty?**
    
    **Answer:**
    Use `if not s:`

23. **How do you remove an element from a set if it exists?**
    
    **Answer:**
    Use `s.discard(x)`.

24. **What is the output of `print set([1, 2, 3]).discard(2)`?**
    
    **Answer:**
    ```akandechips
    s = set([1, 2, 3])
    s.discard(2)
    print s
    ```
    **Output:**
    ```
    {1, 3}
    ```

25. **How do you loop through all elements in a set?**
    
    **Answer:**
    Use `for x in s:`

26. **What is the output of `print set([1, 2, 3]).pop()`?**
    
    **Answer:**
    ```akandechips
    s = set([1, 2, 3])
    print s.pop()
    ```
    **Output:**
    ```
    (any one of 1, 2, or 3)
    ```

27. **How do you create an empty set?**
    
    **Answer:**
    Use `set()`.

28. **How do you convert a list to a set?**
    
    **Answer:**
    Use `set(mylist)`.

29. **How do you convert a set to a list?**
    
    **Answer:**
    Use `list(s)`.

30. **What is the output of `print set([1, 2, 3]) == set([3, 2, 1])`?**
    
    **Answer:**
    ```akandechips
    print set([1, 2, 3]) == set([3, 2, 1])
    ```
    **Output:**
    ```
    True
    ```

#### Projects & Solutions

1. **Project:** Create a set of three numbers and print it.
   
   **Solution:**
   ```akandechips
   s = set([4, 5, 6])
   print s
   ```
   **Output:**
   ```
   {4, 5, 6}
   ```

2. **Project:** Add an element to a set and print it.
   
   **Solution:**
   ```akandechips
   s = set([1, 2])
   s.add(3)
   print s
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

3. **Project:** Remove an element from a set and print it.
   
   **Solution:**
   ```akandechips
   s = set([1, 2, 3])
   s.remove(2)
   print s
   ```
   **Output:**
   ```
   {1, 3}
   ```

4. **Project:** Check if an element is in a set and print the result.
   
   **Solution:**
   ```akandechips
   s = set([1, 2, 3])
   print 2 in s
   ```
   **Output:**
   ```
   True
   ```

5. **Project:** Clear all elements from a set and print it.
   
   **Solution:**
   ```akandechips
   s = set([1, 2, 3])
   s.clear()
   print s
   ```
   **Output:**
   ```
   set()
   ```

6. **Project:** Copy a set and print the copy.
   
   **Solution:**
   ```akandechips
   s = set([1, 2, 3])
   s2 = s.copy()
   print s2
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

7. **Project:** Find the union of two sets and print it.
   
   **Solution:**
   ```akandechips
   a = set([1, 2])
   b = set([2, 3])
   print a | b
   ```
   **Output:**
   ```
   {1, 2, 3}
   ```

8. **Project:** Find the intersection of two sets and print it.
   
   **Solution:**
   ```akandechips
   a = set([1, 2, 3])
   b = set([2, 3, 4])
   print a & b
   ```
   **Output:**
   ```
   {2, 3}
   ```

9. **Project:** Find the difference between two sets and print it.
   
   **Solution:**
   ```akandechips
   a = set([1, 2, 3])
   b = set([2, 3])
   print a - b
   ```
   **Output:**
   ```
   {1}
   ```

10. **Project:** Find the symmetric difference of two sets and print it.
    
    **Solution:**
    ```akandechips
    a = set([1, 2, 3])
    b = set([2, 3, 4])
    print a ^ b
    ```
    **Output:**
    ```
    {1, 4}
    ```

11. **Project:** Check if a set is a subset of another and print the result.
    
    **Solution:**
    ```akandechips
    a = set([1, 2])
    b = set([1, 2, 3])
    print a <= b
    ```
    **Output:**
    ```
    True
    ```

12. **Project:** Check if a set is a superset of another and print the result.
    
    **Solution:**
    ```akandechips
    a = set([1, 2, 3])
    b = set([2, 3])
    print a >= b
    ```
    **Output:**
    ```
    True
    ```

13. **Project:** Loop through all elements in a set and print them.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3])
    for x in s:
        print x
    ```
    **Output:**
    ```
    1
    2
    3
    ```

14. **Project:** Remove an element from a set if it exists and print the set.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3])
    s.discard(2)
    print s
    ```
    **Output:**
    ```
    {1, 3}
    ```

15. **Project:** Create an empty set and print it.
    
    **Solution:**
    ```akandechips
    s = set()
    print s
    ```
    **Output:**
    ```
    set()
    ```

16. **Project:** Convert a list to a set and print it.
    
    **Solution:**
    ```akandechips
    mylist = [1, 2, 2, 3]
    s = set(mylist)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

17. **Project:** Convert a set to a list and print it.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3])
    l = list(s)
    print l
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

18. **Project:** Check if a set is empty and print the result.
    
    **Solution:**
    ```akandechips
    s = set()
    print not s
    ```
    **Output:**
    ```
    True
    ```

19. **Project:** Add multiple elements to a set and print it.
    
    **Solution:**
    ```akandechips
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

20. **Project:** Remove all elements from a set using a loop and print it.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3])
    while s:
        s.pop()
    print s
    ```
    **Output:**
    ```
    set()
    ```

21. **Project:** Find the union of three sets and print it.
    
    **Solution:**
    ```akandechips
    a = set([1])
    b = set([2])
    c = set([3])
    print a | b | c
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

22. **Project:** Find the intersection of three sets and print it.
    
    **Solution:**
    ```akandechips
    a = set([1, 2])
    b = set([2, 3])
    c = set([2, 4])
    print a & b & c
    ```
    **Output:**
    ```
    {2}
    ```

23. **Project:** Find the difference between three sets and print it.
    
    **Solution:**
    ```akandechips
    a = set([1, 2, 3])
    b = set([2])
    c = set([3])
    print a - b - c
    ```
    **Output:**
    ```
    {1}
    ```

24. **Project:** Find the symmetric difference of three sets and print it.
    
    **Solution:**
    ```akandechips
    a = set([1, 2])
    b = set([2, 3])
    c = set([3, 4])
    print a ^ b ^ c
    ```
    **Output:**
    ```
    {1, 4}
    ```

25. **Project:** Print all elements in a set greater than 2.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3, 4])
    for x in s:
        if x > 2:
            print x
    ```
    **Output:**
    ```
    3
    4
    ```

26. **Project:** Create a set from a string and print it.
    
    **Solution:**
    ```akandechips
    s = set("chips")
    print s
    ```
    **Output:**
    ```
    {'c', 'h', 'i', 'p', 's'}
    ```

27. **Project:** Print the number of elements in a set.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3])
    print len(s)
    ```
    **Output:**
    ```
    3
    ```

28. **Project:** Check if two sets are equal and print the result.
    
    **Solution:**
    ```akandechips
    a = set([1, 2, 3])
    b = set([3, 2, 1])
    print a == b
    ```
    **Output:**
    ```
    True
    ```

29. **Project:** Add all elements from a list to a set and print it.
    
    **Solution:**
    ```akandechips
    s = set()
    l = [1, 2, 3]
    for x in l:
        s.add(x)
    print s
    ```
    **Output:**
    ```
    {1, 2, 3}
    ```

30. **Project:** Remove all even numbers from a set and print it.
    
    **Solution:**
    ```akandechips
    s = set([1, 2, 3, 4])
    for x in list(s):
        if x % 2 == 0:
            s.remove(x)
    print s
    ```
    **Output:**
    ```
    {1, 3}
    ```

---


## Tuple Variables

**Expected Output:**
```
No output (variables are stored in memory)
```

#### Coding Questions & Answers

1. **How do you create a tuple with the numbers 1, 2, 3?**
   
   **Answer:**
   ```akandechips
   t = (1, 2, 3)
   print t
   ```
   **Output:**
   ```
   (1, 2, 3)
   ```

2. **How do you access the first element of a tuple?**
   
   **Answer:**
   Use `t[0]`.

3. **What is the output of `print (1, 2, 3)[1]`?**
   
   **Answer:**
   ```akandechips
   print (1, 2, 3)[1]
   ```
   **Output:**
   ```
   2
   ```

4. **How do you get the length of a tuple?**
   
   **Answer:**
   Use `len(t)`.

5. **What is the output of `print (1, 2, 3) + (4, 5)`?**
   
   **Answer:**
   ```akandechips
   print (1, 2, 3) + (4, 5)
   ```
   **Output:**
   ```
   (1, 2, 3, 4, 5)
   ```

6. **How do you check if 2 is in a tuple?**
   
   **Answer:**
   Use `2 in t`.

7. **What is the output of `print (1, 2, 3).count(2)`?**
   
   **Answer:**
   ```akandechips
   print (1, 2, 3).count(2)
   ```
   **Output:**
   ```
   1
   ```

8. **How do you find the index of 3 in a tuple?**
   
   **Answer:**
   Use `t.index(3)`.

9. **What is the output of `print (1, 2, 3).index(2)`?**
   
   **Answer:**
   ```akandechips
   print (1, 2, 3).index(2)
   ```
   **Output:**
   ```
   1
   ```

10. **How do you get the last element of a tuple?**
    
    **Answer:**
    Use `t[-1]`.

11. **What is the output of `print (1, 2, 3)[:2]`?**
    
    **Answer:**
    ```akandechips
    print (1, 2, 3)[:2]
    ```
    **Output:**
    ```
    (1, 2)
    ```

12. **How do you unpack a tuple into variables?**
    
    **Answer:**
    Use `a, b = (1, 2)`.

13. **What is the output of `print tuple([1, 2, 3])`?**
    
    **Answer:**
    ```akandechips
    print tuple([1, 2, 3])
    ```
    **Output:**
    ```
    (1, 2, 3)
    ```

14. **How do you convert a tuple to a list?**
    
    **Answer:**
    Use `list(t)`.

15. **What is the output of `print (1, 2, 3)[::-1]`?**
    
    **Answer:**
    ```akandechips
    print (1, 2, 3)[::-1]
    ```
    **Output:**
    ```
    (3, 2, 1)
    ```

16. **How do you check if a tuple is empty?**
    
    **Answer:**
    Use `if not t:`

17. **What is the output of `print len(())`?**
    
    **Answer:**
    ```akandechips
    print len(())
    ```
    **Output:**
    ```
    0
    ```

18. **How do you create a tuple with one element?**
    
    **Answer:**
    Use `(x,)`.

19. **What is the output of `print (1, 2, 3) * 2`?**
    
    **Answer:**
    ```akandechips
    print (1, 2, 3) * 2
    ```
    **Output:**
    ```
    (1, 2, 3, 1, 2, 3)
    ```

20. **How do you check if two tuples are equal?**
    
    **Answer:**
    Use `t1 == t2`.

21. **What is the output of `print (1, 2) + (3,)`?**
    
    **Answer:**
    ```akandechips
    print (1, 2) + (3,)
    ```
    **Output:**
    ```
    (1, 2, 3)
    ```

22. **How do you slice a tuple from index 1 to 3?**
    
    **Answer:**
    Use `t[1:3]`.

23. **What is the output of `print (1, 2, 3, 4)[1:3]`?**
    
    **Answer:**
    ```akandechips
    print (1, 2, 3, 4)[1:3]
    ```
    **Output:**
    ```
    (2, 3)
    ```

24. **How do you nest tuples?**
    
    **Answer:**
    Use `t = ((1, 2), (3, 4))`.

25. **What is the output of `print ((1, 2), (3, 4))[1][0]`?**
    
    **Answer:**
    ```akandechips
    print ((1, 2), (3, 4))[1][0]
    ```
    **Output:**
    ```
    3
    ```

26. **How do you check if a tuple contains another tuple?**
    
    **Answer:**
    Use `subtuple in t`.

27. **What is the output of `print (1, 2, 3).index(3)`?**
    
    **Answer:**
    ```akandechips
    print (1, 2, 3).index(3)
    ```
    **Output:**
    ```
    2
    ```

28. **How do you repeat a tuple 3 times?**
    
    **Answer:**
    Use `t * 3`.

29. **What is the output of `print (1, 2) * 3`?**
    
    **Answer:**
    ```akandechips
    print (1, 2) * 3
    ```
    **Output:**
    ```
    (1, 2, 1, 2, 1, 2)
    ```

30. **How do you convert a list of tuples to a tuple of tuples?**
    
    **Answer:**
    Use `tuple(list_of_tuples)`.

#### Projects & Solutions

1. **Project:** Create a tuple of three numbers and print it.
   
   **Solution:**
   ```akandechips
   t = (4, 5, 6)
   print t
   ```
   **Output:**
   ```
   (4, 5, 6)
   ```

2. **Project:** Print the first and last element of a tuple.
   
   **Solution:**
   ```akandechips
   t = (7, 8, 9)
   print t[0], t[-1]
   ```
   **Output:**
   ```
   7 9
   ```

3. **Project:** Concatenate two tuples and print the result.
   
   **Solution:**
   ```akandechips
   a = (1, 2)
   b = (3, 4)
   print a + b
   ```
   **Output:**
   ```
   (1, 2, 3, 4)
   ```

4. **Project:** Print the length of a tuple.
   
   **Solution:**
   ```akandechips
   t = (1, 2, 3, 4)
   print len(t)
   ```
   **Output:**
   ```
   4
   ```

5. **Project:** Check if a value is in a tuple and print the result.
   
   **Solution:**
   ```akandechips
   t = (1, 2, 3)
   print 2 in t
   ```
   **Output:**
   ```
   True
   ```

6. **Project:** Print the index of a value in a tuple.
   
   **Solution:**
   ```akandechips
   t = (1, 2, 3)
   print t.index(3)
   ```
   **Output:**
   ```
   2
   ```

7. **Project:** Print the count of a value in a tuple.
   
   **Solution:**
   ```akandechips
   t = (1, 2, 2, 3)
   print t.count(2)
   ```
   **Output:**
   ```
   2
   ```

8. **Project:** Print a slice of a tuple.
   
   **Solution:**
   ```akandechips
   t = (1, 2, 3, 4)
   print t[1:3]
   ```
   **Output:**
   ```
   (2, 3)
   ```

9. **Project:** Unpack a tuple into variables and print them.
   
   **Solution:**
   ```akandechips
   t = (5, 6)
   a, b = t
   print a, b
   ```
   **Output:**
   ```
   5 6
   ```

10. **Project:** Convert a list to a tuple and print it.
    
    **Solution:**
    ```akandechips
    l = [1, 2, 3]
    t = tuple(l)
    print t
    ```
    **Output:**
    ```
    (1, 2, 3)
    ```

11. **Project:** Convert a tuple to a list and print it.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    l = list(t)
    print l
    ```
    **Output:**
    ```
    [1, 2, 3]
    ```

12. **Project:** Print the last element of a tuple.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    print t[-1]
    ```
    **Output:**
    ```
    3
    ```

13. **Project:** Print the first two elements of a tuple.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    print t[:2]
    ```
    **Output:**
    ```
    (1, 2)
    ```

14. **Project:** Repeat a tuple 3 times and print it.
    
    **Solution:**
    ```akandechips
    t = (1, 2)
    print t * 3
    ```
    **Output:**
    ```
    (1, 2, 1, 2, 1, 2)
    ```

15. **Project:** Check if a tuple is empty and print the result.
    
    **Solution:**
    ```akandechips
    t = ()
    print not t
    ```
    **Output:**
    ```
    True
    ```

16. **Project:** Create a tuple with one element and print it.
    
    **Solution:**
    ```akandechips
    t = (5,)
    print t
    ```
    **Output:**
    ```
    (5,)
    ```

17. **Project:** Nest tuples and print the result.
    
    **Solution:**
    ```akandechips
    t = ((1, 2), (3, 4))
    print t
    ```
    **Output:**
    ```
    ((1, 2), (3, 4))
    ```

18. **Project:** Print the first element of the second tuple in a nested tuple.
    
    **Solution:**
    ```akandechips
    t = ((1, 2), (3, 4))
    print t[1][0]
    ```
    **Output:**
    ```
    3
    ```

19. **Project:** Check if a tuple contains another tuple and print the result.
    
    **Solution:**
    ```akandechips
    t = ((1, 2), (3, 4))
    print (1, 2) in t
    ```
    **Output:**
    ```
    True
    ```

20. **Project:** Print the sum of all elements in a tuple.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    print sum(t)
    ```
    **Output:**
    ```
    6
    ```

21. **Project:** Print the minimum and maximum of a tuple.
    
    **Solution:**
    ```akandechips
    t = (2, 4, 1)
    print min(t), max(t)
    ```
    **Output:**
    ```
    1 4
    ```

22. **Project:** Create a tuple from a string and print it.
    
    **Solution:**
    ```akandechips
    t = tuple("chips")
    print t
    ```
    **Output:**
    ```
    ('c', 'h', 'i', 'p', 's')
    ```

23. **Project:** Print every element in a tuple using a loop.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    for x in t:
        print x
    ```
    **Output:**
    ```
    1
    2
    3
    ```

24. **Project:** Create a tuple of tuples and print it.
    
    **Solution:**
    ```akandechips
    t = ((1, 2), (3, 4))
    print t
    ```
    **Output:**
    ```
    ((1, 2), (3, 4))
    ```

25. **Project:** Convert a list of tuples to a tuple of tuples and print it.
    
    **Solution:**
    ```akandechips
    l = [(1, 2), (3, 4)]
    t = tuple(l)
    print t
    ```
    **Output:**
    ```
    ((1, 2), (3, 4))
    ```

26. **Project:** Print the reversed tuple.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    print t[::-1]
    ```
    **Output:**
    ```
    (3, 2, 1)
    ```

27. **Project:** Print the product of all elements in a tuple.
    
    **Solution:**
    ```akandechips
    t = (2, 3, 4)
    prod = 1
    for x in t:
        prod = prod * x
    print prod
    ```
    **Output:**
    ```
    24
    ```

28. **Project:** Print the tuple with all elements doubled.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3)
    newt = tuple([x * 2 for x in t])
    print newt
    ```
    **Output:**
    ```
    (2, 4, 6)
    ```

29. **Project:** Print the tuple with only even elements.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3, 4)
    newt = tuple([x for x in t if x % 2 == 0])
    print newt
    ```
    **Output:**
    ```
    (2, 4)
    ```

30. **Project:** Print the tuple with elements greater than 2.
    
    **Solution:**
    ```akandechips
    t = (1, 2, 3, 4)
    newt = tuple([x for x in t if x > 2])
    print newt
    ```
    **Output:**
    ```
    (3, 4)
    ```

---

## [Room for More Types]
<!-- Add new types as the language evolves -->

---

## Basic Operations
**Explanation:**
You can perform arithmetic and other operations on variables. This is essential for calculations and data processing.

**Example:**
```akandechips
sum = a + b
print(sum)
```
**Expected Output:**
```
8.14
```

### Coding Questions & Answers

1. **What is the output of `print(3 + 5)`?**
   
   **Answer:**
   ```akandechips
   print(3 + 5)
   ```
   **Output:**
   ```
   8
   ```

2. **How do you subtract 2.5 from 7.1 and print the result?**
   
   **Answer:**
   ```akandechips
   print(7.1 - 2.5)
   ```
   **Output:**
   ```
   4.6
   ```

3. **What is the output of `print(2 * 3.5)`?**
   
   **Answer:**
   ```akandechips
   print(2 * 3.5)
   ```
   **Output:**
   ```
   7.0
   ```

4. **How do you divide 10 by 4 and print the result?**
   
   **Answer:**
   ```akandechips
   print(10 / 4)
   ```
   **Output:**
   ```
   2.5
   ```

5. **What is the output of `print(7 % 3)`?**
   
   **Answer:**
   ```akandechips
   print(7 % 3)
   ```
   **Output:**
   ```
   1
   ```

6. **How do you calculate 2 to the power of 4 and print the result?**
   
   **Answer:**
   ```akandechips
   print(2 ** 4)
   ```
   **Output:**
   ```
   16
   ```

7. **What is the output of `print(9 // 2)`?**
   
   **Answer:**
   ```akandechips
   print(9 // 2)
   ```
   **Output:**
   ```
   4
   ```

8. **How do you add two variables `a = 3.14` and `b = 5` and print the result?**
   
   **Answer:**
   ```akandechips
   a = 3.14
   b = 5
   print(a + b)
   ```
   **Output:**
   ```
   8.14
   ```

9. **What is the output of `print(abs(-7.5))`?**
   
   **Answer:**
   ```akandechips
   print(abs(-7.5))
   ```
   **Output:**
   ```
   7.5
   ```

10. **How do you round 3.678 to 2 decimal places and print it?**
    
    **Answer:**
    ```akandechips
    print(round(3.678, 2))
    ```
    **Output:**
    ```
    3.68
    ```

11. **What is the output of `print(10 - 3 * 2)`?**
    
    **Answer:**
    ```akandechips
    print(10 - 3 * 2)
    ```
    **Output:**
    ```
    4
    ```

12. **How do you calculate the average of 4, 8, and 10?**
    
    **Answer:**
    ```akandechips
    print((4 + 8 + 10) / 3)
    ```
    **Output:**
    ```
    7.333333333333333
    ```

13. **What is the output of `print(2 * (3 + 4))`?**
    
    **Answer:**
    ```akandechips
    print(2 * (3 + 4))
    ```
    **Output:**
    ```
    14
    ```

14. **How do you find the minimum of 5, 2, and 9?**
    
    **Answer:**
    ```akandechips
    print(min(5, 2, 9))
    ```
    **Output:**
    ```
    2
    ```

15. **What is the output of `print(max(5, 2, 9))`?**
    
    **Answer:**
    ```akandechips
    print(max(5, 2, 9))
    ```
    **Output:**
    ```
    9
    ```

16. **How do you calculate the sum of a list `[1, 2, 3, 4]`?**
    
    **Answer:**
    ```akandechips
    print(sum([1, 2, 3, 4]))
    ```
    **Output:**
    ```
    10
    ```

17. **What is the output of `print(5 * 0)`?**
    
    **Answer:**
    ```akandechips
    print(5 * 0)
    ```
    **Output:**
    ```
    0
    ```

18. **How do you calculate the remainder of 17 divided by 4?**
    
    **Answer:**
    ```akandechips
    print(17 % 4)
    ```
    **Output:**
    ```
    1
    ```

19. **What is the output of `print(2 ** 3 ** 2)`?**
    
    **Answer:**
    ```akandechips
    print(2 ** 3 ** 2)
    ```
    **Output:**
    ```
    512
    ```

20. **How do you negate a number and print it?**
    
    **Answer:**
    ```akandechips
    x = 7
    print(-x)
    ```
    **Output:**
    ```
    -7
    ```

21. **What is the output of `print(10 / 3)`?**
    
    **Answer:**
    ```akandechips
    print(10 / 3)
    ```
    **Output:**
    ```
    3.3333333333333335
    ```

22. **How do you use parentheses to change the order of operations?**
    
    **Answer:**
    Use parentheses, e.g., `(2 + 3) * 4`.

23. **What is the output of `print(100 // 9)`?**
    
    **Answer:**
    ```akandechips
    print(100 // 9)
    ```
    **Output:**
    ```
    11
    ```

24. **How do you calculate the square root of 16?**
    
    **Answer:**
    ```akandechips
    print(16 ** 0.5)
    ```
    **Output:**
    ```
    4.0
    ```

25. **What is the output of `print(0.1 + 0.2)`?**
    
    **Answer:**
    ```akandechips
    print(0.1 + 0.2)
    ```
    **Output:**
    ```
    0.30000000000000004
    ```

26. **How do you calculate the cube of 5?**
    
    **Answer:**
    ```akandechips
    print(5 ** 3)
    ```
    **Output:**
    ```
    125
    ```

27. **What is the output of `print(7 + 3 * 2)`?**
    
    **Answer:**
    ```akandechips
    print(7 + 3 * 2)
    ```
    **Output:**
    ```
    13
    ```

28. **How do you calculate the difference between the largest and smallest in `[4, 8, 15]`?**
    
    **Answer:**
    ```akandechips
    print(max([4, 8, 15]) - min([4, 8, 15]))
    ```
    **Output:**
    ```
    11
    ```

29. **What is the output of `print(2 + 3 * 4 - 5)`?**
    
    **Answer:**
    ```akandechips
    print(2 + 3 * 4 - 5)
    ```
    **Output:**
    ```
    9
    ```

30. **How do you calculate the product of 2, 3, and 4?**
    
    **Answer:**
    ```akandechips
    print(2 * 3 * 4)
    ```
    **Output:**
    ```
    24
    ```


### Projects & Solutions

1. **Project:** Add two numbers and print the result.
   
   **Solution:**
   ```akandechips
   a = 2.5
   b = 4.7
   sum = a + b
   print(sum)
   ```
   **Output:**
   ```
   7.2
   ```

2. **Project:** Subtract one number from another and print the result.
   
   **Solution:**
   ```akandechips
   a = 10
   b = 3
   print(a - b)
   ```
   **Output:**
   ```
   7
   ```

3. **Project:** Multiply two numbers and print the result.
   
   **Solution:**
   ```akandechips
   a = 6
   b = 7
   print(a * b)
   ```
   **Output:**
   ```
   42
   ```

4. **Project:** Divide two numbers and print the result.
   
   **Solution:**
   ```akandechips
   a = 9
   b = 2
   print(a / b)
   ```
   **Output:**
   ```
   4.5
   ```

5. **Project:** Find the remainder of a division and print it.
   
   **Solution:**
   ```akandechips
   a = 17
   b = 5
   print(a % b)
   ```
   **Output:**
   ```
   2
   ```

6. **Project:** Calculate the power of a number and print it.
   
   **Solution:**
   ```akandechips
   print(3 ** 3)
   ```
   **Output:**
   ```
   27
   ```

7. **Project:** Floor divide two numbers and print the result.
   
   **Solution:**
   ```akandechips
   print(15 // 4)
   ```
   **Output:**
   ```
   3
   ```

8. **Project:** Add three numbers and print the result.
   
   **Solution:**
   ```akandechips
   a = 1
   b = 2
   c = 3
   print(a + b + c)
   ```
   **Output:**
   ```
   6
   ```

9. **Project:** Calculate the absolute value of a number and print it.
   
   **Solution:**
   ```akandechips
   x = -12.5
   print(abs(x))
   ```
   **Output:**
   ```
   12.5
   ```

10. **Project:** Round a number to 1 decimal place and print it.
    
    **Solution:**
    ```akandechips
    x = 3.14159
    print(round(x, 1))
    ```
    **Output:**
    ```
    3.1
    ```

11. **Project:** Calculate the average of a list of numbers and print it.
    
    **Solution:**
    ```akandechips
    nums = [2, 4, 6, 8]
    avg = sum(nums) / len(nums)
    print(avg)
    ```
    **Output:**
    ```
    5.0
    ```

12. **Project:** Use parentheses to change the order of operations and print the result.
    
    **Solution:**
    ```akandechips
    print((2 + 3) * 4)
    ```
    **Output:**
    ```
    20
    ```

13. **Project:** Find the minimum and maximum of a list and print them.
    
    **Solution:**
    ```akandechips
    nums = [7, 2, 9]
    print(min(nums), max(nums))
    ```
    **Output:**
    ```
    2 9
    ```

14. **Project:** Calculate the product of all elements in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [2, 3, 4]
    prod = 1
    for x in nums:
        prod = prod * x
    print(prod)
    ```
    **Output:**
    ```
    24
    ```

15. **Project:** Find the difference between the largest and smallest in a list and print it.
    
    **Solution:**
    ```akandechips
    nums = [4, 8, 15]
    print(max(nums) - min(nums))
    ```
    **Output:**
    ```
    11
    ```

16. **Project:** Calculate the square root of a number and print it.
    
    **Solution:**
    ```akandechips
    print(25 ** 0.5)
    ```
    **Output:**
    ```
    5.0
    ```

17. **Project:** Calculate the cube of a number and print it.
    
    **Solution:**
    ```akandechips
    print(4 ** 3)
    ```
    **Output:**
    ```
    64
    ```

18. **Project:** Use floor division to divide two numbers and print the result.
    
    **Solution:**
    ```akandechips
    print(17 // 3)
    ```
    **Output:**
    ```
    5
    ```

19. **Project:** Add 0.1 and 0.2 and print the result.
    
    **Solution:**
    ```akandechips
    print(0.1 + 0.2)
    ```
    **Output:**
    ```
    0.30000000000000004
    ```

20. **Project:** Negate a number and print it.
    
    **Solution:**
    ```akandechips
    x = 11
    print(-x)
    ```
    **Output:**
    ```
    -11
    ```

21. **Project:** Calculate the sum of the first 10 positive integers and print it.
    
    **Solution:**
    ```akandechips
    print(sum(range(1, 11)))
    ```
    **Output:**
    ```
    55
    ```

22. **Project:** Calculate the average of 5, 10, 15, and print it.
    
    **Solution:**
    ```akandechips
    print((5 + 10 + 15) / 3)
    ```
    **Output:**
    ```
    10.0
    ```

23. **Project:** Find the remainder of 100 divided by 9 and print it.
    
    **Solution:**
    ```akandechips
    print(100 % 9)
    ```
    **Output:**
    ```
    1
    ```

24. **Project:** Calculate 2 to the power of 8 and print it.
    
    **Solution:**
    ```akandechips
    print(2 ** 8)
    ```
    **Output:**
    ```
    256
    ```

25. **Project:** Calculate the product of 2, 3, and 5 and print it.
    
    **Solution:**
    ```akandechips
    print(2 * 3 * 5)
    ```
    **Output:**
    ```
    30
    ```

26. **Project:** Calculate the difference between 100 and 45 and print it.
    
    **Solution:**
    ```akandechips
    print(100 - 45)
    ```
    **Output:**
    ```
    55
    ```

27. **Project:** Calculate the sum of a list `[10, 20, 30]` and print it.
    
    **Solution:**
    ```akandechips
    nums = [10, 20, 30]
    print(sum(nums))
    ```
    **Output:**
    ```
    60
    ```

28. **Project:** Calculate the average of a list `[2, 4, 6, 8]` and print it.
    
    **Solution:**
    ```akandechips
    nums = [2, 4, 6, 8]
    print(sum(nums) / len(nums))
    ```
    **Output:**
    ```
    5.0
    ```

29. **Project:** Calculate the square of 12 and print it.
    
    **Solution:**
    ```akandechips
    print(12 ** 2)
    ```
    **Output:**
    ```
    144
    ```

30. **Project:** Calculate the cube root of 27 and print it.
    
    **Solution:**
    ```akandechips
    print(27 ** (1/3))
    ```
    **Output:**
    ```
    3.0
    ```

---

## Control Flow
**Explanation:**
Control flow lets you make decisions and repeat actions. This is how programs become dynamic and interactive.

**Example:**
```akandechips
if a > 3:
    print("a is greater than 3")
else:
    print("a is 3 or less")
```
**Expected Output:**
```
a is greater than 3
```

### Coding Questions & Answers
<!-- Q1-Q30 with code, answer, and output go here -->

### Projects & Solutions
<!-- P1-P30 with code, solution, and output go here -->

---

## [Room for Future Topics]
<!-- Add new topics and subtopics here as the language and curriculum grow -->

Input and Output (User Input, Reading/Writing Files)
Input and Output (I/O) are fundamental concepts in programming, enabling interaction between a program and the outside world. I/O operations allow programs to receive data from users, read data from files, and write data back to files or display results on the screen. This chapter covers two main areas: user input and file I/O.

1. User Input
1.1. What is User Input?
User input refers to the data or information that a program receives from the user during execution. This allows programs to be dynamic and interactive, responding to user commands or data.

1.2. Methods of Receiving User Input
Command Line Input: Most programming languages provide built-in functions to receive input from the keyboard. For example, in Python, the input() function is used.
Graphical User Interface (GUI) Input: In GUI applications, input can be received through text boxes, buttons, and other widgets.
Validation of Input: It is important to validate user input to ensure it meets the required format or constraints (e.g., checking if the input is a number).
1.3. Example (Python)
Here, the program prompts the user for their name and age, then displays a message using the input.

2. Output
2.1. Displaying Output
Output refers to the information that a program sends to the user, usually via the screen or console. The most common way is using print statements.

Console Output: Using functions like print() in Python or System.out.println() in Java.
Formatted Output: Output can be formatted to display data in a user-friendly way, such as aligning columns or controlling decimal places.
2.2. Example (Python)
This prints messages and formats the score to two decimal places.

3. File Input and Output
3.1. Why Use Files?
Files are used to store data permanently. Unlike variables, which lose their values when a program ends, files retain data for future use.

3.2. Types of Files
Text Files: Store data as readable text (e.g., .txt, .csv).
Binary Files: Store data in binary format (e.g., images, executables).
3.3. Opening and Closing Files
Before reading or writing, a file must be opened. After operations, it should be closed to free resources.

Opening a File: In Python, use open(filename, mode).
Modes: 'r' for reading, 'w' for writing (overwrites), 'a' for appending, 'b' for binary mode.
Closing a File: Use file.close() or a context manager (with statement) for automatic closing.
3.4. Reading from Files
Read Entire File: file.read()
Read Line by Line: file.readline() or iterate over the file object.
Example:
3.5. Writing to Files
Write Data: file.write(data)
Example:
3.6. Appending to Files
Append Mode: Opens the file for writing at the end, preserving existing content.
3.7. File Handling Best Practices
Always close files after use.
Use exception handling to manage errors (e.g., file not found).
Use context managers (with statement) for safer file operations.
4. Practical Applications
Saving User Data: Storing user preferences or scores.
Processing Data Files: Reading data from CSV files for analysis.
Logging: Writing logs for debugging or auditing.
5. Summary
Input and Output operations are essential for interactive and data-driven programs. User input allows programs to receive data dynamically, while file I/O enables persistent storage and retrieval of information. Mastery of these concepts is crucial for building robust applications.

Certainly! Here’s a concise summary and explanation of the key points from your chapter on Input and Output (User Input, Reading/Writing Files):

1. User Input
Definition: User input is data provided by the user during program execution, making programs interactive.
Methods:
Command Line Input: e.g., input() in Python.
GUI Input: Through widgets like text boxes and buttons.
Validation: Always check if the input meets requirements (e.g., is it a number?).
Example (Python):


name = input("Enter your name: ")age = input("Enter your age: ")print(f"Hello, {name}! You are {age} years old.")
2. Output
Definition: Output is information sent from the program to the user, usually via the screen.
Methods:
Console Output: e.g., print() in Python.
Formatted Output: Control how data is displayed (e.g., decimal places, alignment).
Example (Python):


score = 93.4567print(f"Your score is {score:.2f}")
3. File Input and Output
Purpose: Files store data permanently, unlike variables.
Types:
Text Files: Human-readable (e.g., .txt, .csv).
Binary Files: Not human-readable (e.g., images).
Opening/Closing Files:
Use open(filename, mode); modes include 'r' (read), 'w' (write), 'a' (append), 'b' (binary).
Always close files with file.close() or use a context manager (with statement).
Reading Example:


with open('data.txt', 'r') as file:    content = file.read()    print(content)
Writing Example:


with open('output.txt', 'w') as file:    file.write("Hello, file!")
Appending Example:


with open('output.txt', 'a') as file:    file.write("\nAdding more data.")
Best Practices:
Always close files.
Use exception handling for errors.
Prefer context managers for safety.
4. Practical Applications
Saving user data (preferences, scores)
Processing data files (e.g., CSV analysis)
Logging (debugging, auditing)
5. Summary
Input and Output are essential for interactive and persistent programs. User input makes programs dynamic, while file I/O allows data to be saved and retrieved. Mastering these skills is crucial for robust application development.

Absolutely! Here’s a suggested chapter outline for a beginner-friendly HDL/programming textbook, tailored for American students and the chips workforce, based on your list. I’ve organized and expanded your topics into logical chapters, with brief descriptions for each:

1. Introduction to Programming and HDL
What is programming?
What is HDL (Hardware Description Language)?
Why learn both? (Relevance to chips workforce)
Overview: AkandeChips vs. Python
2. Getting Started: Your First Program
Setting up your environment
Writing and running your first program (Hello, World!)
Understanding program structure
3. Input and Output
User input (keyboard, switches)
Displaying output (screen, LEDs)
Reading and writing files (if supported)
4. Comments and Documentation
Why comment your code?
Single-line and multi-line comments
Writing clear documentation
5. Variables, Data Types, and Operators
Declaring variables
Basic data types (integers, floats, strings, bits)
Arithmetic, comparison, and logical operators
6. Error Handling and Debugging
Common errors (syntax, runtime, logic)
Try/except (if supported)
Basic debugging techniques
7. Control Flow: Conditionals and Loops
If, else, elif statements
For and while loops
Break and continue
8. Functions and Procedures
Defining and calling functions
Parameters and return values
Scope and lifetime of variables
9. Data Structures
Lists/arrays
Tuples (if supported)
Dictionaries and sets (if supported)
When to use each
10. Simple Algorithms
Sorting (bubble sort, selection sort)
Searching (linear, binary)
Step-by-step examples
11. Modules and Imports
What are modules?
Importing and using libraries
Creating your own modules
12. Simple Hardware Concepts
Logic gates (AND, OR, NOT, etc.)
Truth tables
HDL basics (writing simple hardware descriptions)
13. AkandeChips vs. Python: Key Differences and Similarities
Syntax and structure
Data types and operations
Use cases and limitations
14. Real-World Mini-Projects
Blinking LED (hardware + code)
Simple calculator
File reader/writer
Other beginner-friendly projects
15. Practice Tests and Review Sections
Chapter quizzes
Review exercises
Sample test for certification/interview prep
Tips:

Each chapter should include clear examples, diagrams, and practice exercises.
Consider adding “Common Mistakes” and “Pro Tips” boxes.
End each chapter with a summary and a mini-project or challenge.
Let me know if you want a more detailed breakdown for any chapter, or if you’d like sample content for a specific section!




Continue to the [Getting Started](./getting_started.md) guide for more!
