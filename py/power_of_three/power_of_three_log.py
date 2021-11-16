from math import log, perm
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: 
            return False
        r = log(n)/log(3)
        return (abs(round(r) - r) < 10**-10)


obt = Solution()
print(obt.isPowerOfThree(16423203268260658146231467800709255289))
