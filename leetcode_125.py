class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == " ":
            return True
        
        if len(s)==1:
            return True

        letter_only = ""

        for i in s:
            if i.isalnum():
                letter_only+= i.lower()
            
        
        if len(letter_only)==0:
            return False
        
        if len(letter_only)%2 !=0:
            point1 = 0
            point2 = len(letter_only)-1

            while point1 !=point2:
                if letter_only[point1] == letter_only[point2]:
                    point1+=1
                    point2-=1
                else:
                    return False
        else:
            point1 = 0
            point2 = len(letter_only)-1
            if point2 == point1+1:
                if letter_only[point1] == letter_only[point2]:
                    return True
                else:
                    return False
            else:
                print("Hello")
                counter = 0
                print(letter_only)
                while point2 != point1+1:
                    print(point2,"point 2")
                    print(point1,"point 1")
                    if letter_only[point1] == letter_only[point2]:
                        print(letter_only[point1],"point 1 alpha")
                        print(letter_only[point2],"point2 alpha")
                        point1+=1
                        point2-=1
                        counter+=2
                        print (counter)
                    else:
                        return False
                if point2 == point1+1:
                    if letter_only[point1] == letter_only[point2]:
                        return True
                    else:
                        return False
                    
        return True
    
solution = Solution()

# Test cases
# print(solution.groupAnagrams([""]))  # [1,2]
# print(solution.isPalindrome(".,"))  # [1]
print(solution.isPalindrome("race a car"))  # [1]
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # [1]