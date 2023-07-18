from typing import List


# class Solution:
#     def get_left_right_index(self, nums):
#         length = len(nums)
#         if length % 2 == 0:
#             return [int(length/2-1), int(length/2)]
#         else:
#             return [int((length-3)/2), int((length+1)/2)]
#
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         # 二分法查找中位数
#         l1, r1 = self.get_left_right_index(nums1)
#         l2, r2 = self.get_left_right_index(nums2)
#         mid1 = nums1[l1+1: r1]
#         mid2 = nums2[l2+1: r2]
#         if len(mid1) + len(mid2) == 2:
#             return (mid1[0]+mid2[0])/2
#         if len(mid1) + len(mid2) == 1:
#             res = mid1+mid2
#             return res[0]
#         return self.findMedianSortedArrays(mid1, mid2)


class Solution:
    def get_left_right_index(self, nums):
        length = len(nums)
        if length % 2 == 0:
            return [int(length/2-1), int(length/2)]
        else:
            return [int((length-3)/2), int((length+1)/2)]

    def findMedianSortedArrays(self, nums1, nums2):
        # 双指针
        if len(nums1) + len(nums2) == 1:
            res = nums1 + nums2
            return res[0]

        l1, r1 = 0, len(nums1)-1
        l2, r2 = 0, len(nums2)-1
        while l1 <= r1 and l2 <= r2:
            mid1 = nums1[l1+1: r1]
            mid2 = nums2[l2+1: r2]
            if len(mid1) + len(mid2) == 2:
                return (mid1[0]+mid2[0])/2
            if len(mid1) + len(mid2) == 1:
                res = mid1+mid2
                return res[0]
            return self.findMedianSortedArrays(mid1, mid2)


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    s = Solution()
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)