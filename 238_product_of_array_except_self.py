class Solution:
    def productExceptSelf1(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        forward_prods = [0] * len_nums
        back_prods = [0] * len_nums
        prod1 = 1
        prod2 = 1

        for i,num in enumerate(nums):
            forward_prods[i] = prod1
            prod1 *= num

        for i,num in reversed(list(enumerate(nums))):
            back_prods[i] = prod2
            prod2 *= num

        answer = [x*y for x,y in zip(forward_prods, back_prods)]
        return answer

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        answer = [0] * len_nums
        prod1 = 1
        prod2 = 1
    
        for i,num in enumerate(nums):
            answer[i] = prod1
            prod1 *= num

        for i,num in reversed(list(enumerate(nums))):
            answer[i] *= prod2
            prod2 *= num       

        return answer
