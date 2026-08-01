class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #brute force
        pos=[x for x in nums if x>=0]
        neg=[x for x in nums if x<=0]

        for i in range(0,len(pos)):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
        return nums