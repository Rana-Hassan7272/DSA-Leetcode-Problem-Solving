# Problem #22: Minimum Size Subarray Sum

# Link: https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        - Given array of POSITIVE numbers
        - Find smallest length subarray whose sum >= target

        Example:
        target = 7, nums = [2,3,1,2,4,3]
        → [4,3] → length = 2


        🔴 Brute Force:

        Idea:
        - Try all subarrays
        - Calculate sum

        ❌ Problem:
        - O(n^2)
        - Too slow


        🟢 Optimized Approach (Sliding Window) — BEST

        💡 Why sliding window works?

        👉 Because all numbers are POSITIVE

        This means:
        - If we increase window → sum increases
        - If we shrink window → sum decreases

        👉 This property allows two pointer technique


        🔁 Core Idea:

        - Expand window (right pointer) to increase sum
        - Once sum >= target:
            → try shrinking from left to minimize length


        🔁 Step-by-step:

        nums = [2,3,1,2,4,3], target = 7

        right expands:
        [2,3,1,2] → sum = 8 (valid)

        now shrink:
        remove 2 → [3,1,2] → sum = 6 (stop)

        continue...


        💡 Key Insight:
        - Expand to satisfy condition
        - Shrink to optimize length


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅
        """


        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # shrink window while valid
            while current_sum >= target:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len

                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
