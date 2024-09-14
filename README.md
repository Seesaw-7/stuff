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
