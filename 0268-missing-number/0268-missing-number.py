class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)

        sum1=n*((n+1))//2

        
        total=sum(nums)
        missing_num=sum1-total
        return missing_num
        