class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        char_count={}
        for char in s:
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char]=1
        
        for char in char_count:
            if char_count[char]<k:
                max_len=0
                for part in s.split(char):
                    max_len=max(max_len, self.longestSubstring(part,k))
                return max_len
        return len(s)