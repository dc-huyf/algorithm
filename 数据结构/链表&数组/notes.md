# 链表数组

## 一、双指针的技巧
> 处理数组和链表常常用到

> 对于单链表来说，大部分技巧都属于快慢指针，前文单链表的六大解题套路都涵盖了，比如链表环判断，倒数第 K 个链表节点等问题，它们都是通过一个 fast 快指针和一个 slow 慢指针配合完成任务。
- 双指针技巧主要分为两类：左右指针和快慢指针。
    - 左右指针，就是两个指针相向而行或者相背而行；
    - 而所谓快慢指针，就是两个指针同向而行，一快一慢。
- **只要数组有序，就应该想到双指针技巧**
    
### 1.快慢指针的技巧和应用
- 原地修改数组：除了在有序数组/链表中【去重】，对数组中的某些元素进行【原地删除】
- 数据中的滑动窗口技巧：
    - left 指针在后，right 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

### 2. 左右指针的常用算法
1. 二分查找
2. 两数之和II(#167)
3. 反转数组(#344反转字符串)
4. 回文串的判断(#5最长回文子串)
    - 让左右指针从中心向两端扩展


## 二、前缀和技巧
- 空间换时间的操作
> 你们班上有若干同学，每个同学有一个期末考试的成绩（满分 100 分），那么请你实现一个 API，输入任意一个分数段，返回有多少同学的成绩在这个分数段内。
>那么，你可以先通过计数排序的方式计算每个分数具体有多少个同学，然后利用前缀和技巧来实现分数段查询的

- 前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。

### 1.一维数组
```java
int[] scores; // 存储着所有同学的分数
// 试卷满分 100 分
int[] count = new int[100 + 1]
// 记录每个分数有几个同学
for (int score : scores)
    count[score]++
// 构造前缀和
for (int i = 1; i < count.length; i++)
    count[i] = count[i] + count[i-1];
// 利用 count 这个前缀和数组进行分数段查询
```

### 2.二维数组
- 见【304题】二维区域和检索 - 矩阵不可变
    - 空间换时间的做法，时间复杂度O(1)
    - 把问题转换为：求(i, j) -> (0, 0)元素和的问题，这个思路也比较巧妙
    - 另外，求解过程中，稍稍注意下索引越界问题


## 三、差分数组
- 差分数组的主要适用场景是**频繁**对原始数组的某个区间的元素进行增减。
```java
int[] diff = new int[nums.length];
// 构造差分数组
diff[0] = nums[0];
for (int i = 1; i < nums.length; i++) {
    diff[i] = nums[i] - nums[i - 1];
}
```

- 例题
    - 370题:区间加法
    - 1109题:航班预订统计
    - 1094题:拼车

## 四、遍历数组技巧
- 59：螺旋矩阵II


## **五、二分查找**
- 二分查找真正的坑在于到底要给 mid 加一还是减一，while 里到底用 <= 还是 <。
- **704: 二分查找(唯一)**
- **34: 在排序数组中查找元素的第一个和最后一个位置**

```python
class Solution:
    def search(self, nums: [int], target: int) -> int:
        s, e = 0, len(nums)-1
        mid = (s+e)//2
        while s <= e :
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                e = mid-1 # todo
            if nums[mid] < target:
                s = mid+1
            mid = (s+e) // 2

        return -1

class Solution2:
    def searchRange(self, nums: [int], target: int) -> [int]:
        l, r = self.left_bound(nums, target), self.right_bound(nums, target)
        return [l, r]

    def left_bound(self, nums, target):
        start, end = 0, len(nums)-1 # 在[start, end]内搜索
        while start <= end: # start > end结束,注意保证能够结束循环
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid - 1 # 搜索[start, mid-1]
            if nums[mid] > target:
                end = mid - 1 # 搜索[start, mid-1]
            if nums[mid] < target:
                start = mid + 1 # 搜索[mid+1, end]
        if start >= len(nums):
            return -1
        return start if nums[start]==target else -1

    def right_bound(self, nums, target):
        start, end = 0, len(nums) - 1  # 在[start, end]内搜索
        while start <= end:  # start > end结束,注意保证能够结束循环
            mid = (start + end) // 2
            if nums[mid] == target:
                start = mid + 1  # 增大左边界，搜索[mid+1, end]
            if nums[mid] > target:
                end = mid - 1  # 搜索[start, mid-1]
            if nums[mid] < target:
                start = mid + 1  # 搜索[mid+1, end]
        if start == 0:
            return -1
        return end if nums[end] == target else -1
```



## **六、滑动窗口**
- 76:最小覆盖字串
- 438:找到字符串中所有字母异位词
- 567:字符串的排列
- 3:无重复字符的最长子串
