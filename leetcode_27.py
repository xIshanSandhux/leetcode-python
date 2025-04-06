from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_pointer =0

        for fast in range(len(nums)):
            if nums[val_pointer] == val and nums[fast] != val:
                print(nums)
                temp = nums[val_pointer]
                nums[val_pointer]= nums[fast]
                nums[fast] = temp
                val_pointer+=1
                print(val_pointer,"hello")
            elif nums[val_pointer] != nums[fast]:
                val_pointer+=1
            elif nums[val_pointer]==nums[fast] and nums[val_pointer]!=val:
                val_pointer+=1
        print(nums)

        return val_pointer
    
solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
print(solution.removeElement([2,2,3],3)) 
# print(solution.removeElement([0,1,2,2,3,0,4,2],2)) # [4,2,4,3,5,1,0,0,0,0]

