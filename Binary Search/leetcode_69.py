class Solution:
    def mySqrt(self, x: int) -> int:

        if x==0:
            return 0
        
        first = 1
        last = x
        middle = 0
        res=0

        while first <=last:
            middle = (first+last)//2
            double = middle*middle
            if double==x:
                return middle
            elif double<x:
                res = middle
                first = middle+1
            elif double>x:
                last = middle-1

        return res
    
    def isPerfectSquare(self, num: int) -> bool:

        first  = 1
        last = num
        middle=0
        sqre = 0

        while first<=last:
            middle = (first+last)//2
            sqre = middle*middle

            if sqre==num:
                return True
            elif sqre >num:
                last = middle-1
            elif sqre<num:
                first = middle+1
        return False
    
solution =Solution()

# print(solution.characterReplacement("AABABBA",1))
# print(solution.mySqrt(4))
# print(solution.mySqrt(8))
print(solution.isPerfectSquare(16))
print(solution.isPerfectSquare(14))