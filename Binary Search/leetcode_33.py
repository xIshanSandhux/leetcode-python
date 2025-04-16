from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        pivot_index = (self.findPivot(nums) - 1 + len(nums)) % len(nums)
        print(pivot_index)
        first = 0
        r = -1
        last = len(nums)-1
        
        if target >= nums[0]:
            # target is in left sorted half
            first = 0
            last = pivot_index
        else:
            # target is in right sorted half
            first = (pivot_index + 1) % len(nums)
            last = len(nums) - 1

        while first<=last:
            middle = (first+last)//2
            print(middle)
            if nums[middle]>target:
                last = middle-1
            elif nums[middle]<target:
                first = middle+1
            elif nums[middle]==target:
                # print("hello")
                return middle
        return r
    
    def findPivot(self,nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low  # low is now the index of the **smallest** element (rotation point)


    
    
    
solution = Solution()

# print(solution.search([4,5,6,7,0,1,2],3)) #7
# print(solution.search([6,7,8,1,2,3,4,5],0)) #8
# print(solution.search([5,6,7,8,9,1,2,3,4],0)) #9
# print(solution.search([1,2,3,4,5,6],0))#6
# print(solution.search([3, 1],0))#3
# print(solution.search([5, 1, 3],0))#5
print(solution.search([1, 3],1))#3
# print(solution.search([6,7,1,2,3,4,5],0))#7
# print(solution.search([6,7,8,9,1,2,3,4,5],0))#7