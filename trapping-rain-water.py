# Problem #13: Trapping Rain Water

# Link:https://leetcode.com/problems/trapping-rain-water


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        You are given heights of bars.
        After rain, water gets trapped between bars.

        👉 You need to calculate total trapped water.

        Example:
        [0,1,0,2,...]
        → water fills in gaps between taller bars


        🔴 Brute Force:

        Idea:
        - For each index:
            find left max
            find right max
            water = min(left_max, right_max) - height[i]

        ❌ Problem:
        - For each index → scanning left & right
        - Time: O(n^2)


        🟡 Better Approach (Prefix arrays):

        - Precompute left_max[] and right_max[]
        - Time: O(n)
        - Space: O(n)

        ❌ Still not optimal (extra space used)


        🟢 BEST Approach (Two Pointers) — O(1) Space

        💡 Core Idea:

        Water trapped at index depends on:
        min(left_max, right_max) - height[i]

        👉 Instead of storing arrays,
        we track left_max and right_max dynamically


        🔁 Two Pointer Logic:

        left = 0
        right = n - 1

        Maintain:
        left_max
        right_max

        Rule:
        - Move the pointer with smaller height


        💡 Why?

        If height[left] < height[right]:
            → water depends on left_max
            → process left side

        Else:
            → water depends on right_max
            → process right side


        🔁 Step-by-step intuition:

        - If left_max < right_max:
            → left side is limiting
        - Else:
            → right side is limiting


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅
        """


        # 🔹 Initialize pointers
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        # 🔹 Traverse
        while left < right:

            if height[left] < height[right]:

                # Update left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                # Update right_max
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water
