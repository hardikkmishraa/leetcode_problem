class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        pair_xor = set()

        for i in range(n):
            ai = nums[i]
            for j in range(i + 1, n):
                pair_xor.add(ai ^ nums[j])

        ans = set(nums)

        for x in pair_xor:
            for v in nums:
                ans.add(x ^ v)

        return len(ans)