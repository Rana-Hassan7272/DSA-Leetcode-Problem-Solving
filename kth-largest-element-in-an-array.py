# Problem: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Sorting:
        #    ❌ O(n log n) → unnecessary full sort
        #
        # 2. Max Heap (store all elements):
        #    ❌ O(n) space + O(n log n) operations
        #
        # 3. Quickselect:
        #    ✅ Best average O(n)
        #    ❌ But more complex
        #
        # 👉 BEST PRACTICAL APPROACH:
        # ✅ Min Heap of size k
        #
        # Why?
        # - Keep ONLY k largest elements
        # - Smallest among them = kth largest
        # - Efficient and easy to implement

        # -------------------- CORE IDEA --------------------
        # Maintain a min heap of size k:
        # - Add elements one by one
        # - If size > k → remove smallest
        #
        # At end:
        # heap[0] = kth largest element

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # Keep only k largest elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Root = kth largest
        return min_heap[0]


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# nums = [3,2,1,5,6,4], k = 2
#
# Step-by-step heap (size k=2):
# [3]
# [2,3]
# [2,3] (1 ignored)
# [3,5]
# [5,6]
# [5,6] (4 ignored)
#
# Answer = 5

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)
# - Each insertion/removal: O(log k)

# -------------------- SPACE COMPLEXITY --------------------
# O(k)
# - Heap stores only k elements
