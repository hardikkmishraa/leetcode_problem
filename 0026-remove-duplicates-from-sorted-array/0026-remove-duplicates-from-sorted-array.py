class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        res=[]
        i=0
        j=i+1
        n=len(nums)

        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
                
        
        