# Problem: Top K Frequent Words
# Link: https://leetcode.com/problems/top-k-frequent-words/

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Sorting all words by frequency:
        #    ❌ O(n log n) → not optimal
        #
        # 2. Only Heap without HashMap:
        #    ❌ Cannot track frequency efficiently
        #
        # 👉 BEST APPROACH:
        # ✅ HashMap (frequency count) + Min Heap (size k)
        #
        # Why?
        # - HashMap gives frequency in O(n)
        # - Min Heap keeps only top k → O(n log k)
        #
        # Special requirement:
        # If same frequency → lexicographically smaller word first

        # -------------------- STEP 1: COUNT FREQUENCY --------------------
        freq = Counter(words)  # {word: count}

        # -------------------- STEP 2: MIN HEAP --------------------
        # Heap will store (frequency, word)
        # BUT:
        # - Lower frequency → smaller
        # - For same freq → lexicographically larger should be removed first
        #
        # So we push (freq, word) but control comparison carefully

        min_heap = []

        for word, count in freq.items():
            heapq.heappush(min_heap, (count, word))

            # Keep heap size k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # -------------------- STEP 3: BUILD RESULT --------------------
        # Heap gives smallest first → reverse later
        result = []

        while min_heap:
            result.append(heapq.heappop(min_heap)[1])

        # Reverse because we want highest freq first
        return result[::-1]


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# ["i","love","leetcode","i","love","coding"], k = 2
#
# Frequency:
# i:2, love:2, leetcode:1, coding:1
#
# Heap (size 2):
# Keep top 2 frequent words
#
# Output:
# ["i","love"] (sorted by freq desc, then lex order)

# -------------------- IMPORTANT NOTE --------------------
# Python heap compares tuple like:
# (freq, word)
#
# If freq same → compares word lexicographically
# BUT:
# We need lexicographically SMALLER word FIRST in result
# So we reverse at end

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)
# - Counting: O(n)
# - Heap ops: O(n log k)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
# - HashMap + heap
