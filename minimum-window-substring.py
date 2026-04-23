# Problem #14: Minimum Window Substring

# Link:https://leetcode.com/problems/minimum-window-substring


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """
        🧠 Problem (Simple Words):

        Given two strings s and t,
        find the smallest substring in s that contains ALL characters of t
        (including duplicates)

        Example:
        s = "ADOBECODEBANC", t = "ABC"
        → Answer = "BANC"


        🔴 Brute Force:

        Idea:
        - Generate all substrings of s
        - Check if each contains t

        ❌ Problem:
        - Time: O(n^2 * m)
        - Very slow


        🟢 Optimized Approach (Sliding Window + HashMap) — BEST

        💡 Core Idea:

        - Use two pointers (left, right)
        - Expand window until it contains all chars of t
        - Then shrink window to find minimum


        🔑 Key Variables:

        need_map → frequency of chars in t
        window_map → current window frequency

        need_count → total unique chars required
        have_count → how many are satisfied


        🔁 Step-by-step:

        1. Build need_map from t

        2. Expand window (move right):
           → Add char to window_map

        3. If frequency matches:
           → increase have_count

        4. When have_count == need_count:
           → valid window found
           → try shrinking (move left)

        5. Update minimum window


        💡 Key Insight:
        - Expand to satisfy condition
        - Shrink to optimize size


        ⚡ Complexity:
        - Time: O(m + n) ✅
        - Space: O(n)
        """


        if len(t) > len(s):
            return ""

        # 🔹 Build frequency map for t
        need_map = {}
        for char in t:
            need_map[char] = need_map.get(char, 0) + 1

        window_map = {}

        have = 0
        need = len(need_map)

        res = [-1, -1]
        res_len = float("inf")

        left = 0

        # 🔹 Expand window
        for right in range(len(s)):
            char = s[right]
            window_map[char] = window_map.get(char, 0) + 1

            # 🔹 Check if requirement met
            if char in need_map and window_map[char] == need_map[char]:
                have += 1

            # 🔹 Shrink window if valid
            while have == need:

                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove left char
                left_char = s[left]
                window_map[left_char] -= 1

                if left_char in need_map and window_map[left_char] < need_map[left_char]:
                    have -= 1

                left += 1

        left, right = res
        return s[left:right+1] if res_len != float("inf") else ""
        
