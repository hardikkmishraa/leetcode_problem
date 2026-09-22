class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        # Base case: Found a valid combination
        if target == 0:
            result.append(subset.copy())  # Add copy to preserve current state
            return
        
        # Try each candidate from current index onwards
        for i in range(index, len(candidates)):
            # Skip duplicates: if current element is same as previous and we're not
            # at the starting position, skip it to avoid duplicate combinations
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            
            # Early termination: if current candidate exceeds target,
            # all remaining candidates will also exceed (array is sorted)
            if candidates[i] > target:
                break
            
            # Include current candidate
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            
            # Backtrack: remove the candidate
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to enable duplicate skipping and early termination
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result