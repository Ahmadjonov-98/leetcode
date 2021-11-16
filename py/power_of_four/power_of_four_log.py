from collections import Counter
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bin_num = bin(n)[2:]
        counts = Counter(bin_num)
        if n > 0 and counts['1'] == 1 and counts['0'] % 2 == 0:
            return True
        return False

obt = Solution()
print(obt.isPowerOfFour(16777216))
