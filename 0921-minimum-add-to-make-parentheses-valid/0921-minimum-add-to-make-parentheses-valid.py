class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        count=0
        for i in s:
            if i=='(':
                st.append(i)
            elif i==')' and len(st)==0:
                count+=1
            elif i==')':
                st.pop()
        x=len(st)+count
        return x
        