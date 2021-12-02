class Solution:
    def reverseString(self, s) -> None:
        size = len(s)
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]


abt = Solution()
print(abt.reverseString(["h","e","l","l","o"]))