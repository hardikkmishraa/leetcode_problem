class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # All elements already have even parity
        if min_odd == float('inf'):
            return True

        # All elements already have odd parity
        if min_even == float('inf'):
            return True

        # Make every even element odd using the smallest odd element
        return min_odd < min_even