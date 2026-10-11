class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxi=0
        n=len(nums)
        r=0
        l=0
        zeros=0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
           
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi