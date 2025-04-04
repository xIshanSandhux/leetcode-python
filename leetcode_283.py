from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0
        pointer2 = 1

        # for i in range(len(nums)):
        #     print(i)
        #     if nums[pointer1] == 0 and len(nums)>pointer2 and nums[pointer2]!=0:
        #         print ("helo")
        #         temp = nums[pointer1]
        #         nums[pointer1] = nums[pointer2]
        #         nums[pointer2] = temp
        #         pointer1 +=1
        #         pointer2 +=1   
        #     elif nums[pointer1]==0 and len(nums)>pointer2 and nums[pointer2]==0:
        #         print(pointer2)
        #         pointer2+=1
        #     elif nums[pointer1] != 0 and len(nums)>pointer2 and nums[pointer2]==0:
        #         # temp = nums[pointer1]
        #         # nums[pointer1] = nums[pointer2]
        #         # nums[pointer2] = temp
        #         # pointer1 +=1
        #         # pointer2 +=1
        #         print("hello2")
        #         pointer1+=1
        for i in range(len(nums)):
            if nums[i]!=0 and nums[pointer1]==0:
                temp = nums[pointer1]
                nums[pointer1] = nums[i]
                nums[i] = temp
            
            if nums[pointer1]!=0:
                pointer1+=1

        print(nums)

solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
# print(solution.moveZeroes([1,0,1])) 
print(solution.moveZeroes([4,2,4,0,0,3,0,5,1,0])) # [4,2,4,3,5,1,0,0,0,0]

