'''
BF
'''
def BF(s1, s2):
    if not s2 or not s1:
        return -1
    for i in range(len(s1)-len(s2)+1):
        if s1[i: i+len(s2)] != s2:
            continue
        else:
            return i
    return -1

'''
KMP
'''
def get_start_end(s):
    i, j = 1, 0
    result_list=[0] * len(s)
    while i < len(s):
        if j == 0 and s[j] != s[i]:
            result_list[i] = 0
            i += 1
        elif s[j] != s[i] and j != 0:
            j = result_list[j-1]
        elif s[j] == s[i]:
            result_list[i] = j+1
            j = j+1
            i = i+1
    return result_list

def KMP(s, p):
    s_len, p_len = len(s), len(p)
    i, j = 0, 0
    next = get_start_end(p)
    while i < s_len:
        if s[i] == p[j]:
            i += 1
            j += 1
            if j >= p_len:
                return i - p_len
        elif s[i] != p[j]:
            if j == 0:
                i += 1
            else:
                j = next[j]
    if i == s_len:
        return -1

'''
定长顺序存储
'''
class Solution:
    def __init__(self):
        self.max_len = 20
    def preprocess(self, s):
        return [len(s)] + list(s)
    def concat(self, s1, s2):
        s1 = self.preprocess(s1)
        s2 = self.preprocess(s2)
        res = ''
        if s1[0] + s2[0] <= self.max_len:
            for i in range(1, s1[0]+1):
                res += s1[i]
            for j in range(1, s2[0]+1):
                res += s2[j]
        elif s1[0] < self.max_len:
            for i in range(1, s1[0]+1):
                res += s1[i]
            for j in range(1, self.max_len-s1[0]+1):
                res += s2[j]
        else:
            for i in range(1, self.max_len+1):
                res += s1[i]
        return self.preprocess(res)
    def substrinf(self, s1, pos, length):
        res = ""
        s1 = self.preprocess(s1)
        if pos < 1 or pos > s1[0] or length < 0 or length > s1[0] - pos + 1:
            return False
        for i in range(1, length+1):
            res += s1[i]
        return self.preprocess(res)
    def subdelete(self, s1, pos, length):
        s1 = self.preprocess(s1)
        if pos < 1 or pos > s1[0] or length < 0:
            return False
        if pos + length - 1 >= s1[0]:
            return s1
        else:
            res = ""
            for i in range(1, pos):
                res += s1[i]
            for j in range(pos+length, s1[0]+1):
                res += s1[j]
            return self.preprocess(res)