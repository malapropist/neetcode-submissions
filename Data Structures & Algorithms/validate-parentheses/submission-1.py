class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack and i in ")}]":
                if i == ")" and stack[-1]=="(":
                    stack.pop()
                elif i == "}" and stack[-1]=="{":
                    stack.pop()
                elif i == "]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif i in "{[(":
                stack.append(i)
            else:
                return False
        if not stack:
            return True
        else:
            return False