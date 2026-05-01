# Problem: Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Convert to infix and evaluate:
        #    ❌ Complex parsing, unnecessary
        #
        # 👉 BEST APPROACH:
        # ✅ Stack
        #
        # Why?
        # - RPN (postfix) is naturally solved using stack
        # - Process left → right
        # - When operator comes → apply on last two elements

        stack = []

        # -------------------- MAIN LOGIC --------------------
        for token in tokens:

            # If operator → pop two elements
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                # Apply operation
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # IMPORTANT: truncate toward zero
                    stack.append(int(float(a) / b))

            else:
                # Operand → push
                stack.append(int(token))

        # Final result
        return stack[0]


# -------------------- HOW IT WORKS --------------------
# tokens = ["2","1","+","3","*"]
#
# stack:
# push 2
# push 1
# '+' → pop(1,2) → 2+1=3 → push 3
# push 3
# '*' → pop(3,3) → 3*3=9

# -------------------- KEY INSIGHT --------------------
# Always:
# - Push numbers
# - When operator → pop 2 → compute → push result

# -------------------- TIME COMPLEXITY --------------------
# O(n)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
