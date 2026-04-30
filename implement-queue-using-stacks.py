# Problem: Implement Queue using Stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Direct list (append + pop(0)):
        #    ❌ pop(0) is O(n) → shifts all elements
        #
        # 👉 BEST APPROACH:
        # ✅ Two Stacks (Amortized O(1))
        #
        # Why?
        # - Stack is LIFO, Queue is FIFO
        # - Use two stacks to reverse order

        # stack for push
        self.in_stack = []

        # stack for pop/peek
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Always push to in_stack
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """

        # -------------------- LAZY TRANSFER --------------------
        # Only move elements when needed
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """

        # Same logic as pop but don't remove
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack


# -------------------- HOW IT WORKS --------------------
# push: [1,2,3] → in_stack
#
# pop:
# move → out_stack becomes [3,2,1]
# pop → 1 (FIFO)

# -------------------- KEY INSIGHT --------------------
# Each element:
# - pushed once
# - popped once
#
# 👉 Total operations = O(n)

# -------------------- TIME COMPLEXITY --------------------
# push → O(1)
# pop → amortized O(1)
# peek → amortized O(1)
# empty → O(1)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
