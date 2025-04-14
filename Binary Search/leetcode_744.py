from typing import List


class Solution:

    # O(n) time complexity
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        smallest = letters[0]

        for i in letters:
            if i> target:
                smallest = i
                return smallest
        return smallest

    
solution =Solution()

# print(solution.characterReplacement("AABABBA",1))
print(solution.nextGreatestLetter(["c","f","j"],"a"))
print(solution.nextGreatestLetter(["c","f","j"],"c"))
print(solution.nextGreatestLetter(["x","x","y","y"],"z"))
# print(solution.nextGreatestLetter([3,4,5,1]))
