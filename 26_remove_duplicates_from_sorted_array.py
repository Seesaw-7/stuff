class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1 if len(nums) else 0
        for i in range(0, len(nums)-1):
            if nums[i+1] != nums[k-1]:
                k += 1
                nums[k-1] = nums[i+1]
        return k
