# Python notes on Leetcode problems

## Array/String

### 169 Majority Element
  
    ```py
    from collections import defaultdict
    d = defaultdict(int)
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
  >- the next-to-last scope contains the current module’s global names **`global` means module-level binding**
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

- Check if String Contains Only Digits:
  
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

### Minimum Size Subarray Sum

- In the Dictionary, the key must be unique and immutable. This means that a Python Tuple can be a key whereas a Python List can not. 

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
