class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n/=3
        return n==1

obt = Solution()
print(obt.isPowerOfTwo(21))
