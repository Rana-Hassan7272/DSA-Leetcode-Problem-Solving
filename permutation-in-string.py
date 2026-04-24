# Problem #21: Permutation in String

# Link: https://leetcode.com/problems/permutation-in-string/


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        """
        🧠 Problem (Simple Words):

        - Check if any permutation of s1 exists in s2
        - Means: any substring of s2 should have same characters as s1

        Example:
        s1 = "ab", s2 = "eidbaooo"
        → "ba" exists → True


        🔴 Brute Force:

        Idea:
        - Generate all permutations of s1
        - Check if present in s2

        ❌ Problem:
        - O(n!) → impossible


        🟡 Sorting Approach:

        - Sort s1 and every substring of s2 of same length

        ❌ Problem:
        - O(n * k log k) → slow


        🟢 Optimized Approach (Sliding Window + Fixed Size) — BEST

        💡 Core Idea:

        - Window size = len(s1)
        - Compare frequency of s1 with window in s2

        👉 If frequencies match → permutation found


        🔁 Strategy:

        Step 1:
        - Build frequency array for s1

        Step 2:
        - Use sliding window of size len(s1) on s2

        Step 3:
        - Keep updating window frequency
        - Compare with s1 frequency


        💡 Optimization Trick:

        - Instead of comparing full arrays every time,
          maintain a "matches" count

        matches = number of positions where freq matches

        When matches == 26 → all characters match


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) (26 letters)
        """


        if len(s1) > len(s2):
            return False

        # 🔹 Frequency arrays
        s1_count = [0] * 26
        window_count = [0] * 26

        # 🔹 Fill s1 and initial window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # 🔹 Count matches
        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        left = 0

        # 🔹 Slide window
        for right in range(len(s1), len(s2)):

            # If all match → found permutation
            if matches == 26:
                return True

            # Add new char
            index = ord(s2[right]) - ord('a')
            window_count[index] += 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1

            # Remove left char
            index = ord(s2[left]) - ord('a')
            window_count[index] -= 1

            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] - 1:
                matches -= 1

            left += 1

        return matches == 26
        
