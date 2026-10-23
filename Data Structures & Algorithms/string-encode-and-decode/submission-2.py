class Solution:

    def encode(self, strs: List[str]) -> str:
        bij_list = []

        for i in range(len(strs)):
            bij_list.append(str(len(strs[i])).zfill(3))
            bij_list.append(strs[i])
        return "".join(bij_list)

    def decode(self, s: str) -> List[str]:
        k = 0
        strs = []
        while k < len(s):
            strs.append(s[k + 3: k + 3 + int(s[k:k+3])])
            k += 3 + int(s[k:k+3])
        return strs