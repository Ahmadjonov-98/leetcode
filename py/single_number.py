class Solution:
    def singleNumber(self, nums) -> int:
        n=len(nums)
        r=nums[0]
        for i in range(1,n):
            r ^= nums[i] 
        return r
abt  = Solution()
print(abt.singleNumber([3,4,5,3,4]))
