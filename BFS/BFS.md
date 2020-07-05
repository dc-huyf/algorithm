```buildoutcfg
# python版模板套路： start 到终点 target 的最近距离
def solve(start, target):
    # 回头路原则
    track = set()
    track.add('start')
    record = deque([(start)])
    step = 0

    while record:
        # 遍历当前队列
        lens = len(record)
        for q in range(lens):
            cur = record.popleft()
            if cur == target:
                return step
            # 加入当前节点的所有相邻节点
            for obj in cur.choices:
                if obj not in track:
                    record.append(obj)
                    track.add(obj)
        # 这一层级的更新完毕，再加一步
        step += 1

```