class Solution:
    # O(n) Space, beacuse the worst case for tmep is O(n)
    def rotate1(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[len(nums)-k:]
        
        i = len(nums) - 1
        while (i >= k):
            nums[i] = nums[i-k]
            i -= 1
        
        for j in range(0, k):
            nums[j] = temp[j]

    # O(n) Space cuz temporal space created while slicing, but another way to code in python
    def rotate2(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

    # O(1) space when trying to reverse by swapping
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)

        def reverse(left:int, right:int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
