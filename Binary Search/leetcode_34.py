from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
       if target not in nums:
           return [-1,-1]
       
       l = [solution.searchRangefirst(nums,target),solution.searchRangelast(nums,target)]
       return l
    
    def searchRangefirst(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1

        if nums[0]==target:
            return 0

        while first<=last:
            middle = (first+last)//2
            if nums[middle]<target:
                first = middle+1
                # print(nums[first])
                if nums[first]==target:
                    # print(l)
                    return first
            elif nums[middle]>target:
                last = middle-1
            else:
               last = middle-1
 
    
    def searchRangelast(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        
        if nums[last]==target:
            return last

        while first<=last:
            middle = (first+last)//2
            if nums[middle]<target:
                first = middle+1 
            elif nums[middle]>target:
                last = middle-1
                if nums[last]==target:
                    return last
            else:
               first = middle+1

solution =Solution()


print(solution.searchRange([5,7,7,8,8,10],8))
print(solution.searchRange([0, 1, 2, 3, 4, 5, 9, 9],9))
print(solution.searchRange([1, 1, 2, 3, 4, 5, 6, 6],1))
print(solution.searchRange([1, 2, 3, 4, 5, 6, 7],4))
print(solution.searchRange([1, 2, 3, 3, 3, 4, 5],3))
print(solution.searchRange([1, 2, 3, 3, 3, 4, 5, 9, 9, 9, 9, 10],9))
print(solution.searchRange([2, 2, 2, 2, 2],3))



class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirst(nums, target), self.findLast(nums, target)]

    def findFirst(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    index = mid
                right = mid - 1  # Move left to find earlier occurrence

        return index

    def findLast(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    index = mid
                left = mid + 1  # Move right to find later occurrence

        return index

        