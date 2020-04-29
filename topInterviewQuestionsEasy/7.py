from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strN = ''
        for val in digits:
            strN = strN + str(val)
        return [int(x) for x in str(int(strN)+1)]

sol = Solution()

print(sol.plusOne([1,2,3]))
