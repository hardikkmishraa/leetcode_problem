class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float("inf")

        while low <= high:
            mid = (low + high) // 2            # Find the middle index

            # If left half is sorted
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])  # Update minimum
                low = mid + 1                      # Search in the right half
            else:                                  # Right half is sorted
                minimum = min(minimum, nums[mid])  # Update minimum
                high = mid - 1                     # Search in the left half

        return minimum                             # Return the smallest element