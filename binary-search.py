# Problem: Binary Search
# Link: https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Linear Search:
        #    ❌ O(n) → too slow for large input
        #
        # 👉 BEST APPROACH:
        # ✅ Binary Search
        #
        # Why?
        # - Array is sorted
        # - We can eliminate half of search space each step

        # -------------------- INITIAL POINTERS --------------------
        left = 0
        right = len(nums) - 1

        # -------------------- MAIN LOOP --------------------
        while left <= right:
            mid = left + (right - left) // 2  # avoids overflow

            # -------------------- CHECK --------------------
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                # target in right half
                left = mid + 1

            else:
                # target in left half
                right = mid - 1

        # -------------------- NOT FOUND --------------------
        return -1


# -------------------- HOW IT WORKS --------------------
# Example:
# nums = [-1,0,3,5,9,12], target = 9
#
# mid = 3 → nums[3]=5 → go right
# mid = 5 → nums[5]=12 → go left
# mid = 4 → nums[4]=9 → found

# -------------------- TIME COMPLEXITY --------------------
# O(log n)

# -------------------- SPACE COMPLEXITY --------------------
# O(1)
