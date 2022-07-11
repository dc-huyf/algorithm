from collections import deque
class Solution:
    def openLock(self, deadends, target: str) -> int:
        '''
        心路历程：
        初始化：'0000'
        每次转动前，都有一个备选方案集合：8个，相当于每个结点有8个相邻的节点
        '''
        # 回头路原则
        track = set()
        track.add('0000')
        record = deque([('0000')])
        step = 0
        while record:
            # 遍历当前队列
            lens = len(record)
            for q in range(lens):
                cur = record.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                # 加入当前节点的所有相邻节点
                for i in range(len(cur)):
                    # 两种选择
                    tmp = cur[:i] + self.plusone(cur[i]) + cur[i+1:]
                    if tmp not in track:
                        record.append(tmp)
                        track.add(tmp)
                    tmp = cur[:i] + self.jianone(cur[i]) + cur[i+1:]
                    if tmp not in track:
                        record.append(tmp)
                        track.add(tmp)
            step += 1
        return -1
    # 每次都要做选择，上或者下
    def plusone(self, s):
        if s == "9":
            return "0"
        else:
            return str(int(s) + 1)
    def jianone(self, s):
        if s == "0":
            return "9"
        else:
            return str(int(s) - 1)

s = Solution()
s.openLock(["0201","0101","0102","1212","2002"], "0202")
