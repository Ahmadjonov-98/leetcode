class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
        summ=numbers[s[-1]]
        
        for i in range(len(s))[-2::-1]:
            if numbers[s[i+1]]>numbers[s[i]]:
                summ -= numbers[s[i]]
            else:
                summ += numbers[s[i]]
        return summ

obt = Solution()
print(obt.romanToInt("LVIII"))
            