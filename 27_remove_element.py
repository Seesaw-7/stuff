class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        idx = 0
        for i in nums:
            if i != val:
                nums[idx] = i
                idx += 1
        return idx
