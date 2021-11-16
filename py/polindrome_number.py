class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

obt = Solution()
print(obt.isPalindrome(2772))
            