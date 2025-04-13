# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        first = 1
        last = n
        middle = 0
        api = False

        while first <=last:
            middle = (first+last)//2
            api = isBadVersion(middle)
            if api == False:
                first = middle+1
            elif api == True:
                last = middle-1

        return first
    
    # The isBadVersion API is already defined for you.
    def isBadVersion(version: int) -> bool:
        return False