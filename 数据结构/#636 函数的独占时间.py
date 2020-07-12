'''
吐槽：leetcode-cn的翻译绝了
'''

class Solution:
    def exclusiveTime(self, n: int, logs):
        if n == 0 or len(logs) <= 1:
            return []
        time_dict = {}
        # 每轮需要更新
        a, b, c = logs[0].split(":")
        states = [int(a)]
        for idx in range(1, len(logs)):
            func, state, time = logs[idx].split(":")
            if state == 'start':
                if len(states) >= 1:
                    time_dict[states[-1]] = time_dict.get(states[-1], 0) + int(time) - int(c) - (b == 'end')
                states.append(int(func))
            else:
                if b == 'start':
                    time_dict[int(func)] = time_dict.get(int(func), 0) + int(time) - int(c) + 1
                else:
                    time_dict[states[-1]] = time_dict.get(states[-1]) + int(time) - int(c)
                states.pop()
            a, b, c = func, state, time
        return list(time_dict.values())