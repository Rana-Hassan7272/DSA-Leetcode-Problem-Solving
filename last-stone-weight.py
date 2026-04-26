# Problem: Last Stone Weight
# Link: https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Sorting every time:
        #    ❌ After each smash, we need to re-sort → O(n log n) each time
        #    ❌ Overall becomes inefficient
        #
        # 2. Brute Force (find max manually each time):
        #    ❌ O(n) per operation → total O(n^2)
        #
        # 👉 BEST APPROACH:
        # ✅ Max Heap (Priority Queue)
        #
        # Why?
        # - Always need top 2 largest elements
        # - Heap gives O(log n) insertion and removal
        #
        # NOTE:
        # Python has min-heap → we simulate max-heap using negative values

        # -------------------- BUILD MAX HEAP --------------------
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # -------------------- MAIN LOOP --------------------
        while len(max_heap) > 1:
            # Get two largest stones
            y = -heapq.heappop(max_heap)  # largest
            x = -heapq.heappop(max_heap)  # second largest

            # If not equal, push the difference
            if y != x:
                heapq.heappush(max_heap, -(y - x))

        # -------------------- RESULT --------------------
        return -max_heap[0] if max_heap else 0


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# [2,7,4,1,8,1]
#
# Max heap:
# [8,7,4,2,1,1]
#
# Step 1: 8 - 7 = 1 → push back
# Step 2: 4 - 2 = 2 → push back
# Step 3: 2 - 1 = 1 → push back
# Step 4: 1 - 1 = 0 → both destroyed
#
# Final: 1

# -------------------- TIME COMPLEXITY --------------------
# O(n log n)
# - Heapify: O(n)
# - Each operation: O(log n)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
# - Heap storage
