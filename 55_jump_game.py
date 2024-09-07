class Solution:

    # O(N^2)
    def canJump1(self, nums: list[int]) -> bool:

        len_num = len(nums)

        reach = [0 for x in range(len_num)]
        reach[0] = 1

        len_num = len(nums)

        for i, num in enumerate(nums):
            if reach[i] == 1:
                if num > 0:
                    for j in range(1, min(num+1, len_num-i)):
                        if i+j < len_num:
                            reach[i+j] = 1
                        if reach[-1] == 1:
                            return True

        return reach[-1]

    # O(N)
    def canJump2(self, nums: list[int]) -> bool:

        len_nums = len(nums)
        max_steps = 0

        for i in range(len_nums):
            max_steps = max(max_steps, nums[i])
            max_steps -= 1

            if max_steps < 0 and i != len_nums-1:
                return False
            if i + max_steps >= len_nums :
                return True

        return True

    # better coding style
    def canJump(self, nums: list[int]) -> bool:

        max_steps = 0

        for num in nums:
            if max_steps < 0:
                return False
            elif max_steps < num:
                max_steps = num
            max_steps -= 1

        return True
    