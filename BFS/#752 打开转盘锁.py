from typing import List


class SolutionBFS:
    def __init__(self):
        self.res = 0

    def plus_str(self, s):
        if s == "9":
            return "0"
        else:
            return str(int(s) + 1)

    def sub_str(self, s):
        if s == "0":
            return "9"
        else:
            return str(int(s) - 1)

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" == target: return 0
        queue_list = ["0000"]
        history = set("0000")
        while len(queue_list) > 0:
            lens = len(queue_list)
            for i in range(lens):
                curr = queue_list.pop(0)
                if curr in deadends: continue
                if curr == target: return self.res
                for i in range(4):
                    tmp_plus = curr[:i] + self.plus_str(curr[i]) + curr[i + 1:]
                    tmp_sub = curr[:i] + self.sub_str(curr[i]) + curr[i + 1:]
                    if tmp_plus not in history:
                        queue_list.append(tmp_plus)
                        history.add(tmp_plus)
                    if tmp_sub not in history:
                        queue_list.append(tmp_sub)
                        history.add(tmp_sub)
            self.res += 1
        return -1


if __name__ == "__main__":
    s = SolutionBFS()
    res = s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
    print(res)
