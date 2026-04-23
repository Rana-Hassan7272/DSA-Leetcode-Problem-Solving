# Problem #15: Longest Palindromic Substring

# Link:https://leetcode.com/problems/longest-palindromic-substring


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        🧠 Problem (Simple Words):

        Given a string,
        find the longest substring which is a palindrome

        👉 Palindrome = same forward and backward

        Example:
        "babad" → "bab" or "aba"


        🔴 Brute Force:

        Idea:
        - Generate all substrings
        - Check each if palindrome

        ❌ Problem:
        - O(n^3) → very slow


        🟡 DP Approach:

        - Use 2D table
        - Time: O(n^2)
        - Space: O(n^2)

        ❌ Not optimal (extra space)


        🟢 Best Approach: Expand Around Center

        💡 Key Idea:

        Every palindrome expands from center

        👉 Two cases:
        1. Odd length → center is one char (e.g., "aba")
        2. Even length → center is between chars (e.g., "bb")


        🔁 Strategy:

        For each index i:
            expand(i, i)     → odd length
            expand(i, i+1)   → even length

        Expand while:
            left >= 0 and right < n and s[left] == s[right]


        🔁 Example:
        s = "babad"

        center at 'a':
        expand → "aba"


        💡 Key Insight:
        - Try all centers
        - Expand as much as possible
        - Keep track of longest


        ⚡ Complexity:
        - Time: O(n^2) ✅
        - Space: O(1) ✅
        """


        # 🔹 Helper function to expand around center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""

        # 🔹 Try all centers
        for i in range(len(s)):

            # Odd length
            temp1 = expand(i, i)

            # Even length
            temp2 = expand(i, i+1)

            # Update longest
            if len(temp1) > len(longest):
                longest = temp1
            if len(temp2) > len(longest):
                longest = temp2

        return longest
