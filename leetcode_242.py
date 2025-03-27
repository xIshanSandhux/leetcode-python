from typing import List


class Solution:
    # Leetcode problem 242 Valid Anaggram
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            elif s[i] in dict1:
                num = dict1.get(s[i])
                dict1[s[i]] = num + 1

        dict2 = {}

        for j in range(len(t)):
            if t[j] not in dict2:
                dict2[t[j]] = 1
            elif t[j] in dict2:
                num2 = dict2.get(t[j])
                dict2[t[j]] = num2 + 1

        if len(dict1)!= len(dict2):
            return False
            

        for t in dict1:
            if t not in dict2:
                return False
            else:
                if dict1.get(t) != dict2.get(t):
                    return False

        return True 


solution = Solution()

# Test cases
print(solution.isAnagram("aa","a"))  # True
# print(solution.containsDuplicateoptimized([1, 2, 3, 4, 5, 7]))  # False
# print(solution.containsDuplicateoptimized([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True