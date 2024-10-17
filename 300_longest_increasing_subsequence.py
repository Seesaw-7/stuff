import bisect

class Solution:
    # DP O(N^2)
    def lengthOfLIS1(self, nums: list[int]) -> int:
        if not nums:
            return 0
        len_nums = len(nums)
        dp = [0 for _ in range(len_nums)]

        for i in range(len_nums):
            for j in range(i, len_nums):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[i]+1, dp[j])

        return max(dp) + 1

    # seems that this implementation is functionally equal to bisect.bisect_left
    def _binary_search(self, nums: list[int], target) -> int:
        # print(target, nums)
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)-1
        elif target == nums[-1]:
            return 0
        i = len(nums) // 2
        if target < nums[i]:
            return self._binary_search(nums[:i], target)
        else:
            return i + self._binary_search(nums[i:], target)

    # Replacement with Binary Search
    def lengthOfLIS(self, nums: list[int]) -> int:
        seq = []
        for num in nums:
            if not seq or num > seq[-1]:
                seq.append(num)
            else:
                idx = self._binary_search(seq, num)
                idx = bisect.bisect_left(seq, num)
                seq[idx] = num

        return len(seq)
