# Problem: Basic Calculator
# Link: https://leetcode.com/problems/basic-calculator/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Using eval():
        #    ❌ Not allowed
        #
        # 2. Converting to postfix (Shunting Yard):
        #    ❌ Overkill for only +, -, ()
        #
        # 👉 BEST APPROACH:
        # ✅ Stack + Running Result + Sign
        #
        # Why?
        # - Only +, - operators → no precedence issue
        # - Parentheses handled via stack
        # - Efficient single pass O(n)

        stack = []
        result = 0
        number = 0
        sign = 1   # +1 for '+', -1 for '-'

        for ch in s:

            # -------------------- BUILD NUMBER --------------------
            if ch.isdigit():
                number = number * 10 + int(ch)

            # -------------------- HANDLE + / - --------------------
            elif ch in ['+', '-']:
                # finalize previous number
                result += sign * number
                number = 0

                # update sign
                sign = 1 if ch == '+' else -1

            # -------------------- HANDLE '(' --------------------
            elif ch == '(':
                # push current state
                stack.append(result)
                stack.append(sign)

                # reset for new sub-expression
                result = 0
                sign = 1

            # -------------------- HANDLE ')' --------------------
            elif ch == ')':
                # finalize current number
                result += sign * number
                number = 0

                # first pop sign, then previous result
                prev_sign = stack.pop()
                prev_result = stack.pop()

                # combine
                result = prev_result + prev_sign * result

            # ignore spaces

        # last number
        result += sign * number

        return result


# -------------------- HOW IT WORKS --------------------
# Example: "(1+(4+5+2)-3)+(6+8)"
#
# Idea:
# - Keep running result
# - Use stack when entering parentheses
# - Restore previous state when exiting

# -------------------- KEY INSIGHT --------------------
# Stack stores:
# [previous_result, previous_sign]
#
# When we hit ')':
# result = prev_result + prev_sign * current_result

# -------------------- TIME COMPLEXITY --------------------
# O(n)

# -------------------- SPACE COMPLEXITY --------------------
# O(n) (stack for parentheses)
