# Problem: Min Stack
# Link: https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Keep single stack + find min each time:
        #    ❌ getMin() becomes O(n)
        #
        # 👉 BEST APPROACH:
        # ✅ Two Stacks
        #
        # Why?
        # - One stack stores values
        # - Second stack tracks minimum at each step
        # - So min is always available in O(1)

        self.stack = []      # main stack
        self.min_stack = []  # track minimums

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.stack.append(val)

        # Push min so far
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return self.min_stack[-1]


# -------------------- HOW IT WORKS --------------------
# push(-2) → stack=[-2], min_stack=[-2]
# push(0)  → stack=[-2,0], min_stack=[-2,-2]
# push(-3) → stack=[-2,0,-3], min_stack=[-2,-2,-3]
#
# getMin() → -3
#
# pop() removes both → min_stack updates automatically

# -------------------- KEY INSIGHT --------------------
# min_stack[i] = minimum of stack[0..i]

# -------------------- TIME COMPLEXITY --------------------
# push → O(1)
# pop → O(1)
# top → O(1)
# getMin → O(1)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
