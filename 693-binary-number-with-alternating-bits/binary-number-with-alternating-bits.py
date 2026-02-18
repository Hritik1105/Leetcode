class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev=-1
        while n!=0:
            bit=n%2
            if bit==prev:
                return False
            prev=bit
            n//=2
        return True