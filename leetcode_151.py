class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""

        word_list = s.split()
        # rev = word_list[len(word_list)-1]

        for i in reversed(range(len(word_list))):
            rev = rev+ word_list[i] + " "
            # print(word_list[i])

        rev = rev.rstrip()

        return rev
    
solution = Solution()

# Test cases
print(solution.reverseWords("abcdes hfndshfn"))  # True
print(solution.reverseWords("aaab sdohfjns"))  # False
