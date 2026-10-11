class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        left_sum, right_sum=0,0
        for i in range(0,k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_inx=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_inx]
            maxi=max(maxi,right_sum+left_sum)
            right_inx-=1
        return maxi