# Python notes on Leetcode problems

## Array/String

### 169 Majority Element
  
    ```py
    from collections import defaultdict
    d = defaultdict(int) # the input should be one datatype
    d1 = defaultdict(list) # [] by default
    ```

### 189 Rotate Array

- slices can be assigned, temps are not needed
  
    ```py
    nums[:k], nums[k:] = nums[-k:], nums[:-k]
    ```

- define a function inside a function, all parameters in the parent function are available to children, swapping does not need temp in python

    ```py
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        def reverse(left:int, right:int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
    ```

### 121 Best Time to Buy and Sell Stock

- use `and` `or` for logical comparison, `&` is only a bitwise operator
- `half = len(l) // 2`

### 55

- Initialize list with list comprehension
  `reach = [0 for x in range(len(nums))]`
- can omit `else:`

    ```py
    for num in nums:
        if max_steps < 0:
            return False
        elif max_steps < num:
            max_steps = num
        max_steps -= 1
    ```

- use enumerate for lists
  `for i, num in enumerate(nums):`
  When using `range(len(nums))`, you manually index into the list, which is less efficient and can be harder to read.
  While the performance gain is usually small for small datasets, using enumerate avoids the extra call to `len(nums)` and indexing into the list for each iteration.

- save variables to avoid repetative computation
  `len_nums = len(nums)`

### 274 H-Index

- in-place list methods (l.method()) and non-in-place list methods (method(l))
  In-Place List Methods
  Their return type is None, so l.method() is not iterable and cannot be returned

  ```py
  my_list.append(5)

  # extend(iterable): Adds all elements from the iterable to the end of the list.
  my_list.extend([6, 7])

  # insert(index, item): Inserts an item at a specified position.
  my_list.insert(2, 10)
  
  # remove(item): Removes the first occurrence of an item from the list.
  my_list.remove(3)
  
  # pop([index]): Removes and returns the item at the given index (last item if index is not specified).
  my_list.pop(1)
  
  # sort(): Sorts the list in ascending order.
  my_list.sort()

  # reverse(): Reverses the elements of the list in place.
  my_list.reverse()
  
  # clear(): Removes all elements from the list.
  my_list.clear()
  ```

  Non-In-Place Methods

  ```py
  sorted(list) # Returns a new sorted list; does not modify the original.
  reversed(list) # Returns an iterator that accesses the list in reverse order; does not modify the original.
                    # does not return a list
  list[start:stop:step] # list slicing
  ```

- back iteration `for i in range(n, -1, -1):`
  

### 380 Insert Delete GetRandom O(1)

- see python scope, class and namespace:
[python class documentation](https://docs.python.org/3/tutorial/classes.html)

  > Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change — this eliminates the need for two different argument passing mechanisms as in Pascal.


  Modifying an Object Inside a Function:
  - Since the function receives a reference to the original object, if you modify the object inside the function, you are modifying the same object that the caller has.

  - This means that changes made within the function will be visible outside of it, as both the caller and the function are accessing the same object in memory.
    

  ```python
  def modify_list(my_list):
      my_list.append(4)

  numbers = [1, 2, 3]
  modify_list(numbers)
  print(numbers)  # Output: [1, 2, 3, 4]
  ```

  Important Note:
  - While the object itself can be modified inside the function (if it is mutable, like lists, dictionaries, etc.), you cannot change the reference (pointer) to point to a different object within the function.
  - For example:
    ```python
    def reassign_list(my_list):
        my_list = [4, 5, 6]  # This reassigns the local reference, not the original list

    numbers = [1, 2, 3]
    reassign_list(numbers)
    print(numbers)  # Output: [1, 2, 3]
    ```
  In this case, `my_list` is reassigned to a new list within the function, but this reassignment does not affect the original `numbers` list.

  > A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.

  > Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)

  > The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.

  > A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

  > Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:
  > - the innermost scope, which is searched first, contains the local names
  >- the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names
  >- the next-to-last scope contains the current module’s global names `global` means module-level binding**
  >- the outermost scope (searched last) is the namespace containing built-in names

  > 
    ```
    def scope_test():
      def do_local():
          spam = "local spam"

      def do_nonlocal():
          nonlocal spam
          spam = "nonlocal spam"

      def do_global():
          global spam
          spam = "global spam"

      spam = "test spam"
      do_local()
      print("After local assignment:", spam)
      do_nonlocal()
      print("After nonlocal assignment:", spam)
      do_global()
      print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)
    ```
    ```
    After local assignment: test spam
    After nonlocal assignment: nonlocal spam
    After global assignment: nonlocal spam
    In global scope: global spam
    ```
  > Note how the local assignment (which is default) didn’t change scope_test's binding of spam. The nonlocal assignment changed scope_test's binding of spam, and the global assignment changed the module-level binding.
  > You can also see that there was no previous binding for spam before the global assignment.

- class
  ```
  class Dog:

      kind = 'canine'         # class variable shared by all instances

      def __init__(self, name):
          self.name = name    # instance variable unique to each instance

  >>> d = Dog('Fido')
  >>> e = Dog('Buddy')
  >>> d.kind                  # shared by all dogs
  'canine'
  >>> e.kind                  # shared by all dogs
  'canine'
  >>> d.name                  # unique to d
  'Fido'
  >>> e.name                  # unique to e
  'Buddy'
  ```

- print all dict methods with dir()
  `print(dir(dict()))`

- dict methods
  `s.pop(key)`

  popitem(): Removes and returns a random key-value pair as a tuple. In Python 3.7+, it removes the last inserted item.
  ```py
  my_dict = {'a': 1, 'b': 2}
  item = my_dict.popitem()  # Output: ('b', 2)
  print(my_dict)  
  ```

  `my_dict.clear()` removes all items



  ```py
  my_dict = {'a': 1, 'b': 2}
  my_dict.update({'c': 3, 'a': 10})
  print(my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3}
  ```

  ```py
  my_dict = {'a': 1, 'b': 2}
  value = my_dict.get('a')  # Output: 1
  value = my_dict.get('c', 0)  # Output: 0 (default value)
  ```

  | Method           | Description                               |
  |------------------|-------------------------------------------|
  | `dict[key]`      | Adds or updates key-value pairs          |
  | `update()`       | Updates with another dictionary or iterable|
  | `get()`          | Retrieves value by key, with optional default|
  | `pop()`          | Removes key and returns value            |
  | `popitem()`      | Removes and returns the last inserted pair|
  | `clear()`        | Removes all items                        |
  | `keys()`         | Returns view object of all keys          |
  | `values()`       | Returns view object of all values        |
  | `items()`        | Returns view object of all key-value pairs|
  | `setdefault()`   | Returns value of key or inserts default  |
  | `copy()`         | Returns a shallow copy of the dictionary |


- set methods
  `s = set()`
  `s.remove(val)`
  `s.add(val)`

- `len()` always take O(1)

- random

  ```py
  import random
  a = random.randint(0, 2) # both inclusive!!!!!
  rand_elt = random.choice(self.elt_list)
  rand_elts = random.sample(elt_list, 3) # randomly select 3 elts from an iterable, returned as a list
  ```

### 238 Product of Array Except Self

- back iteration
  `for i,num in reversed(list(enumerate(nums))):`
  `for i in reversed(list(range(n))):`
- list comprehension with `zip()`: `answer = [x*y for x,y in zip(forward_prods, back_prods)]`

### 42 Trapping Rain Water

- Python stack is just list, `l.append()`,`l.pop()`, judging empty by `if l:`, peek by `l[-1]`


### 13 Roman to Integer

- Use python dict as Macro, dict can also help to compare the defined value of strings

### 58 Length of Last Word

Python provides a wide range of string manipulation methods that are very useful for working with and modifying text. Below are some of the most commonly used string manipulation techniques:

 1. Basic String Operations

- Repetition: Repeat strings using the `*` operator.
  
  ```python
  a = "Ha"
  result = a * 3  # "HaHaHa"
  ```


 2. Slicing Strings


- Step in Slicing: Extract characters with a step.
  
  ```python
  step_substring = a[::2]  # "Hlo" (every second character)
  ```

 3. Changing Case

- Convert to Uppercase:
  
  ```python
  a = "hello"
  result = a.upper()  # "HELLO"
  ```

- Convert to Lowercase:
  
  ```python
  a = "HELLO"
  result = a.lower()  # "hello"
  ```

- Capitalize the First Letter:
  
  ```python
  a = "hello"
  result = a.capitalize()  # "Hello"
  ```

- Title Case (Capitalize Each Word):
  
  ```python
  a = "hello world"
  result = a.title()  # "Hello World"
  ```

- Swap Case (Lowercase becomes uppercase and vice versa):
  
  ```python
  a = "HeLLo WoRLD"
  result = a.swapcase()  # "hEllO wOrld"
  ```

 4. String Searching and Checking

- Check if a Substring Exists:
  
  ```python
  a = "Hello world"
  exists = "world" in a  # True
  ```

- Find the Index of a Substring:
  
  ```python
  a = "Hello world"
  index = a.find("world")  # 6
  ```

- Check if String Starts/Ends with a Substring:
  
  ```python
  starts = a.startswith("Hello")  # True
  ends = a.endswith("world")      # True
  ```

 5. Splitting and Joining Strings

- Split a String into a List (based on a delimiter):
  
  ```python
  a = "one, two, three"
  words = a.split(", ")  # ['one', 'two', 'three']
  ```

- Join a List of Strings into a Single String:
  
  ```python
  words = ["one", "two", "three"]
  sentence = ", ".join(words)  # "one, two, three"
  ```

 6. Replacing Substrings

- Replace All Occurrences of a Substring:
  
  ```python
  a = "Hello world"
  result = a.replace("world", "there")  # "Hello there"
  ```

 7. Trimming Whitespace

- Remove Leading and Trailing Spaces:
  
  ```python
  a = "   Hello world   "
  result = a.strip()  # "Hello world"
  ```

- Remove Leading Spaces Only:
  
  ```python
  result = a.lstrip()  # "Hello world   "
  ```

- Remove Trailing Spaces Only:
  
  ```python
  result = a.rstrip()  # "   Hello world"
  ```

8. Checking String Properties

- Check if String Contains Only Digits (negative integers won't work):
  
  ```python
  a = "12345"
  is_digit = a.isdigit()  # True
  ```

- Check if String Contains Only Alphabetic Characters:
  
  ```python
  a = "Hello"
  is_alpha = a.isalpha()  # True
  ```

- Check if String Contains Alphanumeric Characters:
  
  ```python
  a = "Hello123"
  is_alnum = a.isalnum()  # True
  ```

- Check if String is Uppercase or Lowercase:
  
  ```python
  a = "HELLO"
  is_upper = a.isupper()  # True
  
  b = "hello"
  is_lower = b.islower()  # True
  ```


10. Reversing a String

- Using Slicing:
  
  ```python
  a = "Hello"
  result = a[::-1]  # "olleH"
  ```

11. Counting Substrings

- Count Occurrences of a Substring:
  
  ```python
  a = "banana"
  count = a.count("a")  # 3
  ```

12. Escaping Characters

- Escape Special Characters:
  
  ```python
  a = "He said, \"Hello!\""
  print(a)  # He said, "Hello!"
  ```

13. String Comparison

- Compare Strings Alphabetically:
  
  ```python
  a = "apple"
  b = "banana"
  result = a < b  # True (since "apple" comes before "banana")
  ```

Summary:
These common string manipulation methods are widely used in Python programming for everything from data cleaning to formatting output. Python strings are immutable, which means that every time you modify a string, a new one is created, so operations like `replace`, `upper`, or `strip` return new strings rather than modifying the original string.

### 151 Reverse Words in a String

    ```py
        list_words = s.split() # automatically splits words and handles multi-spaces
        list_words.reverse()
        return " ".join(list_words)
    ```

### 6 Zigzag Conversion

- Using string concatenation character by character in Python is generally inefficient because Python strings are immutable, meaning that every time you concatenate, a new string object is created.

- list comprehension with `for` and `if`: `possible = [x for x in possible if x+i < len_haystack and haystack[x+i] == needle[i]]`

## Sliding Window

### 209 Minimum Size Subarray Sum

- In the Dictionary, the key must be unique and immutable. This means that a Python Tuple can be a key whereas a Python List can not. 

### 30 Substring with Concatenation of All Words

- `Counter`
  ```py
  from collections import Counter
  cnt = Counter([1, 2, 2, 3])
  ```
  if writing `cnt2 = cnt1`, since a Counter object is immutable, `cnt2` and `cnt1` will refer to the same object. Thus, changing one will change the other. So, need to copy them.
  To create a shallow copy, `cnt2 = cnt1.copy()`

  Methods of `Counter`:

   - `elements()`: Returns an iterator over elements, repeating each as many times as its count.
     ```python
     counter = Counter([1, 2, 2, 3])
     print(list(counter.elements()))  # Output: [1, 2, 2, 3]
     ```

   - `most_common([n])`: Returns the `n` most common elements and their counts from the most common to the least.
     ```python
     counter = Counter([1, 2, 2, 3, 3, 3, 4])
     print(counter.most_common(2))  # Output: [(3, 3), (2, 2)]
     ```

   - `subtract()`: Subtracts counts, but keeps non-positive counts.
     ```python
     counter = Counter([1, 2, 2, 3])
     counter.subtract([2, 3])
     print(counter)  # Output: Counter({1: 1, 2: 1, 3: 0})
     ```

  Arithmetic operations on counters:
   You can add, subtract, intersect, or union counters.

   ```python
   c1 = Counter([1, 2, 2, 3])
   c2 = Counter([2, 3, 3, 4])

   # Addition of counters
   print(c1 + c2)  # Output: Counter({2: 3, 3: 3, 1: 1, 4: 1})

   # Subtraction of counters
   print(c1 - c2)  # Output: Counter({1: 1, 2: 1})

   # Intersection (min of counts)
   print(c1 & c2)  # Output: Counter({2: 1, 3: 1})

   # Union (max of counts)
   print(c1 | c2)  # Output: Counter({2: 2, 3: 2, 1: 1, 4: 1})
   ```

## Matrix

### 36 Valid Sudoku

- Do not use `cnts = [{}] * 9`
  which will create 9 mutable dicts, which will always be the same
  despite that we only one to change one of them
  use `cnts = [{} for _ in range(9)]` instead

- range judgement can be directly written in one condition: `2 < j <= 5`

- use `self.method()` for methods inside the class, when return, use `return (a and b)`
  ```py
        return (self.is_valid_row(board)
                and self.is_valid_col(board)
                and self.is_valid_grid(board))
  ```

- The zip() function in Python is used to combine two or more iterables (like lists, tuples, or strings) into an iterator of tuples, where each tuple contains elements from each iterable at the same index. The resulting object from zip() is a zip object, which is an iterator. You can convert it into a list or iterate over it directly.

- regroup matrix columns from rows: `zip(*board)` `list(zip(*board))`

- unpacking arguments
  In Python, `*var` and `**var` are used for unpacking arguments in function calls or definitions. Let's break them down:

  1. `*var` (Unpacking Positional Arguments)

  When used in function definitions, `*var` collects all the positional arguments passed to the function into a tuple. When used in function calls, it unpacks an iterable (like a list or tuple) into individual positional arguments.

  Example in function definition:
  ```python
  def example_func(*args):
      print(args)

  example_func(1, 2, 3)
  ```
  Output:
  ```
  (1, 2, 3)
  ```
  Here, `args` is a tuple containing all the positional arguments passed to the function.

  Example in function call:
  ```python
  numbers = [1, 2, 3]
  print(*numbers)
  ```
  Output:
  ```
  1 2 3
  ```
  Here, `*numbers` unpacks the list into individual elements.

  1. `**var` (Unpacking Keyword Arguments)

  When used in function definitions, `**var` collects all the keyword arguments passed to the function into a dictionary. When used in function calls, it unpacks a dictionary into keyword arguments.

  Example in function definition:
  ```python
  def example_func(**kwargs):
      print(kwargs)

  example_func(a=1, b=2, c=3)
  ```
  Output:
  ```
  {'a': 1, 'b': 2, 'c': 3}
  ```
  Here, `kwargs` is a dictionary containing all the keyword arguments passed to the function.

  Example in function call:
  ```python
  data = {'a': 1, 'b': 2, 'c': 3}
  example_func(**data)
  ```
  This unpacks the dictionary `data` into keyword arguments: `a=1`, `b=2`, `c=3`.

  Using `*` and `**` Together:
  You can use both `*` and `**` in the same function definition to handle both positional and keyword arguments:

  ```python
  def example_func(*args, **kwargs):
      print("Positional:", args)
      print("Keyword:", kwargs)

  example_func(1, 2, a=3, b=4)
  ```
  Output:
  ```
  Positional: (1, 2)
  Keyword: {'a': 3, 'b': 4}
  ```

  Summary:
  - `*var` handles multiple positional arguments or unpacks an iterable into individual arguments.
  - `**var` handles multiple keyword arguments or unpacks a dictionary into keyword arguments.

- determine whether list elts are unique: `len(l) == len(set(l))`

- list comprehension with two for loops: `l = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]`

- for loop with an explicit iterable, grouping elements:
  ```py
  for j in [0, 3, 6]:
      l = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
  ```

### 54 Spiral Matrix

- pattern matching
  Pattern matching in Python was introduced in **Python 3.10** as a way to match patterns against values using a `match` statement. It is similar to switch-case statements in other languages but much more powerful. Pattern matching allows for checking the structure and values of objects in a readable and structured way.

  Syntax:

  ```python
  match value:
      case pattern1:
          # Action when value matches pattern1
      case pattern2:
          # Action when value matches pattern2
      case _:
          # Default case, similar to "else"
  ```

  Example 1: Simple Pattern Matching (like switch-case)
  ```python
  def http_error(status):
      match status:
          case 400:
              return "Bad request"
          case 404:
              return "Not found"
          case 418:
              return "I'm a teapot"
          case _:
              return "Something's wrong"

  print(http_error(404))
  ```

  Output:
  ```
  Not found
  ```

  Example 2: Matching Complex Data Structures

  You can match against more complex data types, like lists, tuples, or dictionaries, and even decompose them during the match.

  ```python
  def handle_point(point):
      match point:
          case (0, 0):
              return "Origin"
          case (x, 0):
              return f"X-axis at {x}"
          case (0, y):
              return f"Y-axis at {y}"
          case (x, y):
              return f"Point at ({x}, {y})"
          case _:
              return "Not a point"

  print(handle_point((3, 4)))
  ```

  Output:
  ```
  Point at (3, 4)
  ```

  Example 3: Matching with Guards

  You can add conditional expressions, called **guards**, to your patterns. Guards are useful for adding extra conditions beyond just structural matching.

  ```python
  def process_number(x):
      match x:
          case x if x < 0:
              return "Negative number"
          case x if x == 0:
              return "Zero"
          case x if x > 0:
              return "Positive number"

  print(process_number(-5))
  ```

  Output:
  ```
  Negative number
  ```

  Example 4: Matching Dictionary-like Objects

  Pattern matching can also be used with dictionaries or classes that have attributes.

  ```python
  def process_order(order):
      match order:
          case {"type": "fruit", "name": name, "quantity": quantity}:
              return f"Fruit order: {quantity}x {name}"
          case {"type": "vegetable", "name": name}:
              return f"Vegetable order: {name}"
          case _:
              return "Unknown order"

  order = {"type": "fruit", "name": "apple", "quantity": 10}
  print(process_order(order))
  ```

  Output:
  ```
  Fruit order: 10x apple
  ```

  Example 5: Matching Class Instances

  You can match attributes from a class, using the `case` statement with a constructor pattern:

  ```python
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y

  def handle_point(point):
      match point:
          case Point(0, 0):
              return "Origin"
          case Point(x, 0):
              return f"X-axis at {x}"
          case Point(0, y):
              return f"Y-axis at {y}"
          case Point(x, y):
              return f"Point at ({x}, {y})"
          case _:
              return "Unknown point"

  p = Point(3, 4)
  print(handle_point(p))
  ```

  Output:
  ```
  Point at (3, 4)
  ```

  Summary of Pattern Matching:
  1. Structural Matching: You can match against the structure (e.g., tuples, lists, dictionaries) and decompose them.
  2. Guards: Add conditions to the patterns.
  3. Default Case: Use `_` as a wildcard (like `else` or `default`).
  4. Complex Matching: Match class instances and data classes.

  Pattern matching in Python is very flexible and can be used for tasks that require handling many cases or conditions. Would you like to see a specific example or dive deeper into any use case?

- `[::-1]` is a slicing technique that reverses the order of a sequence (like a list, string, tuple, etc.). 
  `start:end:step`: This is the general format of slicing.
  ```py
  lst = [1, 2, 3, 4, 5]
  reversed_lst = lst[::-1]
  ```
- Use [::-1] when you need a reversed copy of a list and don't care about memory overhead.
  Use reversed() when you need to iterate over a sequence in reverse without creating a new list, or if you're dealing with very large data where memory efficiency matters.

- `and` operator: the `and` operator returns the first falsy value or the last value if all are truthy.
  ```py
  print([])               # output []
  print([] and 1)         # output []
  print([] and [1])       # output []
  print([2] and [1])      # output [1]
  ```

- `or` operator: If the first operand is truthy (i.e., evaluates to True), it returns that operand immediately.
  If the first operand is falsy (i.e., evaluates to False), it returns the second operand.
  ```py
  print(0 or 2)       # output 2
  print(0 < 1 or 3)   # output True
  print([] or {})     # output {}
  ```

- `spiral(self, matrix)`, but when calling `self.spiral(matrix)`, self is automatically included as the first argument, no need to pass it.

- using `[*matrix.pop(0)]` instead of `matrix.pop(0)` because zip(*matrix) will create tuples and matrix.pop(0) will thus be a tuple

- using [*matrix.pop(0)] instead of list(matrix.pop(0)) may be more pythonic?
  ```py
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
      return matrix and list(matrix.pop(0)) + self.spiralOrder(matrix=[*zip(*matrix)][::-1])
  ```

### 48 Rotate Image

- `matrix[:] = [list(x)[::-1] for x in zip(*matrix)]`  the slice notation [:] means "take all elements of the list (or other sequence) from the start to the end."
  Often used when you want to create a shallow copy of a list without modifying the original list, but don't need a deep copy.
Preserving Immutability: If you want to pass a copy of a list into a function and ensure the original list remains unchanged, but you don't need to duplicate nested structures. matrix.copy() does the same thing as matrix[:], creating a shallow copy.

- list slices can be directly assigned to
  
- `copy.deepcopy()`

- `matrix = [[7,4,1],[8,5,2],[9,6,3]]` This is not in-place
  
- The reason `matrix[:] = zip(*matrix)` works is that Python allows you to assign any iterable (like the iterator returned by `zip()`) to a list slice. Python automatically expands the iterable, iterating over its values, and replaces the contents of matrix with those values.

- `[~i]` is way nicer than `[-1-i]`

- `A[:] = map(list, zip(*A[::-1]))`, `map` accepts one function and one or more iterable
  
  `summed = map(lambda x, y: x + y, list1, list2)`

  `result = map(str.upper, ['apple', 'banana', 'cherry'])`

  `map()` returns an iterable, so `result = list(map(function, iterable))`

## Hashmap

### 383 Ransom Note

- revisit numerical operators for Counters (not applicable for dicts)
  ```py
          mag = Counter(magazine)
          ransom = Counter(ransomNote)
          return mag >= ransom
  ```

  `return mag - ransom > 0`

### 205 Isomorphic Strings

- when you have a dict, you can directly look it up instead of creating another set for its keys....

- ord() converts a single character into its integer Unicode code point.
  It works with both ASCII and Unicode characters.
  The inverse function of ord() is chr(), which takes a Unicode code point (integer) and returns the corresponding character.
  `print(chr(ord('A') + 1))  # Output: 'B'`

- s is a string, `s.find()` returns the first occurence of a substring (can be multiple chars) in a string. 
  It returns -1 while not exists, unlike s.index() that raises an error

  ```py
  s = "hello world"
  print(s.find("world"))  # Output: 6
  print(s.find("python")) # Output: -1
  ```

### 49 Group Anagrams

- `"".join(sorted(w))` w is a string

## Intervals

### 56 Merge Intervals

- sort a list based on the first element (actually python automatically sort based on the first element)
  ```py
  >>> t = [['D', 'F', 'E', 'D', 'F', 'D'], ['A', 'F', 'E', 'C', 'F', 'E'], ['C', 'E', 'E', 'F', 'E', 'E'], ['B', 'F', 'E', 'D', 'F', 'F']]
  >>> t.sort(key=lambda x: x[0]) 
  ```

## Stack

### 155 Min Stack

- Initialize an int without value: `a = None`

### 150 Evaluate Reverse Polish Notation

- python ints are 32 bits

- to check if a string is a number(including negative numbers), you can only do with trying converting to int/float and catch
  
  ```py
  def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
  ``` 

- use `int(a / b)` to truncate the result of a division, which effectively removes the decimal part and rounds the result towards zero. Alternatively, use `math.trunc(num)`

### 224 Basic Calculator

- check whether an object is an instance of a class: `isinstance(tokens[i], int)`
  for example, check whether something is an int

- In Python, int is a class.

  In Python, almost everything is an object, and every object is an instance of some class. The int type, which represents integer numbers, is actually a class that is built into Python.

  You can confirm this with the type() function:

  ```python
  x = 5
  print(type(x))  # Output: <class 'int'>
  ```

  In this example, x is an integer, and its type is `<class 'int'>`. So, int is indeed a class in Python, just like user-defined classes.

- user-defined classes themselves (the class object) versus instances of user-defined classes (objects created from the class).

  Here's why instances of user-defined classes can be used as dictionary keys, but the class object itself generally should not:

  1. User-defined class objects (the class itself)
  A class object (e.g., MyClass) refers to the class definition, not any specific instance of it. By default, class objects do not have the properties required to be used as dictionary keys in the same way that instances do, mainly because:

  Class objects are mutable: The class itself can change dynamically at runtime. For example, you can add new methods or attributes to a class after its creation, which would change its state and affect its hash. Since the class is mutable in this sense, it does not make a reliable dictionary key unless the __hash__ and __eq__ methods are specifically implemented to account for such changes.

  Hashing behavior may not be defined: The default __hash__ and __eq__ methods of the class object may not behave as you'd expect for dictionary key usage. The class itself doesn’t have a unique, stable identity like instances do, so it’s more ambiguous.

  2. Instances of user-defined classes (objects created from the class)
  By contrast, instances of user-defined classes are perfectly suited to be used as dictionary keys, because:

  Instances have a default hash: When you create an instance of a user-defined class, Python provides it with a default __hash__ method that is based on the memory address of the instance. This ensures that each instance is unique and can be hashed, even if the class is mutable.

  Instances have a unique identity: Each instance is distinct and has its own identity, even if multiple instances are created with the same attributes. This uniqueness makes it suitable for use as a key, as dictionary keys require uniqueness.

  Mutability of the class doesn’t affect the instance: Even though you can change the class at runtime (add methods, modify attributes, etc.), that doesn't affect the instance's hash or equality, because those are tied to the instance's identity (memory address) and not the class definition itself.


- The phrase "almost everything is an object" in Python refers to the fact that nearly all entities in Python - whether they are data types, functions, classes, or even modules — are implemented as objects. However, there are a few low-level constructs (e.g., keywords) that are not objects, which is why we say "almost everything" instead of "everything."

  An object in Python is an instance of a class, which means it has attributes (data) and methods (functions) associated with it. Python's object model is highly consistent: most things you interact with (like numbers, strings, functions, etc.) are instances of classes, and hence, objects.

  What Does "Almost Everything is an Object" Include?

  1. Basic Data Types: All data types in Python are implemented as classes, and the values of these types are objects. For example:
      - Numbers (`int`, `float`, `complex`):
        ```python
        x = 10
        print(type(x))  # <class 'int'>
        ```
        Here, `10` is an instance of the `int` class, meaning it is an object.

      - Strings (`str`):
        ```python
        s = "Hello"
        print(type(s))  # <class 'str'>
        ```
        `"Hello"` is an object of the `str` class.

       - Booleans (`bool`):
         ```python
         b = True
         print(type(b))  # <class 'bool'>
         ```
         `True` is an instance of the `bool` class.

  2. Functions: Functions are also objects in Python. You can pass them as arguments, return them from other functions, and assign them to variables.
    ```python
    def my_function():
        return "Hello"

    print(type(my_function))  # <class 'function'>
    ```

  3. Classes: Classes themselves are objects, created by Python's metaclass system (like `type`).
       ```python
       class MyClass:
           pass

       print(type(MyClass))  # <class 'type'>
       ```
       `MyClass` is an object of the class `type`, and you can manipulate it as an object.

  4. Modules: Modules that you import (e.g., `math`, `os`, etc.) are objects as well.
       ```python
       import math
       print(type(math))  # <class 'module'>
       ```

  5. User-Defined Classes and Instances: When you define your own class, it is also an object. Instances of that class are obviously objects too.

   6. Exceptions: Python exceptions are objects, typically instances of classes that inherit from `BaseException`.

   Exceptions (What’s Not an Object)

   There are a few things in Python that are not objects, which is why we say "almost everything" instead of "everything." These include:

   7. Keywords: Python's reserved words (like `if`, `else`, `while`, `for`, `in`, etc.) are not objects. They are part of the Python syntax, used to define control flow and structure in your code.
       ```python
       # Keywords like 'if', 'else', 'for' are part of the language syntax, not objects
       if True:
           print("This is a keyword example")
       ```

   8. Operators: Symbols like `+`, `-`, `*`, `/` are not objects. They are part of the Python syntax that gets translated into method calls or bytecode during execution. However, you can overload these operators in classes using special methods (e.g., `__add__`).

   9. Statements: Python statements (like `print`, `return`, `yield`, etc.) are also not objects but rather part of the language syntax.

   Why Is This Important?
   Because almost everything is an object in Python, you get a very uniform way of interacting with the language. You can:
   - Pass around functions as arguments (since functions are objects).
   - Dynamically create classes or manipulate them (since classes are objects).
   - Use methods and attributes on almost anything, thanks to Python’s object-oriented nature.

## Linked List

```py
class Node:
    def __init__(self, data=None):
        self.data = data  # The value stored in the node
        self.next = None  # Reference to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to print all the nodes in the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to add a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to remove a node by value
    def remove(self, key):
        current = self.head

        # If the list is empty
        if current is None:
            print("List is empty")
            return

        # If the head is the node to be deleted
        if current.data == key:
            self.head = current.next
            current = None
            return

        # Traverse the list to find the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the node wasn't found
        if current is None:
            print(f"Node with value {key} not found.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None
```

### 138 Copy List with Random Pointer

- instances of class can be used as dictionary keys, cuz they are memory addresses.

- `dictionary.get(key, default_value)` default_value (optional): The value to return if the key is not found. If this is not provided, None is returned by default.
  So, instead of writing `old2new[curr].next = old2new[curr.next] if curr.next != None else None`, write `old2new[curr].next = old2new.get(curr.next)`

## Graphs

### 45 Jump Game II

- access python tuple by index `tup[i]`
- `list.append(elt)`
- `list.insert(i, elt)`
- `list1 + list2`
- python list will need O(N) to pop from index 0, but queue will take O(1) to pop and put. using deque is common and fast. If thread safety is needed, use queue.Queue(), though a bit slower.
- create a list of zeros
  `zeros_list = [0 for _ in range(10)]`
  `zeros_list = [0] * 10`
- python queue, `deque` will be fast, `Queue` will be a bit slower but ensures thread safety

  ```py
  from collections import deque
  de = collections.deque([1, 2, 3])
  # using append() to insert element at right end
  de.append(4)
  # using appendleft() to insert element at left end
  de.appendleft(6)
  # using pop() to delete element from right end
  de.pop()
  de.popleft()
  ```
  Peek front: Use deque[0] to peek at the first element.
  Peek back: Use deque[-1] to peek at the last element.
