# My Leetcode solutions and notes

problems that I did not provide solutions with minimum time complexity
45 189 274

## Array/String

### 80 Remove Duplicates from Sorted Array II

Compare nums[i] with nums[k-2], where k signals the current valid sequence. 隔空比较

### 169 Majority Element

#### Algo

- Think about sorting the array `nums.sort()`

- Moore's Voting Algo:
  The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array.
  
  to identify and eliminate pairs of elements from the array that are different.

  The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

  references:

  [leetcode solution](https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=top-interview-150)

  [Moore’s Voting Algorithm: A Powerful Technique for Majority Element Detection in O(1) space/ O(n) time complexity](https://medium.com/@surajbahuguna1/moores-voting-algorithm-a-powerful-technique-for-majority-element-detection-in-o-1-space-o-n-7480e45f881)

#### Language
  
    ```py
    from collections import defaultdict
    d = defaultdict(int)
    ```

### 189 Rotate Array

#### Algo

- think of reversing the array
- reverse can be done in-place by swapping, with O(1) space complexity
  
#### Language

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

#### Language

- use `and` `or` for logical comparison, `&` is only a bitwise operator
- `half = len(l) // 2`

#### Algo

- Think of solving in O(1)

### 55

#### Language

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

#### Language

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
  list[start:stop:step] # list slicing
  ```

- back iteration `for i in range(n, -1, -1):`
  
#### Algo

think of doing counting first (counting to list, instead of a dict)

### 380 Insert Delete GetRandom O(1)

#### Algo

- pop one element from a list takes `O(N)`, but swapping it with the last elt and delete the last elt only takes `O(1)`



#### Language

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

## Graphs

### 45 Jump Game II

#### Algo

[BFS vs DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
Greedy BFS


#### Language

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
