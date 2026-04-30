# Problem: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force:
        #    For each day, check future days
        #    ❌ O(n^2) → too slow (n up to 1e5)
        #
        # 👉 BEST APPROACH:
        # ✅ Monotonic Stack (Decreasing)
        #
        # Why?
        # - We need "next greater element"
        # - Stack helps track unresolved indices efficiently

        n = len(temperatures)
        result = [0] * n

        # Stack stores indices (not values)
        stack = []

        # -------------------- MAIN LOGIC --------------------
        for i in range(n):

            # Resolve all previous colder days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            # Push current index
            stack.append(i)

        return result


# -------------------- HOW IT WORKS --------------------
# temperatures = [73,74,75,71,69,72,76,73]
#
# stack keeps indices of decreasing temps
#
# Example:
# 73 → push
# 74 → pop 73 → result[0]=1
# 75 → pop 74 → result[1]=1
# 71 → push
# 69 → push
# 72 → pop 69,71 → fill answers

# -------------------- KEY INSIGHT --------------------
# Stack = indices of decreasing temperatures
#
# When a higher temp comes → resolve all smaller ones

# -------------------- TIME COMPLEXITY --------------------
# O(n) → each element pushed & popped once

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
