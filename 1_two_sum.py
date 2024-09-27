class Solution:

    # O(nlogn) use hash table to store positions, sort the array and use two pointers
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        equal = []
        for i,num in enumerate(nums):
            if num in mp and num + num == target:
                equal = [mp[num], i]
            else:
                mp[num] = i

        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r - 1 and nums[l] + nums[r] != target:
            while l < r - 1 and nums[l] + nums[r] < target:
                l += 1
            while l < r - 1 and nums[l] + nums[r] > target:
                r -= 1
            
        return [mp[nums[l]], mp[nums[r]]] if nums[l] != nums[r] else equal

    # O(N)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i,num in enumerate(nums):
            if target - num in mp:
                return [mp[target-num], i]
            else:
                mp[num] = i
