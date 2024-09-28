# My Leetcode solutions and notes

problems that I did not provide solutions with minimum time complexity
14 45 189 274 11 49

problems that I did the min time complexity but still not optimal
6

problems that I was slow to pass
12 58 80 121 15 128 56

need to code w/o built-in funcs
14

need to reconsider
15(after 2 sum) 45

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

### 14 Longest Common Prefix

- For the same task in each scan, considering using divide and conquor to reduce time complexity, better than linear scan

### 6 Zigzag Conversion

Sometimes we need to extract necessary info, leaving out unnecessary info from the problem description

Instead of constructing an explicit matrix, you can:

Track the current row.
Append characters directly to the appropriate row.
After processing all characters, concatenate the rows.

### 28 Find the Index of the First Occurance in a String

do candidate elimination, if sliding window is costly

### 11 Container with Most Water

obvious O(N^2) solutio with two different indices might have a greedy O(N) solution

The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

## Sliding Window

### 209 Minimum Size Subarray Sum

A sliding window with a continuously shrinking size, effectively two pointers but both moving in the same direction

### 3 Longest Substring without Repeating characters

- For a sliding window with a flexible size, better write in left and right pointers

  one effective way is that we can iterate the right pointer over the whole array,
  updating the left pointer inside each loop according to different conditions

- To avoid O(window_size) list elt lookup, we can simply use a dict to store the position of each elt in the list

### 30 Substring with Concatenation of All Words

- Brute force might be very helpful to complex questions, while doing a lot of optimization before AC is a bit time consuming

- repeatedly slicing a string is expensive, so we may use pointers when not necessary to slice

- if the size of the sliding window is 3, we only need to scan it in 3 times, starting form the first character, the second and the third respectively

## Matrix

### 289 Game of Life

since the type is int, and it only contains 0 or 1, we can use the second to last bit to denote the new state and shift it later

## Hashmap

### 205 Isomorphic Strings

- Check whether two iterables are isomorphic by checking their pairings.
  `return len(set(zip(s,t))) == len(set(s)) == len(set(t))`

- by checking the first occurence position of every char in s and t are the same
  `return list(map(s.find, s)) == list(map(t.find, t))`

### 49 Group Anagrams

- we can use dict for grouping, where the key is their shared feature, and the value is the list of elts with this feature

- the dict key should be immutable, so we cannot use a Counter object as the key, but we can use the sorted string for the anagrams

### 1 Two Sum

- use one pass hashtable. Record the num-position pair in the hashtable. if target-num in hashtable, then return their positions

### 202 Happy Number

- convert int to str to manipulate each digit in parallel `n = sum([int(x) ** 2 for x in str(n)])`

## Intervals

### 56 Merge Intervals

- When you need to compare two neighbouring elts in a list, always compare this one to the previous one, instead of comparing the currant one to the future one

- be very careful with flags (states), do not use them when not necessary

- do not initialize too many variables, like `temp`. Initialize them only when necessary. This would be very redundant and time consuming
  
- you can revise the answer in the answer list XD
  
- you can put edge case judegment inside conditions of a loop
  ```py
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort()
      ans = []

      for ran in intervals:
          if not ans or ans[-1][1] < ran[0]:
              ans.append(ran)
          else:
              ans[-1][1] = max(ans[-1][1], ran[1])

      return ans
  ```

### 57 Insert Interval

- When dealing with intervals, draw all possible conditions
- keep the logic as simple as possible

### 452 Minimum Number of Arrows to Burst Balloons

effectively the maximum number of non-overlapping intervals

first sort the intervals according to their left end,
then we favor to replace the interval with a shorter right end to the non_overlap list,
because they can potentially accomodate more non-overlapping intervals

always greedily shooting where most intervals overlap is not globally optimal

## Graphs

### 45 Jump Game II

[BFS vs DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
Greedy BFS
