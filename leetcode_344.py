from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer1= 0
        pointer2 = len(s)-1

        while pointer1!=pointer2:
            temp = s[pointer1]
            s[pointer1] = s[pointer2]
            s[pointer2] = temp
            pointer1+=1
            pointer2-=1

            if len(s)%2==0:
                if pointer2 == pointer1+1:
                    temp = s[pointer1]
                    s[pointer1] = s[pointer2]
                    s[pointer2] = temp
                    break
        
        print(s)

solution = Solution()

# Test cases
# print(solution.groupAnagrams([""]))  # [1,2]
# print(solution.isPalindrome(".,"))  # [1]
print(solution.reverseString(["h","e","l","l","o"]))  # [1]
print(solution.reverseString(["H","a","n","n","a","h"]))
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # [1]