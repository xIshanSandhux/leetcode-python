from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return [""]
        elif len(strs)==1:
            return[strs]
        
        dict1 = defaultdict(list)
        for i in strs:
            # print("normal word ",i)
            sorted_word = ''.join(sorted(i))
            # print("sorted word",sorted_word)
            dict1[sorted_word].append(i)
            # print("dictionary",dict1[sorted_word])

        return list(dict1.values())
    
solution = Solution()

# Test cases
# print(solution.groupAnagrams([""]))  # [1,2]
# print(solution.groupAnagrams(["a"]))  # [1]
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [1]