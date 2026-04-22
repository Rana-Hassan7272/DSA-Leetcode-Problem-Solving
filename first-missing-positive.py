# Problem #9: First Missing Positive

# Link:https://leetcode.com/problems/first-missing-positive



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        🧠 Idea Recap (Short & Clear):

        - We must solve in O(n) time and O(1) space
        - So we CANNOT use sorting or extra hashmap

        💡 Trick:
        Use array itself as index map

        👉 Place each number x at index (x - 1)

        Example:
        nums = [3,4,-1,1]

        After placement:
        [1, -1, 3, 4]

        Now:
        index 0 → 1 ✅
        index 1 → not 2 ❌ → answer = 2


        🔁 Core Logic:

        While traversing:
        - If current number is in range [1, n]
        - And it's NOT already in correct position
        → Swap it to its correct position

        ⚠️ Ignore:
        - Negative numbers
        - Zeros
        - Numbers > n


        ⚡ Complexity:
        Time: O(n)
        Space: O(1)
        """


        n = len(nums)
        i = 0

        # 🔹 Step 1: Place numbers at correct indices
        while i < n:
            correct_index = nums[i] - 1

            # 🔹 Check if number is in valid range and not already placed
            if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
                # Swap current element to its correct position
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # 🔹 Step 2: Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 🔹 If all positions correct → answer is n+1
        return n + 1
