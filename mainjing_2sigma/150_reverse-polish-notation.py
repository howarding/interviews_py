# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import operator

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        stk = []
        for element in tokens:
            if element not in {"+", "-", "*" ,"/"}:
                stk.append(int(element))
            else:
                b, a = stk.pop(), stk.pop()
                if element == "+":
                    stk.append(a + b)
                elif element == "-":
                    stk.append(a - b)
                elif element == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(operator.truediv(a, b)))
        return stk.pop()


if __name__ == "__main__":
    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["4", "13", "5", "/", "+"]
    print sol.evalRPN(tokens)