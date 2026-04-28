# Problem: Merge k Sorted Lists
# Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (collect all values + sort):
        #    ❌ O(n log n) + extra space
        #
        # 2. Merge one by one:
        #    ❌ O(k * n) → inefficient when k is large
        #
        # 3. Divide & Conquer (merge pairs):
        #    ✅ O(n log k) → good
        #
        # 👉 BEST APPROACH:
        # ✅ Min Heap (Priority Queue)
        #
        # Why?
        # - Always extract smallest among k heads
        # - Efficient merging across lists

        # -------------------- EDGE CASE --------------------
        if not lists:
            return None

        # -------------------- MIN HEAP --------------------
        # Store (value, index, node)
        # index needed to avoid comparison error between nodes
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # -------------------- DUMMY NODE --------------------
        dummy = ListNode(0)
        curr = dummy

        # -------------------- MAIN LOOP --------------------
        while heap:
            val, i, node = heapq.heappop(heap)

            # Add smallest node to result
            curr.next = node
            curr = curr.next

            # Move forward in that list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# -------------------- HOW IT WORKS (INTUITION) --------------------
# lists = [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
#
# Heap initially:
# [1,1,2]
#
# Step-by-step:
# pick smallest → attach → push next
#
# Always maintain k candidates

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)
# n = total nodes
# k = number of lists

# -------------------- SPACE COMPLEXITY --------------------
# O(k)
# heap stores at most k elements
