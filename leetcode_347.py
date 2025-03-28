from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 ={}

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            elif nums[i] in dict1:
                num = dict1.get(nums[i])
                dict1[nums[i]] = num+1

        arr = []
        for num, cnt in dict1.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    

solution = Solution()

# Test cases
print(solution.topKFrequent([1,1,1,2,2,3],2))  # [1,2]
print(solution.topKFrequent([1],1))  # [1]