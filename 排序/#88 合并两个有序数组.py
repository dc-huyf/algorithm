class Solution:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        ## 类似于归并排序的思想
        """
        if nums2:
            end = m + n - 1
            while m > 0 and n > 0:
                if nums2[n - 1] > nums1[m - 1]:
                    nums1[end] = nums2[n - 1]
                    n -= 1
                else:
                    nums1[end] = nums1[m - 1]
                    nums1[m - 1] = 0
                    m -= 1
                end -= 1
            while n > 0:
                nums1[end] = nums2[n - 1]
                n -= 1
                end -= 1
            while m > 0:
                nums1[end] = nums1[m - 1]
                m -= 1
                end -= 1