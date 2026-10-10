class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        stack=[]
        res=[-1]*n
        

        for i in range(2*n-1,-1,-1):
            while len(stack)!=0 and nums[stack[-1]]<=nums[i%n]:
                stack.pop()
            if i<n:
                if len(stack)!=0:
                    res[i]=nums[stack[-1]]
            stack.append(i%n)
        return res        