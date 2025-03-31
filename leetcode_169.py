from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        threshold = int((len(nums)/2))
        majority=0

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            elif nums[i] in dict1:
                num = dict1.get(nums[i])
                dict1[nums[i]] = num+1
        
        for k,v in dict1.items():
            if v>threshold:
                majority = k
        return majority
    
solution = Solution()

# Test cases
print(solution.majorityElement([3,2,3]))  # [1,2]
print(solution.majorityElement([2,2,1,1,1,2,2]))  # [1]