from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]

        sorter_list = sorted(nums)
        
        return sorter_list
    
solution = Solution()

# Test cases
print(solution.sortedSquares([-4,-1,0,3,10]))  # [1]
print(solution.sortedSquares([-7,-3,2,3,11]))
