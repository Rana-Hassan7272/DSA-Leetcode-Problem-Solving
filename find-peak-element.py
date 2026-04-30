# Problem: Find Peak Element
# Link: https://leetcode.com/problems/find-peak-element/

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Linear Scan:
        #    ❌ O(n) → but question demands O(log n)
        #
        # 👉 BEST APPROACH:
        # ✅ Binary Search
        #
        # Why?
        # - We don’t need global max
        # - Only need ANY peak
        # - Use slope idea (increasing/decreasing)

        # -------------------- BINARY SEARCH --------------------
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # -------------------- CORE IDEA --------------------
            # Compare mid with next element
            if nums[mid] > nums[mid + 1]:
                # We are in descending slope
                # Peak is on LEFT side (including mid)
                right = mid
            else:
                # We are in ascending slope
                # Peak is on RIGHT side
                left = mid + 1

        # -------------------- RESULT --------------------
        return left


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Think like mountains:
#
# If nums[mid] > nums[mid+1] → going DOWN → peak is left
# If nums[mid] < nums[mid+1] → going UP → peak is right
#
# Eventually left == right → peak

# -------------------- EXAMPLE --------------------
# nums = [1,2,3,1]
#
# mid=1 → nums[1]=2 < nums[2]=3 → go right
# mid=2 → nums[2]=3 > nums[3]=1 → go left
# answer = index 2

# -------------------- TIME COMPLEXITY --------------------
# O(log n)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
