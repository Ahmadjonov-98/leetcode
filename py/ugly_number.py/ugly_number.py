class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        while n%2==0 and n!=1:
            n=int(n/2)
            if n==1:
                return True
        while n%3==0 and n!=1:
            n=int(n/3)
            if n==1:
                return True
        while n%5==0 and n!=1:
            n=int(n/5)
            if n==1:
                return True
        return False

obt = Solution()
print(obt.isUgly(12))
            