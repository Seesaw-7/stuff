# My Leetcode solutions and notes

problems that I did not provide solutions with minimum time complexity
14 45 189 274 11 49 117

problems that I did the min time complexity but still not optimal
6 105

problems that I was slow to pass
12 58 80 121 15 128 56 224 25

need to code w/o built-in funcs
14

need to reconsider
15(after 2 sum) 45

problems with other solutions

42 202

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

- can be solved with fast and slow pionter

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

## Stack

### 20 Valid Parenthesis

Use stack for parsing strings that will open and close

### 71 Simplify Path

- When you need to retrieve and pop the previous one, consider using stack
  
- When speraters exists, consider push and pop word to and from stack, instead of single characters
  
- When seperators exists, try splitting by seperaters and join them by seperaters later

## 155 Min Stack

get_min() does not mean that you need to pop an element.. just peeking..

## 224 Basic Calculator

you may not necessarily need to use stack all the way long
use it when you have to (eg. only for parts inside ())

## Linked List

### 141 Linked List Cycle

- To find cycle, either using hashtable or using slow & fast pointers

### 21 Merge Two Sorted Lists

- initialize a linked list with Node(), but only return node.next, this would ease initialization of the first node and ease looping

### 138 Copy List with Random Pointer

- interweaving the new linked list with the old linked list, thus keeping the same sequence. Later, leave out the old linked list.
  
- use hashtable to take down the mapping from the old nodes to new nodes

### 146 LRU Cache

- using a doubly linked list and a dict. The dict keeps track of the key and the node addr which stores the key-value pair
  
  linked lists support O(1) insertion/deletion in the middle, if you specify the address of the node. Thus, we need to keep the address of each node. Use a linked list if need O(1) insertion/deletion in the middle. Use a DLL if the tail need to be considered.

- using a deque and 2 dicts, one taking the key-value pair, the other taking how many times each key appears in the deque

- using a single python dict which is ordered according to insertion sequence

## Binary Tree General

### 104 Maximum Depth of Binary Tree

- divide and conquer(recursive DFS)
  
- iterative DFS

- BFS

- Preorder, In-order, post-order

### 100 Same Tree

- coding
  
  ```py
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            a = p.val == q.val
            b = self.isSameTree(p.left, q.left)
            c = self.isSameTree(p.right, q.right)
            return a and b and c
        else:
            return not p and not q
  ```

### 226 Invert Binary Tree

recursive stack space: O(N) space complexity, or possibly O(log N)

### 101 Symmetric Tree

Time complexity of DFS and BFS in Tree: O(N) num nodes

Time complexity of DFS and BFS in Graph: O(V+E) for adjacency list and O(V^2) for adjacency matrix. because of potential loops, one node can be checked multiple times in a graph, checking whether it is visited or not

Space complexity of DFS in tree: O(h) height of the tree

Space complexity of DFS in graph: O(V) stack space and O(V+E) adjancy list space

Space complexity of BFS in tree: O(b) breadth of the tree

Space complexity of BFS in graph: O(V) queue space and O(V+E) adjacency list space

### 105 Construct Binary Tree form Inorder and Preorder Traversal

- use scratch paper for tree building problems

- think about whether to use recursive or iterative beforehand. choose iterative with stack in this case. Think about what should be kept in the stack, in this case the parent nodes that we need to use again later, which are nodes that has a left child but no right child yet. For nodes with right child, we'll never use it again later
  
- Another solution is to use recursion. We can build the tree subtree by subtree. The root node is always the first node of preorder, then since the inorder is the sequence of nodes in the tree from left to right, the nodes left to the root node in inorder list belongs to the left subtree, and the nodes right to the root nodes belongs to the right subtree. What's important is that the structure of the preorder list is <root node + all left subtree nodes + all subtree nodes>. In addition, we can modify the preorder list in each iteration, with mutable nature of python list. Since the recursions of left subtrees will all be calulated before the right subtrees.
  
  ```py
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root
  ```

### 117 Populating Next Right Pointers in Each Node II

Other than BFS which traverse the tree level by level..

Inorder to fit in O(1) space complexity, we can keep on the currant level, and assign left and right child with the next pointer. We iterate with curr = curr.next which was previously assigned, and assign prev node in the next level with our left or right child. I feel dumb.

## Graphs

### 45 Jump Game II

[BFS vs DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
Greedy BFS

## Dynamic Programming

- DP vs Divide & Conquer
  
  While both approaches involve breaking a problem into smaller subproblems, dynamic programming focuses on solving overlapping subproblems efficiently by storing intermediate results. In contrast, divide and conquer assumes that subproblems are independent and does not reuse the solutions to the subproblems.

  In short, dynamic programming can be thought of as a more specialized version of divide and conquer that optimizes by storing and reusing solutions to overlapping subproblems.

- DP vs Greedy
  
  Greedy algorithms do not guarantee that a locally optimal solution will lead to a globally optimal solution unless the problem has the greedy choice property (i.e., a globally optimal solution can be obtained by making locally optimal choices).

  DP solves each subproblem and stores the result, ensuring that it finds the optimal solution for each subproblem and combines these solutions. It revisits subproblems and reuses solutions from earlier steps to make a globally optimal decision. DP considers all possible decisions at each step and chooses the best one based on prior calculations.
  DP doesn't rely on just one greedy choice. Instead, it examines multiple possibilities and combines results of overlapping subproblems, ensuring that the optimal decision is made globally, not just locally.

  Consider the 0/1 Knapsack problem:

  A greedy algorithm might pick the item with the highest value-to-weight ratio, but this does not always lead to the best solution (e.g., choosing smaller items with slightly lower ratios could give a better total value).
  Dynamic programming considers all subsets of items and ensures the optimal combination by storing and using intermediate results.
