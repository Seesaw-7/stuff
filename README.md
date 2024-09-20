# My Leetcode solutions and notes

problems that I did not provide solutions with minimum time complexity
45 189 274

problems that I was slow to pass
12 58 80 121

## Array/String

### 80 Remove Duplicates from Sorted Array II

Compare nums[i] with nums[k-2], where k signals the current valid sequence. 隔空比较

### 169 Majority Element

- Think about sorting the array `nums.sort()`

- Moore's Voting Algo:
  The algorithm works on the basis of the assumption that the majority element occurs more than n/2 times in the array.
  
  to identify and eliminate pairs of elements from the array that are different.

  The algorithm will ensure that the count remains positive for the majority element throughout the traversal, guaranteeing that it will be selected as the final candidate.

  references:

  [leetcode solution](https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=top-interview-150)

  [Moore’s Voting Algorithm: A Powerful Technique for Majority Element Detection in O(1) space/ O(n) time complexity](https://medium.com/@surajbahuguna1/moores-voting-algorithm-a-powerful-technique-for-majority-element-detection-in-o-1-space-o-n-7480e45f881)

### 189 Rotate Array

- think of reversing the array
- reverse can be done in-place by swapping, with O(1) space complexity

### 121 Best Time to Buy and Sell Stock

- Think of solving in O(1)

### 274 H-Index

think of doing counting first (counting to list, instead of a dict)

### 380 Insert Delete GetRandom O(1)

- pop one element from a list takes `O(N)`, but swapping it with the last elt and delete the last elt only takes `O(1)`

### 135 Candy

I often design algo with two-pass and DP.
It is often locally greedy in both the left-to-right and right-to-left passes. Often, the first pass find the max/min values and the second pass revise it to the exact values.

This is very useful in scenarios where an element depends on both of its neighbours (can be next-to neighbours or very far neighbours).

### 42 Trapping Rain Water

- I used two-pass and DP
- use stack and finishing up little by little

### 14. Longest Common Prefix

- For the same task in each scan, considering using divide and conquor to reduce time complexity, better than linear scan

## Graphs

### 45 Jump Game II

[BFS vs DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
Greedy BFS
