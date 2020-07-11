class Solution:
    def decodeString(self, s: str) -> str:
        '''
        利用栈
        '''
        if len(s) <= 3:
            return s

        result = []
        for ss in s:
            # 字母 / [
            if ss != ']':
                result.append(ss)
            elif ss == ']':
                # 获取【】内的字符串
                c = ""
                while result[-1] != '[':
                    c += result.pop()
                c = c[::-1]
                # 获取数字
                num = ''
                result.pop() #去掉【
                while len(result) >= 1 and (ord(result[-1]) >= ord("0") and ord(result[-1]) <= ord("9")):
                    num += result.pop()
                num = int(num[::-1])
                result.extend(list(c * num))
        return "".join(result)

s = Solution()
s.decodeString("3[a2[c]]")





