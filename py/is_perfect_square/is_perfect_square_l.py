class Solution:                                 # 4, 9, 16,25,36, 
    def isPerfectSquare(self, num: int) -> bool:# 1+3+5+7+9+11+13,
        x=num**0.5
        print(x//1)
        return (x==num**0.5)
    
obt = Solution()
print(obt.isPerfectSquare(225))