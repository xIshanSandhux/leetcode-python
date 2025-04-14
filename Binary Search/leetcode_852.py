from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        first = 0
        last = len(arr) - 1

        while first < last:
            middle = (first + last) // 2
            if arr[middle] < arr[middle + 1]:
                first = middle + 1  # move right
            else:
                last = middle  # move left or stay

        return first  # or return last, both point to the peak index

    
solution = Solution()

# Test cases
# print(solution.characterReplacement("AABABBA",1))
print(solution.peakIndexInMountainArray([0,1,0]))
print(solution.peakIndexInMountainArray([0,2,1,0]))
print(solution.peakIndexInMountainArray([0,5,10,2]))
print(solution.peakIndexInMountainArray([3,4,5,1]))
