class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ready = []
        min_word = min(strs)
        for i in range(len(min_word)):
            if strs[0][i] == strs[1][i] and strs[1][i] == strs[2][i] and strs[0][i] == strs[2][i]:
                ready.append(min_word[i])
        return "" if not ready else "".join(ready)


adj = Solution()
print(adj.longestCommonPrefix(["dog", "racecar", "car"]))