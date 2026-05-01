# Problem: Largest Rectangle in Histogram
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (expand left & right for each bar):
        #    ❌ O(n^2) → too slow for n up to 1e5
        #
        # 2. Precompute left/right boundaries:
        #    ✅ Works but more code
        #
        # 👉 BEST APPROACH:
        # ✅ Monotonic Increasing Stack
        #
        # Why?
        # - Helps find "next smaller element" efficiently
        # - Each bar processed once → O(n)

        stack = []  # store indices
        max_area = 0

        # Add sentinel to flush stack at end
        heights.append(0)

        for i in range(len(heights)):

            # -------------------- CORE LOGIC --------------------
            # Maintain increasing stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                # width calculation
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area


# -------------------- HOW IT WORKS --------------------
# heights = [2,1,5,6,2,3]
#
# Stack keeps indices of increasing heights
#
# When smaller height appears:
# → pop and calculate area
#
# Example:
# 5,6 → next is 2 → pop 6 → area = 6*1
#               → pop 5 → area = 5*2

# -------------------- KEY INSIGHT --------------------
# Each bar is treated as:
# "smallest height in its rectangle"
#
# Find how far it can extend left & right

# -------------------- TIME COMPLEXITY --------------------
# O(n) → each index pushed & popped once

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
