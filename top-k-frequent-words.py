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

        # -------------------- WHY THIS APPROACH --------------------
        # We MUST maintain correct order inside heap:
        # - Higher frequency → higher priority
        # - If tie → lexicographically smaller word → higher priority
        #
        # But heap is MIN heap → so we reverse logic:
        # - Smaller freq → worse
        # - If same freq → lexicographically larger → worse

        freq = Counter(words)

        # -------------------- CUSTOM OBJECT --------------------
        class Word:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq
            
            def __lt__(self, other):
                # Define "worse" element for min heap
                if self.freq == other.freq:
                    return self.word > other.word   # reverse lex
                return self.freq < other.freq      # smaller freq worse

        # -------------------- MIN HEAP --------------------
        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, Word(word, count))

            if len(heap) > k:
                heapq.heappop(heap)

        # -------------------- BUILD RESULT --------------------
        # Extract and reverse (because min heap)
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]


# -------------------- WHY THIS WORKS --------------------
# Heap top = WORST element
# So we remove:
# - smaller freq
# - or lexicographically larger (if tie)
#
# Ensures heap always keeps BEST k elements

# -------------------- TIME COMPLEXITY --------------------
# O(n log k)

# -------------------- SPACE COMPLEXITY --------------------
# O(n)
