class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        self.solve(0, subset, nums, result)

        return result

    def solve(self, index: int, subset: List[int], nums: List[int], result: List[List[int]]):

        if index >= len(nums):
            result.append(subset.copy())
            return

        # Take
        subset.append(nums[index])
        self.solve(index + 1, subset, nums, result)

        # Backtrack
        subset.pop()

        # Don't take
        self.solve(index + 1, subset, nums, result)