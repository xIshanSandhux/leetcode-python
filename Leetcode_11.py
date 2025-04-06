from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        while right>left:
            # print(right)
            area = (min(height[left],height[right]))*(right-left)
            if area<0:
                area = -(area)
            if area>max_area:
                max_area=area

            if height[left]>height[right]:
                right-=1
            elif height[right]>height[left]:
                left+=1
            elif height[left]==height[right]:
                right-=1
        return max_area
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7])) 
print(solution.maxArea([8,7,2,1])) 

