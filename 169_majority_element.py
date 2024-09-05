from collections import defaultdict

class Solution:
    # Hash map
    def majorityElement1(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            
        max_k = nums[0]
        max_v = 0
        for k, v in cnt.items():
            if v > max_v:
                max_k = k
                max_v = v
        return max_k

    # Moore's Voting Machine
    def majorityElement(self, nums: list[int]) -> int:       
        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count += 1
        return candidate
        