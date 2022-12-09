class Solution(object):
    def __init__(self):
        self.res = True
        self.visited = None
        self.color = None

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        '''本题下二分图的几个特点：1. 可能不连通；2. 从任意节点出发，都不会有颜色冲突
        核心目标：不论从哪个节点开始，都能够"走到底"，尽管可能无法全部遍历，但不会出现颜色冲突
        '''
        self.visited = [False] * len(graph) # 记录当前已到访节点
        self.color = [False] * len(graph) # 记录颜色
        # 有可能不连通，需要每个节点依次作为初始节点遍历
        for i in range(len(graph)):
            # 如果当前节点已经被到访过，则不必开始，避免陷入闭环
            if self.visited[i]: continue
            self.traverse(graph, i)
        return self.res

    def traverse(self, graph, curr):
        # 确定是非二分图，则直接返回
        if not self.res: return
        self.visited[curr] = True
        for idx in graph[curr]:
            # 确定子节点尚未到访
            if not self.visited[idx]:
                self.color[idx] = not self.color[curr]
                self.traverse(graph, idx)
            else: # 若当前节点到访过，则检查颜色是否冲突
                if self.color[idx] == self.color[curr]:
                    self.res = False
                    return

class SolutionBFS(object):
    def __init__(self):
        self.res = True
        self.visited = None
        self.color = None

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        '''BFS解法：与DFS一条道走到黑不同，BFS为逐层遍历
        '''
        self.visited = [False] * len(graph)  # 记录当前已到访节点
        self.color = [False] * len(graph)  # 记录颜色
        # 有可能不连通，需要每个节点依次作为初始节点遍历
        for i in range(len(graph)):
            # 如果当前节点已经被到访过，则不必开始，避免陷入闭环
            if self.visited[i]: continue
            self.traverse(graph, i)
        return self.res

    def traverse(self, graph, curr):
        # 定义队列,并将当前节点加进去
        queue_list = [curr]
        self.visited[curr] = True

        while len(queue_list) > 0 & self.res:
            root = queue_list.pop(0) # 获得头部节点
            for idx in graph[root]:
                # 确定子节点尚未到访
                if not self.visited[idx]:
                    self.color[idx] = not self.color[root]
                    self.visited[idx] = True
                    queue_list.append(idx)
                else:  # 若当前节点到访过，则检查颜色是否冲突
                    if self.color[idx] == self.color[root]:
                        self.res = False
                        return


if __name__ == "__main__":
    s = SolutionBFS()
    graph = [[1,3],[0,2],[1,3],[0,2]]
    res = s.isBipartite(graph)
    print(res)