class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures) 

        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                ans[prev_day] = day - prev_day

            stack.append(day)
        return ans