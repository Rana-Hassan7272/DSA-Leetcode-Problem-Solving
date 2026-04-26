# Problem: Word Ladder
# Link: https://leetcode.com/problems/word-ladder/

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # -------------------- WHY NOT OTHER TECHNIQUES --------------------
        # 1. Brute Force (try all transformations):
        #    ❌ Exponential → impossible for constraints
        #
        # 2. DFS:
        #    ❌ Does NOT guarantee shortest path
        #    ❌ Can go deep into wrong paths → TLE
        #
        # 3. Normal BFS:
        #    ✅ Finds shortest path
        #    ❌ But still slow for large wordList (explores too many states)
        #
        # 👉 BEST APPROACH:
        # ✅ Bidirectional BFS
        #
        # Why?
        # Instead of searching from one side:
        # begin → end
        #
        # We search from BOTH sides:
        # begin → ← end
        #
        # This reduces search space drastically

        # -------------------- EDGE CASE --------------------
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # -------------------- INITIALIZE --------------------
        beginSet = set([beginWord])
        endSet = set([endWord])

        visited = set()
        length = 1

        # -------------------- MAIN LOOP --------------------
        while beginSet and endSet:

            # Always expand the smaller set (optimization)
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            next_level = set()

            for word in beginSet:
                word_chars = list(word)

                # Try changing each character
                for i in range(len(word_chars)):
                    original_char = word_chars[i]

                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word_chars[i] = c
                        new_word = "".join(word_chars)

                        # If found connection
                        if new_word in endSet:
                            return length + 1

                        # If valid transformation
                        if new_word in wordSet and new_word not in visited:
                            next_level.add(new_word)
                            visited.add(new_word)

                    # Restore original character
                    word_chars[i] = original_char

            # Move to next level
            beginSet = next_level
            length += 1

        return 0


# -------------------- HOW IT WORKS (INTUITION) --------------------
# Example:
# "hit" → "cog"
#
# Forward BFS:
# hit → hot → dot → dog → cog
#
# Bidirectional BFS:
# hit → hot → dot
# cog ← dog ← log
#
# Meet in middle → MUCH faster

# -------------------- TIME COMPLEXITY --------------------
# O(N * M * 26)
# N = number of words
# M = word length
#
# But practically much faster due to bidirectional pruning

# -------------------- SPACE COMPLEXITY --------------------
# O(N)
# - wordSet + visited + BFS sets
