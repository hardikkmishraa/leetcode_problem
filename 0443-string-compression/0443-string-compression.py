class Solution:
    def compress(self, chars: list[str]) -> int:
        s=''.join(chars)
        compressed_res=[]
        count=1

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                compressed_res.append(s[i-1])
                if count > 1:
                    compressed_res.extend(str(count))
                count = 1
        compressed_res.append(s[-1])
        if count > 1:
            compressed_res.extend(str(count))
        chars[:] = compressed_res
        return len(chars)