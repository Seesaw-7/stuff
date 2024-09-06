# My Leetcode solutions and notes

## Array/String

## 80 Remove Duplicates from Sorted Array II

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
  