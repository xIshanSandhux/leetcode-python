class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        unique = set()

        max_length = 0

        while right<= len(s)-1:
            if s[right] not in unique:
                unique.add(s[right])
                
                max = right-left+1
                if max>max_length:
                    max_length = max
                right+=1
                print(max_length)
                print(unique)
            elif s[right] in unique:
                unique.clear()
                left+=1
                right = left
                print(unique)
            # right+=1
            
        return max_length
    
solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
# print(solution.moveZeroes([1,0,1])) 
# print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.lengthOfLongestSubstring("abcabcbb")) 