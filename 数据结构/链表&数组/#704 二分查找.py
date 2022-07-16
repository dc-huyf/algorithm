class Solution:
    def search(self, nums: [int], target: int) -> int:
        s, e = 0, len(nums)-1
        mid = (s+e)//2
        while s <= e :
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                e = mid-1
            if nums[mid] < target:
                s = mid+1
            mid = (s+e) // 2

        return -1


if __name__ == "__main__":
    nums, target = [-1,0,3,5,9,12], 9
    s = Solution()
    print(s.search(nums, target))