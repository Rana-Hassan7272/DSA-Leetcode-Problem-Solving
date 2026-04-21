# Problem #5: Group Anagrams

# Link:https://leetcode.com/problems/group-anagrams/


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        🔴 Sorting Approach (Common but NOT optimal):

        Idea:
        - Sort each string and use it as a key
        Example:
            "eat" → "aet"
            "tea" → "aet"
            "ate" → "aet"

        - Group by sorted string

        ❌ Problem:
        - Sorting each string takes O(k log k)
        - For n strings → O(n * k log k)
        - Not optimal when k (string length) is large


        🟢 Optimized Approach (Hashing + Frequency Array):

        💡 Why this is BEST:
        - Strings contain only lowercase letters (a–z)
        - We can represent each string using a frequency count of size 26
        - This avoids sorting → faster

        🔁 Idea:
        - For each string:
            → Create count array of size 26
            → Count frequency of each character
            → Convert it to tuple (so it can be used as dict key)
            → Store string in hashmap

        🔁 Example:
        "eat" → count = [1,0,0,...,1(t),...]
        "tea" → same count → grouped together

        HashMap:
        {
            (count tuple): [list of anagrams]
        }

        💡 Key Insight:
        - Anagrams have same character frequency
        - Tuple of counts uniquely identifies group

        ⚡ Complexity:
        - Time: O(n * k)  ✅ (better than sorting)
        - Space: O(n)
        """


        # 🔹 Hash map: key = frequency tuple, value = list of strings
        anagram_map = {}

        # 🔹 Traverse each string
        for word in strs:

            # 🔹 Create count array of size 26
            count = [0] * 26

            # 🔹 Fill frequency
            for char in word:
                count[ord(char) - ord('a')] += 1

            # 🔹 Convert list to tuple (hashable key)
            key = tuple(count)

            # 🔹 Add to hashmap
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        # 🔹 Return grouped anagrams
        return list(anagram_map.values())
