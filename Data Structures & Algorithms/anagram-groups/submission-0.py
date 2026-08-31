class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        for i in range(0, len(strs)):
            l = ''.join(sorted(strs[i]))
            if l in temp:
                temp[l].append(strs[i])
            else:
                temp[l] = [strs[i]]
        return temp.values()