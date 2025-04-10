from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        left = 0
        right = 1

        while right <= (len(prices)-1):
            if prices[left]>prices[right]:
                print(prices[left], "prices left")
                print(max_profit, "max profit")
                print(prices[right], "prices right")
                left+=1
                right = left+1
            elif prices[left]<=prices[right]:
                max = prices[right] - prices[left]
                if max > max_profit:
                    max_profit = max
                    print(max_profit)
                right+=1
            

        return max_profit
    
solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
# print(solution.moveZeroes([1,0,1])) 
# print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([2,1,2,1,0,1,2])) 