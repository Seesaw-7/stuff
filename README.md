# My Leetcode solutions and notes

## Array/String

## 80

Compare nums[i] with nums[k-2], where k signals the current valid sequence. 隔空比较

### 169

- Think about sorting the array `nums.sort()`
- py:
  
    ```py
    from collections import defaultdict
    d = defaultdict(int)
    ```

- Moore's Voting Algo:
  The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array.
  
  to identify and eliminate pairs of elements from the array that are different.

  The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

  references:

  [leetcode solution](https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=top-interview-150)

  [Moore’s Voting Algorithm: A Powerful Technique for Majority Element Detection in O(1) space/ O(n) time complexity](https://medium.com/@surajbahuguna1/moores-voting-algorithm-a-powerful-technique-for-majority-element-detection-in-o-1-space-o-n-7480e45f881)
