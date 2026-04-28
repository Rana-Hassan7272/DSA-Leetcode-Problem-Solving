# Problem: Find Median from Data Stream
# Link: https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder(object):

    def __init__(self):
        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Sorting after every insertion:
        #    ❌ addNum = O(n log n) → too slow for 50k operations
        #
        # 2. Inserting into sorted list:
        #    ❌ O(n) insertion → inefficient
        #
        # 👉 BEST APPROACH:
        # ✅ Two Heaps (Max Heap + Min Heap)
        #
        # Why?
        # - Left side (smaller half) → max heap
        # - Right side (larger half) → min heap
        # - Median always lies at the top(s)

        # Max heap (store negative values)
        self.small = []  # left half (max heap)

        # Min heap
        self.large = []  # right half (min heap)


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        # -------------------- STEP 1: ADD TO MAX HEAP --------------------
        heapq.heappush(self.small, -num)

        # -------------------- STEP 2: BALANCE ORDER --------------------
        # Ensure every element in small <= elements in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # -------------------- STEP 3: BALANCE SIZE --------------------
        # Maintain size property:
        # len(small) == len(large) OR len(small) = len(large) + 1

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self):
        """
        :rtype: float
        """

        # -------------------- FIND MEDIAN --------------------
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2.0


# -------------------- HOW IT WORKS (INTUITION) --------------------
# small (max heap): stores smaller half
# large (min heap): stores larger half
#
# Example:
# add 1 → small = [1]
# add 2 → small = [1], large = [2]
# median = (1+2)/2 = 1.5
#
# add 3 → small = [2,1], large = [3]
# median = 2

# -------------------- KEY INVARIANTS --------------------
# 1. All elements in small ≤ elements in large
# 2. Size difference ≤ 1

# -------------------- TIME COMPLEXITY --------------------
# addNum: O(log n)
# findMedian: O(1)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
