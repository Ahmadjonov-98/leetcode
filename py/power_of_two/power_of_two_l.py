from math import log, perm
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: 
            return False
        r = log(n)/log(2)
        return (abs(round(r) - r) < 10**-10)


obt = Solution()
print(obt.isPowerOfTwo(2048))
