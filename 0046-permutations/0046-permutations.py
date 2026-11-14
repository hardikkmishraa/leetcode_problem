class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==1:
            return [nums]
        
        permutations=[]
        for i in range(len(nums)):
            current_num=nums[i]
            remaining_num=nums[:i]+nums[i+1:]

            remaining_permutations=self.permute(remaining_num)

            for p in remaining_permutations:
                permutations.append ([current_num]+p)
        return permutations
