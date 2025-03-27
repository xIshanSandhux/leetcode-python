from typing import List

# Leetcode problem 217 Contains Duplicate
class Solution:
    # brute force method
    # simple 2 nested loop
    # run time O(n^2)
    def containsDuplicate(self, nums: List[int]) -> bool:
        b = False
        
        if len(nums)==0:
            return False
        
        for i in range(len(nums)):
            num1 = nums[i]
            for k in range(i+1, len(nums)):
                num2 = nums[k]
                if num1==num2:
                    b = True
                    return b
        return b
    
    # need to use hash for it, because the lookup time is O(1) cause it direcly checks if the specific value is in the hash table or not
    # use set() cause need to store unique values
    # and then it just looks up the value if its present or not.
    # run time of this solution is O(n)
    def containsDuplicateoptimized(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            num = nums[i]
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    

solution = Solution()

# Test cases
print(solution.containsDuplicateoptimized([1, 2, 3, 1]))  # True
print(solution.containsDuplicateoptimized([1, 2, 3, 4, 5, 7]))  # False
print(solution.containsDuplicateoptimized([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True