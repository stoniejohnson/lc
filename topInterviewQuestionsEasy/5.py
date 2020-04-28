from typing import List

class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            
            a = 0
            for i in nums:
                a ^= i
            return a



s = Solution()
s.singleNumber([1,2,2])
