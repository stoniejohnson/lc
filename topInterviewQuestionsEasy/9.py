from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return([required[target - nums[i]], i])
            else:
                required[nums[i]] = i

s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))
