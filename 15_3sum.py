class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        k = n - 1

        a, b = nums[0]-1, nums[1]-1

        for i in range(n-2):
            if nums[i] == a:
                continue
            a = nums[i]
            k = n - 1
            for j in range(i+1, n-1): 
                if nums[j] == b:
                    continue
                b = nums[j] 
                c = a + b 
                while k > j + 1 and  nums[k] + c > 0:
                    k -= 1
                if nums[k] + c == 0:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans
