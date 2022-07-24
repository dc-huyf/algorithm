import numpy as np
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if self.data_map.get(val, -1) == -1:
            self.data_map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.data_map.get(val, -1) == -1:
            return False
        old = self.data_map[val]
        new = len(self.nums)-1
        # 交换值
        self.nums[old], self.nums[new] = self.nums[new], self.nums[old]
        self.data_map[self.nums[new]] = new
        self.data_map[self.nums[old]] = old
        # 删除元素
        self.nums.pop()
        del self.data_map[self.nums[new]]
        return True

    def getRandom(self) -> int:
        return self.nums[int(np.random.rand() * len(self.nums))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()