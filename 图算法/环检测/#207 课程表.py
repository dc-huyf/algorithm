"""
1. 尝试分别用DFS、BFS实现图遍历，主要学习下拓扑排序
2. 目标：找闭环（课程依赖）
"""
from typing import List

class SolutionDFS:
    def __init__(self):
        self.is_circle = False
        self.visited = None
        self.graph = None

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = self.transGraph(numCourses, prerequisites)
        self.visited = [False for _ in range(numCourses)]
        on_path = [False for _ in range(numCourses)]
        for idx in range(numCourses):
            self.traverse(idx, on_path)
        return not self.is_circle

    def traverse(self, curr, on_path):
        """结束条件是：判断出现闭环 -> on_path = True（并非visited=True）
        """
        if on_path[curr]:
            self.is_circle = True
        if self.visited[curr] or self.is_circle:
            return
        self.visited[curr] = True
        on_path[curr] = True
        for idx in self.graph[curr]:
            self.traverse(idx, on_path)
        on_path[curr] = False

    def transGraph(self, n, input_list):
        graph = [[] for _ in range(n)]
        for a, b in input_list:
            graph[a].append(b)  # 依赖方向应该不重要
        return graph


"""
！！若图中不存在多个连通子图，并且不存在环，则与多叉树遍历一致（个人理解），也不需要出入度的概念
引入出入度，每次选取入度=0的加入队列
"""

class SolutionBFS:
    def __init__(self):
        self.graph = None
        self.indegree = None

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = self.transGraph(numCourses, prerequisites)
        # 构建初入度
        self.indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            # 方向与构建图一致
            self.indegree[b] += 1 # 入度

        # 入度为0的均加入队列
        queue_list = []
        count = 0
        for idx in range(numCourses):
            if self.indegree[idx] == 0:
                queue_list.append(idx)

        while len(queue_list) > 0:
            root = queue_list.pop(0)
            count += 1
            for idx in self.graph[root]:
                self.indegree[idx] -= 1
                if self.indegree[idx] == 0:
                    queue_list.append(idx)
        return count == numCourses

    def transGraph(self, n, input_list):
        graph = [[] for _ in range(n)]
        for a, b in input_list:
            graph[a].append(b)  # 依赖方向应该不重要
        return graph


if __name__ == "__main__":
    s = SolutionBFS()
    numCourses = 5
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    res = s.canFinish(numCourses, prerequisites)
    print(res)
