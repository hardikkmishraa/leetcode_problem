class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            rem=target-nums[i]
            if rem in hash_map:
                return [hash_map[rem],i]
            hash_map[nums[i]]=i

