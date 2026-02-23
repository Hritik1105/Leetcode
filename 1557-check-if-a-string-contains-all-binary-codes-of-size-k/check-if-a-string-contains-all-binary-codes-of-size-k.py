class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num=set()
        for i in range(len(s)-k+1):
            num.add(s[i:i+k])
        return len(num)==2**k
        