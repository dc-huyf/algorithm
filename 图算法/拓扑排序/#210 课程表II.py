from typing import List

"""首先判断是否存在环，无环则可遍历
1.DFS实现图遍历
2.BFS实现图遍历:
"""
class SolutionDFS:
    def __init__(self):
        self.is_circle = False
        self.visited = None
        self.graph = None
        self.graph_track = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = self.transGraph(numCourses, prerequisites)
        self.visited = [False for _ in range(numCourses)]
        on_path = [False for _ in range(numCourses)]
        # 判断是否有环
        for idx in range(numCourses):
            self.traverse(idx, on_path)
        if self.is_circle:
            return []
        return self.graph_track

    def traverse(self, curr, on_path):
        if on_path[curr]:
            self.is_circle = True
        if self.visited[curr] or self.is_circle:
            return
        self.visited[curr] = True
        on_path[curr] = True
        for idx in self.graph[curr]:
            self.traverse(idx, on_path)
        on_path[curr] = False
        self.graph_track.append(curr)

    def transGraph(self, n, input_list):
        graph = [[] for _ in range(n)]
        for a, b in input_list:
            graph[a].append(b)  # 依赖方向：依赖项 -> 被依赖项
        return graph

class SolutionBFS:
    def __init__(self):
        self.graph = None
        self.indegree = None
        self.graph_track = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
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
            self.graph_track.append(root)

            for idx in self.graph[root]:
                self.indegree[idx] -= 1
                if self.indegree[idx] == 0:
                    queue_list.append(idx)
        if count != numCourses:
            return []

        return self.graph_track[::-1]

    def transGraph(self, n, input_list):
        graph = [[] for _ in range(n)]
        for a, b in input_list:
            graph[a].append(b)  # 依赖方向应该不重要
        return graph

if __name__ == "__main__":
    s = SolutionBFS()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    res = s.findOrder(numCourses, prerequisites)
    print(res)