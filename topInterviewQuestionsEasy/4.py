from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueValues = []
        for val in nums:
            if val not in uniqueValues:
                uniqueValues.append(val)
            else:
                return True
        return False

sol = Solution()

print(sol.containsDuplicate([1,2,3,4,5]))

print(sol.containsDuplicate([1,2,3,1]))
