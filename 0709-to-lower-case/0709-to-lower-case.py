class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        for char in s:
            if 'A'<=char<='Z':
                res+= chr(ord(char)+32)
            else:
                res+=char
        return res