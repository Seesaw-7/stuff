class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        
        while True:
            if numbers[idx1] + numbers[idx2] == target:
                return [idx1+1, idx2+1]
            elif numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            else:
                idx2 -= 1
        