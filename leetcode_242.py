from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       seen_letters = set()

       if len(s)!= len(t):
           return False

       for i in range(len(s)):
           if s[i] not in seen_letters:
               seen_letters.add(s[i])
               
       for j in range(len(t)):
           if t[j] not in seen_letters:
               return False
       return True