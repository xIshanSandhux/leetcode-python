class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        dict1 = {}

        for i in range(len(magazine)):
            if magazine[i] not in dict1:
                dict1[magazine[i]] = 1
            elif magazine[i] in dict1:
                num = dict1.get(magazine[i])
                dict1[magazine[i]] = num+1
        # print(dict1)
        for i in range(len(ransomNote)):
            # print("heelo")
            if ransomNote[i] in dict1:
                # print("heelo if")
                num = dict1.get(ransomNote[i])
                print(num , ransomNote[i])
                if num<=0:
                    return False
                dict1[ransomNote[i]] = num-1
            elif ransomNote[i] not in dict1:
                return False

        return True
    
solution = Solution()

# Test cases
print(solution.canConstruct("a","b"))  # False
print(solution.canConstruct("dehifb","hhjdgjbhahaagihhhhhajjibjffhijehda"))  # True
# print(solution.canConstruct("aa","ab"))  # False
# print(solution.canConstruct("aa","aab"))  # True