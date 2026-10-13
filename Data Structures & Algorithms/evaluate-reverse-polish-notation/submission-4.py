class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] in "+-*/":
                first = int(stack.pop())
                second = int(stack.pop())
                sym = tokens[i]
                if sym=="/":
                    stack.append(int(float(second)/first))
                elif sym == "+":
                    stack.append(second+first)
                elif sym == "-":
                    stack.append(second-first)
                else:
                    stack.append(second*first)
            else:
                stack.append(tokens[i])
        return int(stack[-1])