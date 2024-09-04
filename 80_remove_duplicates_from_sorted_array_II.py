class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1 if len(nums) else 0
        flag = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
                flag = 0
            else:
                if flag == 0:
                    nums[k] = nums[i]
                    k += 1
                    flag = 1
        return k
