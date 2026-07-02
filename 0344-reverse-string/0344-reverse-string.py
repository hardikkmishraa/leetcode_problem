class Solution:

    def fucn(self,arr,i,j):
        if i>=j:
            return
        arr[i],arr[j]=arr[j],arr[i]
        self.fucn(arr,i+1,j-1)
    def reverseString(self, s: List[str]) -> None:
        self.fucn(s,0,len(s)-1)
        """
        Do not return anything, modify s in-place instead.
        """
    
    