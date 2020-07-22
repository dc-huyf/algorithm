class Solution:
    def search(self, arr, target: int) -> int:
        '''
        先遍历目标区间，再二分查找，存储目标再区间内的索引位置
        '''
        left, right = 0, 1
        record = []
        while right < len(arr):
            if right < len(arr) - 1 and arr[right] >= arr[right - 1]:
                right += 1
            else:
                if target >= arr[left] and target <= arr[right-1]:
                    if self.binary(arr, target, left, right-1):
                        record.append(self.binary(arr, target, left, right-1))
                left = right
                right += 1
        return sorted(record, key=lambda x:x[0])[0][1]

    def binary(self, arr, target, left, right):
        l, r = left, right
        while l < r:
            mid = int((l + r) / 2)
            if arr[mid] == target:
                r = mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if arr[l] == target:
            return [l - left, l]
        else:
            return False

s = Solution()
s.search(arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5)