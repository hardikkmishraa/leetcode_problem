class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for char in s:
            if char.isalnum():
                new_s+=char.lower()
        
        i=0
        j=len(new_s)-1

        while i<j:
            if new_s[i]!=new_s[j]:
                return False
            i+=1
            j-=1
        return True
