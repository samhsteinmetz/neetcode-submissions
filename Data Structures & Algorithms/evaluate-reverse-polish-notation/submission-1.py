class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = 0
        firstGo = True
        op = ('+*/-')
        stack = []
        for t in tokens:
            
            if t in op:
                first = int(stack.pop())
                second = int(stack.pop())
                if t == op[0]:
                    res = first + second
                elif t == op[1]:
                    res = first * second
                elif t == op[2]:
                    res = second / first
                elif t == op[3]:
                    res = second - first
                stack.append(res)
            else:
                stack.append(t)
            
        return int(stack[-1])

            
        