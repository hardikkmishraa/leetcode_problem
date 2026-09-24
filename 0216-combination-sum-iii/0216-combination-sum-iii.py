class Solution:
    def func(self,n,Sum,curr,nums,k,ans):
        if Sum==n and len(nums)==k:
            ans.append(list(nums))
        if Sum>n or len(nums)>k:
            return
        for i in range(curr,10):
            nums.append(i)
            self.func(n,Sum+i,i+1,nums,k,ans)
            nums.pop()

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans=[]
        nums=[]
        self.func(n,0,1,nums,k,ans)
        return ans
