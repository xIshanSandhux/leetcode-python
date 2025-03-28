from typing import List


class Solution:

    # this is the same as using nested for loops. just made it harder for me
    # o(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # pointer1 = nums[0]
        # pointer2 = nums[1]
        pointer1 = 0
        pointer2 = 1

        while pointer1!= (len(nums)-1):

            if pointer2 == (len(nums)) and len(nums)>2:
                pointer1+=1
                pointer2 = pointer1+1
            
            num1 = nums[pointer1]
            num2 = nums[pointer2]

            
            sum = num1+num2
            if sum==target:
                return [pointer1,pointer2]
            else:
                pointer2+=1


    # the main thing is basically to use the difference between the current number in the list and the target
    # because there is only 1 unique solution so there is only 1 index which is going to be the other part of the difference
    # o(n)
    def twoSumOptimized(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in dict1:
                return [i, dict1.get(diff)]
            
            dict1[num] = i
            

            
solution = Solution()

# Test cases
print(solution.twoSumOptimized([2,7,11,15],9))  # [0,1]
print(solution.twoSumOptimized([3,2,4],6))  # [1,2]
print(solution.twoSumOptimized([3,3],6))  # [0,1]