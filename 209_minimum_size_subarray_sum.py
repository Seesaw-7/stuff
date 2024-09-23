import math

class Solution:
    # I miss understood the question which requires the sum equal to target
    def minSubArrayLen1(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        d = {}
        for num in nums:
            d1 = {num: 1}
            for k, v in d.items():
                if k+num <= target:
                    d1[k+num] = min(v+1, d.get(k+num, n))
            d.update(d1)
        return d.get(target, 0)

    # I miss understood again
    # subarray is contiguous while subsequence is not
    def minSubArrayLen2(self, target: int, nums: list[int]) -> int:
        max_val = max(nums)
        cnt = [0 for _ in range(max_val+1)]

        for num in nums:
            cnt[num] += 1

        accum = 0
        ans_num = 0
        print(cnt)

        for i in reversed(list(range(1, max_val+1))):
            if accum + cnt[i] * i < target:
                accum += cnt[i] * i
                ans_num += cnt[i]
            else:
                print(accum)
                a = math.ceil((target - accum) / i)
                print(ans_num, a)
                ans_num += a
                return ans_num

        return 0

    # O(N) sliding window with continuously shrinking window size (effectively two pointers moving in the same direction)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        window_size = 0
        accum = 0

        for i,num in enumerate(nums):
            window_size += 1
            accum += num
            if accum >= target:
                break

        if accum < target:
            return 0

        for i,num in enumerate(nums):
            if i == 0:
                continue
            accum = accum - nums[i-1]
            if accum >= target:
                window_size -= 1
            else:
                if i + window_size-1 < len(nums):
                    accum += nums[i+window_size-1]
                
        return window_size
    