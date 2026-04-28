# Problem: Reorganize String
# Link: https://leetcode.com/problems/reorganize-string/

import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (generate all permutations):
        #    ❌ O(n!) → impossible
        #
        # 2. Simple Greedy (just pick different char):
        #    ❌ Can fail when high frequency char dominates
        #
        # 👉 BEST APPROACH:
        # ✅ Max Heap (Greedy) + always pick top 2 elements
        #
        # Why?
        # - Always place most frequent characters first
        # - Prevents same adjacent characters

        # -------------------- STEP 1: COUNT --------------------
        freq = Counter(s)

        # -------------------- IMPOSSIBLE CASE --------------------
        # If any char > (n+1)//2 → impossible
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        # -------------------- STEP 2: MAX HEAP --------------------
        # Use negative freq to simulate max heap
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        result = []

        # -------------------- MAIN LOGIC --------------------
        while len(max_heap) > 1:
            # Take two most frequent chars
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            # Add to result
            result.append(char1)
            result.append(char2)

            # Decrease counts
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))

        # -------------------- HANDLE LAST CHAR --------------------
        if max_heap:
            result.append(max_heap[0][1])

        return "".join(result)


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# s = "aab"
#
# freq = {a:2, b:1}
#
# Heap:
# a(2), b(1)
#
# Step 1: pick a, b → "ab"
# Step 2: pick a → "aba"

# -------------------- KEY INSIGHT --------------------
# Always take TWO most frequent characters
# → ensures no same adjacent

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)
# k = unique chars (≤ 26)

# -------------------- SPACE COMPLEXITY --------------------
# O(k)
