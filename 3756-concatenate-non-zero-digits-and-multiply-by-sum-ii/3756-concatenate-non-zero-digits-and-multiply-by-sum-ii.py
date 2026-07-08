from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digit = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(int(ch))

        m = len(digit)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix sum of digits
        preSum = [0] * (m + 1)
        for i in range(m):
            preSum[i + 1] = preSum[i] + digit[i]

        # prefix number
        preValue = [0] * (m + 1)
        for i in range(m):
            preValue[i + 1] = (preValue[i] * 10 + digit[i]) % MOD

        ans = []

        for l, r in queries:

            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            value = (
                preValue[R + 1]
                - preValue[L] * pow10[length]
            ) % MOD

            digitSum = preSum[R + 1] - preSum[L]

            ans.append((value * digitSum) % MOD)

        return ans