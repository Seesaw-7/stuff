class Solution:
    # My sol: use a flag to flag whether the second occurance of a number has occurred
    def removeDuplicates1(self, nums: list[int]) -> int:
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

    # Compare nums[i] with nums[k-2], where k signals the current valid sequence. 
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1 if len(nums) else 0
        k = 2 if len(nums) > 1 else k
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
        