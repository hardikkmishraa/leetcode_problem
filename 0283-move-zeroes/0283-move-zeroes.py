class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        if len(nums)==0: #edge case
            return
        

        i=0
        while i<len(nums):
            if nums[i]==0:
                break
            i+=1
        if i==len(nums): #edge case
            return
        
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1