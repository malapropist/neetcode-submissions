class Solution:
    def isValid(self, s: str) -> bool:
        corr={  ')':'(',
                '}':'{',
                ']':'['}
        stack=[]
        for c in s:
            if c in corr and stack and stack[-1]==corr[c]:
                stack.pop(-1)
            else:
                stack.append(c)
        if len(stack)>0:
            return False
        return True