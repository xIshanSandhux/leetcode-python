class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # if (s[0]==')' or s[0]=='}' or s[0]==']'):
        #     return False
        
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif (s[i]==')' or s[i]=='}' or s[i]==']') and len(stack)==0:
                return False
            elif s[i]==')' and len(stack)>0:
                last = stack.pop()
                if last != '(':
                    return False
            elif s[i]=='}'  and len(stack)>0:
                last = stack.pop()
                if last != '{':
                    return False
            elif s[i]==']' and len(stack)>0:
                last = stack.pop()
                if last != '[':
                    return False 
                
        if len(stack)!=0:
            return False
        
        return True
    
solution = Solution()

# Test cases
# print(solution.moveZeroes([0,1,0,3,12]))  
# print(solution.moveZeroes([1,0,1])) 
print(solution.isValid("()")) # [4,2,4,3,5,1,0,0,0,0]
print(solution.isValid("()[]{}")) # [4,2,4,3,5,1,0,0,0,0]

