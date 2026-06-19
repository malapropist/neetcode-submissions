class Solution:
    def isValid(self, s: str) -> bool:
        corr={  ')':'(',
                '}':'{',
                ']':'['}
        stack=[]
        for c in s:
            if c in corr:
                if stack and stack[-1]==corr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack)>0:
            return False
        return True