from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))
        values = [x for x, _ in arr]

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # Find connected components
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # Farthest position reachable in one edge to the right
        right = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1
            right[i] = r

        # Farthest position reachable in one edge to the left
        left = [0] * n
        l = 0
        for i in range(n):
            while values[i] - values[l] > maxDiff:
                l += 1
            left[i] = l

        LOG = n.bit_length()

        upR = [right]
        upL = [left]

        for _ in range(1, LOG):
            prev = upR[-1]
            upR.append([prev[prev[i]] for i in range(n)])

            prev = upL[-1]
            upL.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu < pv:
                cur = pu
                steps = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = upR[k][cur]
                    if nxt < pv:
                        cur = nxt
                        steps += 1 << k
                ans.append(steps + 1)
            else:
                cur = pu
                steps = 0
                for k in range(LOG - 1, -1, -1):
                    nxt = upL[k][cur]
                    if nxt > pv:
                        cur = nxt
                        steps += 1 << k
                ans.append(steps + 1)

        return ans