class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #optimal soln:
        n1=len(nums)
        res=[0]*n1
        p,n=0,1 #p->positive index, n-> negative index
        for i in range(0,n1):
            if nums[i]>=0:
                res[p]=nums[i]
                p+=2
            else:
                res[n]=nums[i]
                n+=2
        return  res