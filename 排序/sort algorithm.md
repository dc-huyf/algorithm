## 几种常见方法的简单实现

#### 1. 冒泡排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    	## 冒泡排序, 超时凉凉，优点：比较稳定
        if len(nums) == 1:
            return nums
        for i in range(1,len(nums)):
            for j in range(0,len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
```



#### 2. 选择排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## 选择排序，，超时凉凉，好处：不占用内存，缺点：不稳定
        if len(nums) == 1:
            return nums
        for i in range(len(nums)-1, 0,-1):
            maxIndex = i
            for j in range(i-1, -1, -1):
                if nums[j] > nums[maxIndex]:
                    maxIndex = j
            if maxIndex != i:
                nums[i], nums[maxIndex] = nums[maxIndex], nums[i]
        return nums
```

#### 3. 插入排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        ## 插入排序，超时，优点：稳定
        for i in range(len(nums)):
            cur = nums[i]
            pre = i-1
            while pre >= 0 and nums[pre] > cur:
                nums[pre+1] = nums[pre]
                pre -= 1
            nums[pre+1] = cur
        return nums
```

#### 4. 希尔排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:  
        '''
        希尔排序：插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。O(nlnO)
        希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。不快，但内存占用少。
        '''
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                while i >= gap and nums[i] < nums[i - gap]:
                    nums[i], nums[i - gap] = nums[i - gap], nums[i]
                    i -= gap
            gap //= 2
        return nums
```



#### 5. 归并排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:  
        ## 归并排序，没超时，但内存使用量和速度比较一般
        if len(nums) < 2:
            return nums
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
        return self.merge(self.sortArray(left), self.sortArray(right))
        
    def merge(self, left, right):
        res = []
        while left and right:
            if left[-1] <= right[-1]:
                res.append(right.pop())
            else:
                res.append(left.pop())
        while left:
            res.append(left.pop())
            
        while right:
            res.append(right.pop())
        
        return sorted(res)
```

#### 6. 快速排序
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
     ## 快速排序：不稳定、但快。使用分治法策略来把一个串行（list）分为两个子串行。理解为冒泡排序基础上的递归分治法。
        if len(nums) >= 2:
            left = []
            right = []
            middle = nums[len(nums)-1]  # 指定最后一个元素为基准
            nums.pop()
            for i in nums:
                if i <= middle:
                    left.append(i)
                else:
                    right.append(i)
            return self.sortArray(left) + [middle] + self.sortArray(right)
        else:
            return nums
```