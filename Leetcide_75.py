from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=[]
        ones=[]
        twos=[]

        for i in nums:
            if i==0:
                zeros.append(i)
            elif i==1:
                ones.append(i)
            elif i==2:
                twos.append(i)
        
        combined1=  zeros+ones
        final_combined = combined1+twos
        print(final_combined)

        for i in range(len(nums)):
            nums[i] = final_combined[i]
        
        print(nums, "nums lists")

solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
# print(solution.moveZeroes([1,0,1])) 
print(solution.sortColors([2,0,2,1,1,0])) # [4,2,4,3,5,1,0,0,0,0]

