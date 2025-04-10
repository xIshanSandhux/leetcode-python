from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=1
        curr_k=0
        max_length=1
        max_length_repeating=1
        positions = {}
        pos_list = []

        while left<=right and right<len(s):
            if right<len(s) and (k>curr_k) and (s[right] != s[left]):
                pos_list.append(right)
                print(pos_list)
                right+=1
                curr_k+=1
                print(curr_k)
                max_length+=1

            if right<len(s) and (k<=curr_k) and (s[right]!=s[left]):
                # positions[max_length] = pos_list[:]
                if max_length not in positions:
                        positions[max_length] = pos_list[:]
                pos_list.clear()
                max_length=1
                max_length_repeating=0
                curr_k=0
                left+=1
                right = left+1
            elif right<len(s) and s[right] == s[left]:
                right+=1
                max_length+=1
                max_length_repeating+=1

            if (k<=curr_k):
                if max_length not in positions:
                        positions[max_length] = pos_list[:]

        
        if max_length_repeating == len(s):
             return max_length_repeating
        else:
             largest = max(positions.keys())
        # print (largest)
        # if largest in positions:
        #     l = positions.get(largest)
        #     for i in l:

        
        print(positions.keys(),positions.values())
        return largest
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

solution = Solution()

# Test cases
# print(solution.characterReplacement("AABABBA",1))
print(solution.characterReplacement("ABBB",2))
