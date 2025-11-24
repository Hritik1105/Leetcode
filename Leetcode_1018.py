# Binary Prefix Divisible by 5
# LeetCode Problem 1018
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        x = 0
        for v in nums:
            x = (x << 1 | v) % 5
            ans.append(x == 0)
        return ans
# Time Complexity: O(n)
# Space Complexity: O(1)