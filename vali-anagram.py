# Problem #3: Valid Anagram

# Link:https://leetcode.com/problems/valid-anagram/


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        🔴 Brute Force Approach:

        Idea:
        - Sort both strings and compare

        Example:
        sorted(s) == sorted(t)

        ❌ Problem:
        - Time Complexity: O(n log n)
        - Not optimal


        🟢 Optimized Approach (Array Technique - BEST for lowercase letters):

        Idea:
        - Since only lowercase English letters (a–z)
        - Use an array of size 26
        - Each index represents a character

        Mapping:
        'a' → index 0
        'b' → index 1
        ...
        'z' → index 25

        🔁 Step-by-step:
        s = "anagram", t = "nagaram"

        - Create array of size 26 → all 0
        - For s → increment counts
        - For t → decrement counts

        If all values = 0 → anagram

        💡 Key Insight:
        - Avoid hashing → faster constant time
        - Direct index access using ASCII

        ⚡ Complexity:
        - Time: O(n)
        - Space: O(1) (fixed size 26 array)
        """

        # 🔹 If lengths differ → not anagram
        if len(s) != len(t):
            return False

        # 🔹 Create count array of size 26
        count = [0] * 26

        # 🔹 Traverse both strings together
        for i in range(len(s)):
            # Increment for s
            count[ord(s[i]) - ord('a')] += 1

            # Decrement for t
            count[ord(t[i]) - ord('a')] -= 1

        # 🔹 Check if all values are zero
        for val in count:
            if val != 0:
                return False

        return True
