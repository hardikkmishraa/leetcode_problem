class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")#agr sb minus hua to usko handle krne ke liye, min value sbse
        total=0 #isme temp store karenge aur capre karnege amxi se , agr bda hua to maxi me update karnege

        for i in range(0,n):
            total=total+nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi
#kadane algo-> total me kabi bhi -ve value aata h to usko 0 pr reset krdenge har baar aur sife +ve value to hi add kakre maxi me store karenge ...

