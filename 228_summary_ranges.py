class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        if len(nums) == 0:
            return ans

        start = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == i - 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start])+"->" + str(nums[i-1]))
                start = i

        if start == len(nums) - 1:
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start])+"->" + str(nums[len(nums)-1]))

        return ans
