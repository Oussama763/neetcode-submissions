class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        L = Counter(s)
        for i in range(len(t)):
            if L[t[i]] == 0:
                return False
            L[t[i]] -= 1
        return True