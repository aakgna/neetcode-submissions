from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            alphabet = [0]*26
            for char in word:
                alphabet[ord(char) - 97] += 1
            alpha = tuple(alphabet)
            groups[alpha].append(word)
        return groups.values()