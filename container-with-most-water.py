# Problem #18: Container With Most Water

# Link:https://leetcode.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        - You are given heights of vertical lines
        - Pick TWO lines such that they form a container
        - Maximize water stored

        👉 Water = width * min(height[left], height[right])

        Example:
        [1,8,6,2,5,4,8,3,7]
        → answer = 49


        🔴 Brute Force:

        Idea:
        - Try all pairs (i, j)
        - Compute area

        ❌ Problem:
        - Time: O(n^2)
        - Too slow


        🟢 Optimized Approach (Two Pointers) — BEST

        💡 Core Idea:

        - Start with widest container:
            left = 0
            right = n - 1

        - Calculate area

        - Move pointer of SMALLER height


        🔑 Why move smaller one?

        Area formula:
        area = width * min(height[left], height[right])

        👉 Width always decreases (as pointers move)

        So to increase area:
        - We need a taller height

        ❌ Moving taller pointer:
            → min height stays same or decreases
            → area cannot increase

        ✅ Moving smaller pointer:
            → chance to find taller height
            → area may increase


        🔁 Step-by-step:

        left=0, right=8
        area = min(1,7)*8 = 8

        move left (smaller)

        left=1, right=8
        area = min(8,7)*7 = 49 ✅


        💡 Key Insight:
        - Greedy decision:
          always move the limiting (smaller) height


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅
        """


        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            # 🔹 Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            if area > max_area:
                max_area = area

            # 🔹 Move pointer of smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
