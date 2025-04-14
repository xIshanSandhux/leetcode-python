from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        middle = 0
        index = 0

        while first<last:
            middle = (first+last)//2
            print(middle,"middle")
            print(first,"first")
            print(last,"last")
            if target>nums[middle]:
                first = middle+1
                print(nums[middle])
            elif target< nums[middle]:
                last = middle-1
                print(nums[middle])
            elif target==nums[middle]:
                print(nums[middle])
                return middle
        index = middle
        return index
    
solution = Solution()

# Test cases
# print(solution.characterReplacement("AABABBA",1))
print(solution.searchInsert([1,3,5,6],5))

