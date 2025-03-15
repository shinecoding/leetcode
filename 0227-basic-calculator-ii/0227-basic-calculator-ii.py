class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        prev_operator = '+'
        stack = []
        s += "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ":
                pass
            else:
                if prev_operator == "+":
                    stack.append(num)
                elif prev_operator == "-":
                    stack.append(-num)
                elif prev_operator == "*":
                    prev_num = stack.pop()
                    stack.append((prev_num * num))
                elif prev_operator == "/":
                    prev_num = stack.pop()
                    stack.append(math.trunc(prev_num / num))
                num = 0
                prev_operator = c
        return sum(stack)

