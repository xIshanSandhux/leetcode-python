from typing import List


class Solution:
    def removeDuplicatesbruteforce(self, nums: List[int]) -> int:
        seen = sorted(set(nums))
        counter =0
        print(seen)

        for i,val in enumerate(seen):
            print(i)
            nums[i] = val

        print(nums)

        return len(seen)
    
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        # Slow pointer
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp

        print(nums)
        return i+1
    
solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
print(solution.removeDuplicates([0, 1, 2, 3, 4, 0, 2, 1, 3, 1])) 
print(solution.removeDuplicates([1,1,2])) # [4,2,4,3,5,1,0,0,0,0]

