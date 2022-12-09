class Solution(object):
    def __init__(self):
        self.res = True
        self.visited = None
        self.color = None

    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        '''
        0. 本质上为判断是否为二分图
        1. dislike并非邻接表的形式，需要先做转化
        '''
        graph = self.transGraph(n, dislikes)
        self.visited = [False for _ in range(n)]
        self.color = [False for _ in range(n)]
        for idx in range(n):
            if not self.visited[idx]:
                self.traverse(graph, idx)
        return self.res

    def traverse(self, graph, curr):
        '''考虑使用DFS'''
        if not self.res: return
        self.visited[curr] = True
        for idx in graph[curr]:
            if not self.visited[idx]:
                self.color[idx] = not self.color[curr]
                self.traverse(graph, idx)
            else:
                if self.color[idx] == self.color[curr]:
                    self.res = False
                    return

    def transGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        return graph

if __name__ == "__main__":
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    s = Solution()
    res = s.possibleBipartition(n, dislikes)
    print(res)
