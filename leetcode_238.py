from typing import List


class Solution:
    def productExceptSelfbrute(self, nums: List[int]) -> List[int]:
        prod = []
        product=1
        for i in range(len(nums)):
            for counter in range(len(nums)):
                # print("counter inner loop: ",counter)
                if nums[i]!=0:
                    product = nums[counter]*product
                    print(product)
            if nums[i]!= 0:
                product = int (product/nums[i])
                prod.append(product)
            elif nums[i]==0:
                prod.append(product)
            product = 1
        
        return prod
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            return_list[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            return_list[i] *=postfix
            postfix *=nums[i]

        return return_list
        
solution = Solution()

# Test cases
print(solution.productExceptSelf([1,2,3,4]))  # [1,2]
print(solution.productExceptSelf([-1,1,0,-3,3]))  # [1]