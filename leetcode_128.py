from typing import List


class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:

            if len(nums)==0:
                return 0
            
            seen = set()

            for i in nums:
                if i not in seen:
                    seen.add(i)
            
            # new_list = list(seen)
            longest=0

            for n in seen:

                if n-1 not in seen:
                    length =0
                    while (n+length) in seen:
                        length+=1
                    longest = max(length,longest)

            return longest
    

solution = Solution()

# Test cases
print(solution.longestConsecutive([1,0,1,2]))  # [1,2]
print(solution.longestConsecutive([2,2,1,1,1,2,2]))  # [1]
print(solution.longestConsecutive([100,4,200,1,3,2]))  # [1]