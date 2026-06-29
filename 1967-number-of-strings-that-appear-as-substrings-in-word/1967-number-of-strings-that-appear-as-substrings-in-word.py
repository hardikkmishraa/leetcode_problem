class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0

        for n in patterns:
            if n in word:
                count+=1
        return count
