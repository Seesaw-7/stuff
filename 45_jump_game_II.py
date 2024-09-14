from collections import deque

class Solution:

    # O(N^2) Iterative DP
    def jump1(self, nums: list[int]) -> int:
        len_nums = len(nums)

        reach = [len_nums for x in range(len_nums)] #tuple.first record whether
        reach[0] = 0

        for i, num in enumerate(nums):
            if reach[i] != len_nums: # this point is reachable
                for j in range(1, num+1):
                    if i+j < len_nums and reach[i+j] > reach[i] + 1:
                        reach[i+j] = reach[i] + 1
                        if i+j == len_nums - 1:
                            return reach[i+j]
        
        return reach[-1]

    # BFS
    def jump2(self, nums: list[int]) -> int:
        visited = deque()
        visited.append(0)

        len_nums = len(nums)
        depth = [len_nums for x in range(len_nums)]
        depth[0] = 0

        while visited and depth[-1] == len_nums:
            v = visited.popleft()
            for i in range(1, nums[v]+1):
                if v+i < len_nums and depth[v+i] == len_nums:
                    visited.append(v+i)
                    depth[v+i] = depth[v] + 1
        
        return depth[-1]

    # Greedy BFS O(N)
    def jump(self, nums: list[int]) -> int:
        last_jump_pos = 0
        max_reachable = 0
        num_jumps = 0

        for i,num in enumerate(nums):
            if last_jump_pos < len(nums)-1: # hasn't reached end
                max_reachable = max(max_reachable, i+num)
                if i == last_jump_pos:
                    num_jumps += 1
                    last_jump_pos = max_reachable

        return num_jumps