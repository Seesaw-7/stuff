class Solution:
    def merge1(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        idx = m+n-1
        while (idx >= 0):
            if i < 0:
                nums1[idx] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[idx] = nums1[i]
                    i -= 1
                else:
                    nums1[idx] = nums2[j]
                    j -= 1
            idx -= 1

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(0, n):
            nums1[m+i] = nums2[i]
        nums1.sort()
