class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[-1]]
        idx = [len(temperatures) - 1]
        res = [0]
        i = len(temperatures) - 2
        while i >= 0:
            flag = True
            while flag:
                if len(stack) > 0:
                    val = stack.pop()
                    index = idx.pop()
                    if temperatures[i] < val:
                        res.append(index-i)
                        stack.append(val)
                        idx.append(index)
                        stack.append(temperatures[i])
                        idx.append(i)
                        break
                else:
                    res.append(0)
                    flag = False
                    stack.append(temperatures[i])
                    idx.append(i)
            i -= 1
        return list(reversed(res))