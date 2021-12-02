class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<6:
            return False
        lopp = round(num/2)//1+1
        sum=0
        for i in range(1,lopp):
            if num%i == 0:
                sum+=i
        return sum==num



obj = Solution()
print(obj.checkPerfectNumber(56))