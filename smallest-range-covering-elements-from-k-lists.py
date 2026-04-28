# Problem: Smallest Range Covering Elements from K Lists
# Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (check all combinations):
        #    ❌ Exponential → impossible
        #
        # 2. Merge all + sliding window:
        #    ❌ Requires sorting all elements → O(n log n)
        #
        # 👉 BEST APPROACH:
        # ✅ Min Heap + Track Current Maximum
        #
        # Why?
        # - Similar to "Merge K Sorted Lists"
        # - Always keep one element from each list
        # - Track min (heap top) and max → gives range

        # -------------------- INITIALIZE --------------------
        # Heap stores: (value, list_index, element_index)
        heap = []
        current_max = float('-inf')

        # Put first element of each list
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            current_max = max(current_max, val)

        # Initial answer range
        start, end = float('-inf'), float('inf')

        # -------------------- MAIN LOOP --------------------
        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)

            # Update best range
            if current_max - min_val < end - start:
                start, end = min_val, current_max

            # Move forward in the same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # cannot include all lists anymore

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

            # Update current max
            current_max = max(current_max, next_val)

        return [start, end]


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Keep one element from each list:
#
# Example:
# [4,10,15,24,26]
# [0,9,12,20]
# [5,18,22,30]
#
# Start:
# heap = [4,0,5], max = 5 → range [0,5]
#
# Move smallest pointer forward → update range
# Always maintain k elements

# -------------------- KEY INSIGHT --------------------
# At any point:
# Range = [min(heap), current_max]
#
# Try to shrink range by moving the minimum forward

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)
# n = total elements
# k = number of lists

# -------------------- SPACE COMPLEXITY --------------------
# O(k)
# heap stores one element from each list
