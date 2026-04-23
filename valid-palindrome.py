# Problem #16: Valid Palindrome

# Link:https://leetcode.com/problems/valid-palindrome


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        🧠 Problem (Simple Words):

        - Given a string
        - Ignore:
            → spaces
            → symbols
            → uppercase/lowercase difference

        👉 Check if remaining string is palindrome

        Example:
        "A man, a plan, a canal: Panama"
        → "amanaplanacanalpanama" → palindrome ✅


        🔴 Brute Force:

        Idea:
        - Clean string
        - Reverse and compare

        Works but:
        - Uses extra space O(n)


        🟢 Optimized Approach (Two Pointers) — BEST

        💡 Core Idea:

        - Use two pointers:
            left → start
            right → end

        - Move inward:
            → skip non-alphanumeric
            → compare characters


        🔁 Step-by-step:

        s = "A man, a plan..."

        left → move until valid char
        right → move until valid char

        compare lowercase(s[left]) == lowercase(s[right])

        if not equal → return False


        💡 Key Insight:
        - No need to build new string
        - Do everything in-place


        ⚡ Complexity:
        - Time: O(n) ✅
        - Space: O(1) ✅
        """


        left = 0
        right = len(s) - 1

        while left < right:

            # 🔹 Move left to next alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # 🔹 Move right to previous alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # 🔹 Compare (case insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
