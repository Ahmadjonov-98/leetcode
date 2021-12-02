class Solution:    
    def checkPerfectNumber(self, num: int) -> bool:
        result = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                result += i + num / i
        return result == num if num > 1 else False



obj = Solution()
print(obj.checkPerfectNumber(6))