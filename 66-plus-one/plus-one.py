class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=len(digits)
        y=""
        for i in range(x):
            y+=str(digits[i])
        r=int(y)+1
        payal=[int(num) for num in str(r)]
        return payal
        



        