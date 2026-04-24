# Problem #19: 3Sum

# Link: https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        🧠 Problem (Simple Words):

        - Find all unique triplets (a, b, c)
        - Such that: a + b + c = 0
        - No duplicate triplets allowed


        🔴 Brute Force:

        Idea:
        - Try all triplets (i, j, k)

        ❌ Problem:
        - Time: O(n^3)
        - Too slow (n can be 3000)


        🟡 Better (Hashing):

        Idea:
        - Fix one element
        - Use hashmap/set for remaining two

        ❌ Problem:
        - Hard to avoid duplicates cleanly
        - Extra space used


        🟢 Optimized Approach (Sorting + Two Pointer) — BEST

        💡 Core Idea:

        - First sort the array
        - Then fix one element
        - Solve remaining as 2Sum using two pointers

        👉 Why sorting?
        - Helps avoid duplicates easily
        - Enables two pointer technique


        🔁 Step-by-step:

        nums = [-1,0,1,2,-1,-4]

        After sorting:
        [-4,-1,-1,0,1,2]

        Now:
        Fix i = -4
        → find two numbers such that sum = 4

        Fix i = -1
        → find two numbers such that sum = 1

        and so on...


        🔑 Two Pointer Logic:

        left = i + 1
        right = n - 1

        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            → store answer
            → move both pointers

        if total < 0:
            → need bigger sum → move left

        if total > 0:
            → need smaller sum → move right


        🔥 Handling Duplicates (VERY IMPORTANT):

        - Skip same i values
        - After finding triplet:
            skip duplicates of left and right


        ⚡ Complexity:
        - Time: O(n^2) ✅
        - Space: O(1) (ignoring output)
        """


        nums.sort()  # 🔹 sort array
        res = []

        n = len(nums)

        for i in range(n):

            # 🔹 skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 🔹 skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # 🔹 skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # move both pointers
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
