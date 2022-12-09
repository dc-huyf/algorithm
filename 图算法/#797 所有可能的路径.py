class Solution(object):
    def __init__(self):
        self.res = []

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        '''graph为有向无环图，不存在回到同一节点的可能
        ⚠️：找出【所有】从节点 0 到节点 n-1 的路径并输出
        结束条件：1.错误路径:当前节点并非n-1，且无路可走；2.正确路径:当前节点为n-1
        '''
        self.traverse(graph, 0, [])
        return self.res

    def traverse(self, graph, curr, track):
        track.append(curr)
        if curr == len(graph) - 1:
            path = track[:]
            self.res.append(path)
        for node in graph[curr]:
            self.traverse(graph, node, track)
        track.pop()

if __name__ == "__main__":
    s = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    res = s.allPathsSourceTarget(graph)
    print(res)
