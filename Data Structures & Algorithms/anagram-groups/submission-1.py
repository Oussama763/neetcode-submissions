class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in visited:
                visited[sorted_str] = [strs[i]]
            else:
                visited[sorted_str].append(strs[i])
        return [visited[s] for s in visited]
                    
