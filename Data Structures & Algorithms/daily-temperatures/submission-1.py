class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            curr= temperatures[i]
            while stack and stack[-1][1] < curr:
                idx, temp = stack.pop()
                res[idx] = i - idx

            stack.append((i, curr))
        return res

