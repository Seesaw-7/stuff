class Solution:

    # Tabulation O(N) Time, O(N) Space
    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))

        return dp[-1]

    # O(1) Space, O(1) Time
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
    
        for i in range(2, len(nums)):
            now = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = now

        return prev2
