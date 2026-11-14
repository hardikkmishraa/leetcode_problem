class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val={"I":1,
        "V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        total=0
        prev_val=0
        for char in reversed(s):
            curr_value=roman_val[char]
            if curr_value<prev_val:
                total-=curr_value
            else:
                total+=curr_value
            prev_val=curr_value
        return total