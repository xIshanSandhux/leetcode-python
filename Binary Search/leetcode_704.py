from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        end = len(nums)-1
        middle = 0

        while first <= end:
            middle = int((end+first)//2)
            print(nums[middle])
            if target>nums[middle]:
                first = middle+1
                print(nums[middle])
            elif target< nums[middle]:
                end = middle-1
                print(nums[middle])
            elif target==nums[middle]:
                print(nums[middle])
                return middle
        return -1
            
solution = Solution()

# Test cases
# print(solution.characterReplacement("AABABBA",1))
print(solution.search([-1,0,3,5,9,12],2))

