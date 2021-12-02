class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        nm = [6,28,496,8128, 33550336]
        return num in nm


obj = Solution()
print(obj.checkPerfectNumber(6))