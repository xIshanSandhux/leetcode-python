class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1 = {}
        num1=0

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            elif s[i] in dict1:
                num = dict1.get(s[i])
                dict1[s[i]] = num+1

        num_values = list(dict1.values())
        # print(num_values)
        prev = num_values[0]
        for num in num_values:
            if prev!= num:
                return False
        return True
    
solution = Solution()

# Test cases
print(solution.areOccurrencesEqual("aabb"))  # True
print(solution.areOccurrencesEqual("aaab"))  # False