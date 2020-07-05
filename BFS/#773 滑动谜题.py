from collections import deque
import copy
class Solution:
    def slidingPuzzle(self, board) -> int:
        target = "123450"
        # 初始化
        start = ""
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])

        if start == target:
            return 0
        record = deque([start])
        track = {start}
        step = 1

        while record:
            for _ in range(len(record)):
                cur = record.popleft()
                # 做选择，寻找零的位置
                res = self.exchange_pos(cur)
                for cc in res:
                    if cc == target:
                        return step
                    if cc not in track:
                        record.append(cc)
                        track.add(cc)
            step += 1
        return -1

    def exchange_pos(self, record):
        pos_dict = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        index = record.index("0")
        res = []
        for i in pos_dict[index]:
            a = list(record)
            a[index], a[i] = a[i], a[index]
            res.append("".join(a))
        return res

s = Solution()
s.slidingPuzzle([[4,1,2],[5,0,3]])