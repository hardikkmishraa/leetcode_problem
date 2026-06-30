class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(ch.lower() for ch in s if ch.isalnum())

        n=len(s)
        l=0
        r=n-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True