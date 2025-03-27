from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}

        for i in range(len(s)):
            if s[i] in dict1.