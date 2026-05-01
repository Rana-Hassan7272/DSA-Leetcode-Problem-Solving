# Problem: Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Recursive (Top-Down without memo):
        #    ❌ Exponential time O(2^n) → recomputation
        #
        # 2. Recursion + Memoization:
        #    ✅ O(n) but extra recursion stack
        #
        # 3. DP Array:
        #    ✅ O(n) but unnecessary space
        #
        # 👉 BEST APPROACH:
        # ✅ Iterative (Bottom-Up, Space Optimized)
        #
        # Why?
        # - Only need last two values
        # - O(1) space
        # - Fastest & cleanest

        # -------------------- BASE CASE --------------------
        if n <= 1:
            return n

        prev2 = 0   # F(0)
        prev1 = 1   # F(1)

        # -------------------- BUILD SEQUENCE --------------------
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


# -------------------- HOW IT WORKS --------------------
# n = 4
# F(0)=0, F(1)=1
#
# i=2 → 1
# i=3 → 2
# i=4 → 3

# -------------------- KEY INSIGHT --------------------
# Only last 2 values needed:
# F(n) = F(n-1) + F(n-2)

# -------------------- TIME COMPLEXITY --------------------
# O(n)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
