class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr = [0 for _ in range(31)]
        for char in range(len(s)):
            arr[97-ord(s[char])] +=1 
        for char in range(len(s)): 
            arr[97-ord(t[char])] -=1
            if arr[97-ord(t[char])]<0:
                return False
        

abt = Solution()
abt.isAnagram("rat", "cat")