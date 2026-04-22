# Problem #8: Longest Substring Without Repeating Characters

# Link:https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        🧠 Problem (Simple Words):

        Given a string s,
        find the length of the longest substring with NO repeating characters.

        👉 Important:
        - Substring = continuous
        - No duplicates allowed

        Example:
        "abcabcbb" → "abc" → length = 3


        🔴 Brute Force:

        Idea:
        - Generate all substrings
        - Check each for duplicates

        ❌ Time Complexity:
        - O(n^2) or worse
        - Not efficient


        🟢 Optimized Approach (Sliding Window) — BEST

        💡 Key Idea:
        - Use two pointers (left, right)
        - Maintain a "window" with unique characters

        👉 Expand window (move right)
        👉 If duplicate found → shrink window (move left)


        🔁 Step-by-step:

        s = "abcabcbb"

        Window expands:
        "a" → "ab" → "abc" ✅

        Next char "a" → duplicate
        → Move left until duplicate removed

        Continue...


        💡 Key Insight:
        - Keep track of characters in current window
        - If duplicate → shrink window until valid again


        ⚙️ Two Ways:
        1. Using set (simple)
        2. Using hashmap (faster jump of left pointer) ✅


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(n)
        """


        # 🔹 HashMap to store last seen index of each character
        char_map = {}

        left = 0
        max_length = 0

        # 🔹 Expand window using right pointer
        for right in range(len(s)):
            char = s[right]

            # 🔹 If char seen and inside current window
            if char in char_map and char_map[char] >= left:
                # Move left pointer to avoid duplicate
                left = char_map[char] + 1

            # 🔹 Update last seen index
            char_map[char] = right

            # 🔹 Update max length
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length

        return max_length
