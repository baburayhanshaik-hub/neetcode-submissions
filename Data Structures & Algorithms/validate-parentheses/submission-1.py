class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dhash = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack and dhash[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        print(stack)
        if len(stack)==0:
            return True
        return False