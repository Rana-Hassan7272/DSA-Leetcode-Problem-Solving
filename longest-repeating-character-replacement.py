# Problem #20: Longest Repeating Character Replacement

# Link: https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        - You can change at most k characters
        - Goal: make a substring where all characters are SAME
        - Return maximum possible length

        Example:
        "AABABBA", k = 1 → answer = 4


        🔴 Brute Force:

        Idea:
        - Try all substrings
        - For each, count replacements needed

        ❌ Problem:
        - O(n^2) → too slow


        🟢 Optimized Approach (Sliding Window) — BEST

        💡 Core Idea:

        - Use sliding window
        - Track most frequent character in window

        👉 Important condition:

        window size - max_frequency <= k

        WHY?

        - window size = total characters
        - max_frequency = most common char count

        👉 Remaining chars = need to replace

        If replacements needed <= k → valid window


        🔁 Example:

        window = "AABAB"
        max_freq = 3 (A)
        size = 5

        replacements needed = 5 - 3 = 2


        🔁 Strategy:

        - Expand window (right++)
        - Update frequency count
        - Track max_frequency

        - If window becomes invalid:
            → shrink from left

        - Track max length


        💡 Key Insight:
        - We don't need exact max freq after shrink
        - Keeping old max_freq still works (optimization trick)


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) (only 26 letters)
        """


        count = {}   # frequency map
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            # update frequency
            count[char] = count.get(char, 0) + 1

            # track max frequency in window
            if count[char] > max_freq:
                max_freq = count[char]

            # check if window invalid
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update result
            current_len = right - left + 1
            if current_len > max_length:
                max_length = current_len

        return max_length
